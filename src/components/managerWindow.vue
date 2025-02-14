<template>
    <div class="manager-window">
        <div v-for="(message, index) in messages" :key="index" :class="['message',message.isSender?'sender':'receiver']">
            <div class="avatar" v-if="!message.isSender"><img src="@/assets/img/robot.png" alt="机器人"></div>
            <div class="avatar" v-else><img src="@/assets/img/user.png" alt="uesr"></div>
            <div class="time_content">
                <div class="time">时间</div>
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
                this.messages.push({text: this.message_sended, isSender: true})
                const response = await getGptResponse(this.user,this.message_sended,this.model)
                this.messages.push({text: response, isSender: false})
                this.message_sended = ''
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
    },
    created() {
        this.messages = [
            {
                text: '你好,有什么可以帮助你', isSender: false
            }
        ]
    },
}
</script>

<style>
</style>