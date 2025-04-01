<template>
    <div class="manager-window-container" >
        <div class="manager-window" ref="chatWindow" >
            <div v-for="(message, index) in messages" :key="index" :class="['message',message.is_sender?'sender':'receiver']">
                <div class="avatar" v-if="!message.is_sender"><img src="@/assets/img/robot.png" alt="机器人"></div>
                <div class="avatar" v-else><img src="@/assets/img/user.png" alt="uesr"></div>
                <div class="time_content">
                    <div class="time">{{ message.timestamp }}</div>
                    <div class="message-content" v-html="formatMessage(message.message)" @click="handleCopy"></div>
                </div>
            </div>
        </div>
    </div>
    <div class="send">
          <input v-model="message_sended" type="message" placeholder="请输入消息内容" @keydown.enter="sendMessage">
          <button @click="sendMessage"><img src="@/assets/img/send.png" alt="发送"></button>
    </div>
</template>

<script>

import { getGptResponse , getCharHistory} from "@/services/gptResponse.js"
import { marked } from 'marked';
import hljs from 'highlight.js';
import 'highlight.js/styles/github.css'; // 选择代码高亮主题
import DOMPurify from 'dompurify';


export default {
    name: 'managerWindow',
    data() {
        return {
            user:"user",
            message_sended:"",
            messages: [],
            issending : false
        }
    },
    props: {
        model:{
            type: String,
            default:'GPT-3.5-turbo'
        },
        isLogined: {
            type: Boolean,
            default: false
        }
    },
    methods: { 
        async sendMessage() {
            if (this.issending) {return}
            if(this.message_sended.trim() === '') return
            this.issending = true
            try{
                this.messages.push({message:this.message_sended, is_sender: true, timestamp: this.getCurrentTime()})
                this.messages.push({message:'⏳......', is_sender: false,timestamp:''})
                const response = await getGptResponse(this.user,this.message_sended,this.model,this.getCurrentTime())
                this.messages.pop()
                this.messages.push({message:response, is_sender: false, timestamp: this.getCurrentTime()})
                this.message_sended = ''
                sessionStorage.setItem('qaList', JSON.stringify(this.messages));
            }
            catch(error){
                console.log(error)
            }
            this.$nextTick(() => {
            const chatWindow = this.$refs.chatWindow;
            chatWindow.scrollTop = chatWindow.scrollHeight;
            this.issending = false
        });
        },
        async getCharHistory() {
            try{
                const response = await getCharHistory()
                this.messages = response.data
            }
            catch(error){
                console.log(error)
            }
        },
        getCurrentTime() {
            const now = new Date();
            const year = now.getFullYear();
            const month = String(now.getMonth() + 1).padStart(2, '0'); // 月份从 0 开始，需要 +1
            const day = String(now.getDate()).padStart(2, '0');
            const hours = String(now.getHours()).padStart(2, '0');
            const minutes = String(now.getMinutes()).padStart(2, '0');
            const seconds = String(now.getSeconds()).padStart(2, '0');
            return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
        },
        saveQA(question,is_sender,timestamp){
            const qaList = JSON.parse(sessionStorage.getItem('qaList')) || []
            qaList.push({message:question, is_sender: is_sender, timestamp: timestamp})
            sessionStorage.setItem('qaList', JSON.stringify(qaList))
        },
        deleteMessage(){
            sessionStorage.removeItem('qaList')
            this.messages = []
        },
        formatMessage(rawText) {
            marked.setOptions({
                highlight: (code, lang) => {
                const validLang = hljs.getLanguage(lang) ? lang : 'plaintext';
                return hljs.highlight(validLang, code).value;
                },
                renderer: new marked.Renderer({
                    code(code, lang, escaped) {
                        const langLabel = lang || 'text';
                        return `
                        <div class="code-block">
                            <div class="code-header">
                            <span class="lang-label">${langLabel}</span>
                            <button class="copy-btn" data-lang="${langLabel}">Copy</button>
                            </div>
                            <pre><code class="hljs language-${lang}">${escaped ? code : hljs.highlightAuto(code).value}</code></pre>
                        </div>
                        `;
                    }
                })
            });

            return DOMPurify.sanitize(marked(rawText || ''));
        },
        handleCopy(e) {
            if (e.target.classList.contains('copy-btn')) {
                const codeBlock = e.target.closest('.code-block');
                const code = codeBlock?.querySelector('code')?.innerText;
                
                if (code) {
                navigator.clipboard.writeText(code).then(() => {
                    const originalText = e.target.textContent;
                    e.target.textContent = 'Copied!';
                    setTimeout(() => {
                    e.target.textContent = originalText;
                    }, 2000);
                });
                }
            }
        }
    },
    created() {
        if (sessionStorage.getItem('qaList')==null) {
            this.messages = [
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                
            ];
            sessionStorage.setItem('qaList', JSON.stringify(this.messages));
        }
        else {
            this.messages = JSON.parse(sessionStorage.getItem('qaList'));
        }
        if (this.isLogined && this.messages.length <= 1) {
            getCharHistory(sessionStorage.getItem('userId'))
            .then(response => {
                if(response){
                    this.messages = [...this.messages,...response]
                }
            })
        }
    },
}
</script>

<style>
.manager-window-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 85%;
}
.avatar {
    min-width: 35px;
}

.message-content {
  max-width: 100%; /* 限制最大宽度 */
  overflow-wrap: break-word; /* 允许长单词/代码换行 */
}

/* 针对代码块的特殊处理 */
.message-content pre {
  white-space: pre-wrap; 
  max-width: 100%;
  overflow-x: auto; 
  background: #2d2f3b;
  border-radius: 6px;
  padding: 5px;
  color: #e2e2e2;
}



/* 复制按钮 */
.copy-btn {
  background: none;
  border: 1px solid #afb8c1;
  border-radius: 4px;
  padding: 2px 8px;
  font-size: 0.8em;
  cursor: pointer;
  color: #24292f;
  transition: all 0.2s;
}

.copy-btn:hover {
  background: #ffffff80;
}

/* 代码内容 */
.code-block pre {
  margin: 0;
}

/* 高亮样式继承 */
.code-block code.hljs {
  background: transparent;
  padding: 0;
}
</style>