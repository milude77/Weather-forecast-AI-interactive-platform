<template>
  <div class="mobile-container">
    <div class="mobile-header">
      <button class="header-return" @click="returnToHome">
        <img src="@/assets/img/house.png" alt="返回" style="width: 24px; height: 24px;">
      </button> 
      <div class="header-login" v-if="!isLogin">
        <router-link to="/register" style="float: right;">
          <button class="mobile-btn">
            登录/注册
          </button>
        </router-link>
      </div>
      <div class="header-menu" v-else>
        <div class="mobile-welcome">
          欢迎，{{ username }}
        </div>
      </div>
    </div>
    <div class="menu" style="float: right;">
      <img src="@/assets/img/menu.png" alt="菜单" @click="showModelSelect">
    </div>
    <div class="mobile-gpt-manager">
      <div class="mobile-messageBox" style="height: 75%;">
        <managerWindow ref="messageWindow" :model="model" :isLogined="isLogin"/>
      </div>
    </div>

    <custom-dialog class="mobile-dialog" v-model="logindialogVisible" @close="closeDialog('login')"
      :title="dialogTitle"
      :message="dialogContent"
      :confirmButtonText="dialogConfirmText"
      :confirmAction="logToLogin"
    />
    <custom-dialog class="mobile-dialog"  v-if="isLogin" v-model="deldialogVisible" @close="closeDialog('del')" @cancel="triggerMessageDeletion()" @confirm="historyMessageDeletion()"
      :title="'删除数据'"
      :message="'将清除所有聊天记录！'"
      :cancelButtonText="'删除本地数据'"
      :confirmButtonText="'删除云端数据'"
    />
    <custom-dialog class="mobile-dialog"  v-else v-model="deldialogVisible" @close="closeDialog('del')" @confirm="triggerMessageDeletion()"
      :title="'删除数据'"
      :message="'将清除所有聊天记录！'"
      :confirmButtonText="'删除'"
    />
  </div>
</template>

<script>

import managerWindow from '@/mobilecomponents/managerWindow.vue';
import customDialog from '@/mobilecomponents/customDialog.vue';
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
        username: sessionStorage.getItem('username') || '',
        showModelSelect: false,
        modelOptions: [
        { text: 'GPT-4', value: 'gpt-4' },
        { text: 'GPT-3.5', value: 'gpt-3.5-turbo' }
      ]
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
        },
        returnToHome() {
          this.$router.push("/");
        }
    },
  components: {
    managerWindow,
    customDialog
  }
}
</script>

<style>
.mobile-container {
  width: 100%;
  height: 100vh;
  box-sizing: border-box;
  flex-direction: column;
  align-items: center;
}

.mobile-header {
  top: 0;
  height: 10%;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-login {
  width: 100%;
  text-align: center;
}

.mobile-welcome {
  font-size: 18px;
  color: #333;
}

.mobile-gpt-manager {
  height: 85%;
  width: 100%;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.mobile-select-mode {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.mobile-messageBox {
  bottom: 0;
  width: 100%;
  flex: 1;
}

.mobile-btn {
  padding: 8px 16px;
  font-size: 16px;
  color: white;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.mobile-dialog{
  position: fixed;
  top: 0;
  left: 12.5%;
  width: 75%;
  height: 20%;
}
.header-return {
  border: 0;
  background-color: transparent;
}

</style>