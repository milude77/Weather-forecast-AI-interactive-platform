<template>
    <div class="manager-window">
        <div v-for="(message, index) in messages" :key="index" :class="['message',message.isSender?'sender':'receiver']">
            <div class="avatar" v-if="!message.isSender"><img src="@/assets/img/robot.png" alt="机器人"></div>
            <div class="avatar" v-else><img src="@/assets/img/user.png" alt="uesr"></div>
            <div class="time_content">
                <div class="time">{{ message.time }}</div>
                <div class="message-content">{{ message.text }}</div>
            </div>
        </div>
    </div>
    <div class="send">
          <input v-model="message_sended" type="text" placeholder="请输入消息内容">
          <button @click="sendMessage"><img src="@/assets/img/send.png" alt="发送"></button>
    </div>
</template>

<script>

import "@/assets/managerWindow.css"
import { getGptResponse , getCharHistory} from "@/services/gptResponse.js"


export default {
    name: 'managerWindow',
    data() {
        return {
            user:"",
            message_sended:"",
            messages: []
        }
    },
    props: {
        model:String
    },
    methods: { 
        async sendMessage() {
            if(this.message_sended.trim() === '') return
            try{
                this.messages.push({text:this.message_sended, isSender: true, time: this.getCurrentTime()})
                const response = await getGptResponse(this.user,this.message_sended,this.model)
                this.messages.push({text:response, isSender: false, time: this.getCurrentTime()})
                this.message_sended = ''
                sessionStorage.setItem('qaList', JSON.stringify(this.messages));
            }
            catch(error){
                console.log(error)
            }
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
        saveQA(question,isSender,time){
            const qaList = JSON.parse(sessionStorage.getItem('qaList')) || []
            qaList.push({text:question, isSender: isSender, time: time})
            sessionStorage.setItem('qaList', JSON.stringify(qaList))
        }
    },
    created() {
        if (sessionStorage.getItem('qaList')==null) {
            this.messages = [
                {
                    text: '你好,有什么可以帮助你', isSender: false , time: this.getCurrentTime()
                }
            ];
            sessionStorage.setItem('qaList', JSON.stringify(this.messages));
        }
        else {
            this.messages = JSON.parse(sessionStorage.getItem('qaList'));
        }
    },
}
</script>

<style>
</style>