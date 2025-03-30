<template>
    <div class="manager-window-container" >
        <div class="manager-window" ref="chatWindow" >
            <div v-for="(message, index) in messages" :key="index" :class="['message',message.is_sender?'sender':'receiver']">
                <div class="avatar" v-if="!message.is_sender"><img src="@/assets/img/robot.png" alt="机器人"></div>
                <div class="avatar" v-else><img src="@/assets/img/user.png" alt="uesr"></div>
                <div class="time_content">
                    <div class="time">{{ message.timestamp }}</div>
                    <div class="message-content">{{ message.message }}</div>
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
        }
    },
    created() {
        if (sessionStorage.getItem('qaList')==null) {
            this.messages = [
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: true , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
                {
                    message: '你好,有什么可以帮助你', is_sender: false , timestamp: this.getCurrentTime()
                },
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
</style>