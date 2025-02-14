<template>
  <div class="container">
    <div class="header">
      <router-link to="#">
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
        <button class = "gpt-3o-mode model" @click="changeModelTo4o">
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
import managerWindow from './managerWindow.vue';

export default {
    name: "GPTManager",
    data() {
      return {
        model:"gpt-3.5-turbo",
      }
    },
    methods: {
        changeModelTo4o() {
          this.model = "GPT-4omini";
        },
        changeModelTo3o() {
          this.model = "GPT-3.5-turbo";
        }
    },
  components: {
    managerWindow
  }
}
</script>

<style>
</style>