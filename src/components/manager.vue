<template>
  <custom-dialog v-model="dialogVisible" @close="closeDialog"
      :title="dialogTitle"
      :message="dialogContent"
      :confirmButtonText="dialogConfirmText"
      :confirmAction="logToLogin"
   />
  <div class="container">
    <div class="header">
      <router-link to="/register">
        <button class="login-register-btn">
          去登陆/注册
        </button>
      </router-link>
    </div>
    <div class="gpt-manager">
      <div class="select-mode">
        <button class = "gpt-4o-mode model" @click="changeModelTo4o">
          <p>GPT-4o</p>
        </button>
        <button class = "gpt-3o-mode model" @click="changeModelTo3o">
          <p>GPT-3o</p>
        </button>
      </div>
      <div class="messageBox">
        <div class="messagewindow"> 
          <managerWindow :model = "model"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import '@/assets/manager.css';
import managerWindow from '@/components/managerWindow.vue';
import customDialog from '@/components/customDialog.vue';

export default {
    name: "GPTManager",
    data() {
      return {
        model:"gpt-3.5-turbo",
        dialogVisible: false,
        dialogTitle: "请先登录",
        dialogContent: "4o模型需登陆后使用",
        dialogConfirmText: "去登陆"
      }
    },
    methods: {
        changeModelTo4o() {
          if (sessionStorage.getItem("jwt_key") === null) {
            this.openDialog();
            return;
          }
          this.model = "gpt-4";
        },
        changeModelTo3o() {
          this.model = "GPT-3.5-turbo";
        },
        openDialog() {
          this.dialogVisible = true;
        },
        closeDialog() {
          this.dialogVisible = false;
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