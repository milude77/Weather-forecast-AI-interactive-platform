<template>
  <custom-dialog v-model="logindialogVisible" @close="closeDialog('login')"
      :title="dialogTitle"
      :message="dialogContent"
      :confirmButtonText="dialogConfirmText"
      :confirmAction="logToLogin"
   />
   <custom-dialog v-if="isLogin" v-model="deldialogVisible" @close="closeDialog('del')" @cancel="triggerMessageDeletion()" @confirm="historyMessageDeletion()"
      :title="'删除数据'"
      :message="'将清除所有聊天记录！'"
      :cancelButtonText="'删除本地数据'"
      :confirmButtonText="'删除云端数据'"
   />
   <custom-dialog v-else v-model="deldialogVisible" @close="closeDialog('del')" @confirm="triggerMessageDeletion()"
      :title="'删除数据'"
      :message="'将清除所有聊天记录！'"
      :confirmButtonText="'删除'"
   />
  <div class="container">
    <div class="header" v-if="!isLogin">
      <router-link to="/register">
        <button class="login-register-btn">
          去登陆/注册
        </button>
      </router-link>
    </div>
    <div class="header" v-else>
      <div class="welcome-message">
        欢迎，{{this.username}}
      </div>
    </div>
    <div class="gpt-manager">
      <div class="select-mode">
        <button :class = "['gpt-4o-mode', 'model', {'selected': this.model === 'gpt-4'}]" @click="changeModelTo4o">
          <p>GPT-4o</p>
        </button>
        <button :class = "['gpt-3.5-turbo', 'model', {'selected': this.model === 'gpt-3.5-turbo'}]" @click="changeModelTo3o">
          <p>GPT-3.5</p>
        </button>
        <button :class="['model','clearbtn']" @click="openDialog('del')">
          <img src="@/assets/img/huishouzhan.png" alt="回收">
        </button>
      </div>
      <div class="messageBox">
        <div class="messagewindow"> 
          <managerWindow ref="messageWindow" :model = "model" :isLogined="isLogin"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import '@/assets/manager.css';
import managerWindow from '@/components/managerWindow.vue';
import customDialog from '@/components/customDialog.vue';
import {delMessages} from "@/services/gptResponse.js"

export default {
    name: "GPTManager",
    data() {
      return {
        model:"gpt-3.5-turbo",
        deldialogVisible: false,
        logindialogVisible: false,
        dialogTitle: "请先登录",
        dialogContent: "4o模型需登陆后使用",
        dialogConfirmText: "去登陆",
        isLogin: sessionStorage.getItem('isLogin') === 'true' || false,
        username: sessionStorage.getItem('username') || ''
      }
    },
    methods: {
        changeModelTo4o() {
          if (sessionStorage.getItem("jwt_key") === null) {
            this.openDialog('login');
            return;
          }
          this.model = "gpt-4";
        },
        changeModelTo3o() {
          this.model = "gpt-3.5-turbo";
        },
        triggerMessageDeletion() {
          this.$refs.messageWindow.deleteMessage();
        },
        historyMessageDeletion() {
          delMessages(sessionStorage.getItem("userId"))
          .then((message) => {
            alert(message);
          })
          this.$refs.messageWindow.deleteMessage();
        },
        openDialog(dialogType) {
          if (dialogType === 'login') {
            this.logindialogVisible = true;
          } else if (dialogType === 'del') {
            this.deldialogVisible = true;
          }
        },
        closeDialog(dialogType) {
          if (dialogType === 'login') {
            this.logindialogVisible = false;
          } else if (dialogType === 'del') {
            this.deldialogVisible = false;
          }
        },
        logToLogin(){
          this.$router.push("/register");
        }
    },
  components: {
    managerWindow,
    customDialog
  }
}
</script>

<style>
</style>