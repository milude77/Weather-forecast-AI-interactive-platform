<template>
    <div class="auth-container">
      <div class="auth-box">
        <!-- 登录表单 -->
        <div v-if="isLoginForm">
          <h2 class="auth-title">登录</h2>
          <form class="auth-form" @submit.prevent="handleLogin">
            <div class="mb-4">
              <label class="block text-sm font-medium mb-2" for="login-email">邮箱</label>
              <input
                v-model="loginEmail"
                type="email"
                id="login-email"
                class="auth-input"
                placeholder="请输入邮箱"
                required
              />
            </div>
            <div class="mb-6">
              <label class="block text-sm font-medium mb-2" for="login-password">密码</label>
              <input
                v-model="loginPassword"
                type="password"
                id="login-password"
                class="auth-input"
                placeholder="请输入密码"
                required
              />
            </div>
            <button type="submit" class="auth-button">登录</button>
          </form>
          <p class="auth-link">
            没有账号？
            <a href="#" @click.prevent="toggleForm">注册</a>
          </p>
        </div>
  
        <!-- 注册表单 -->
        <div v-else>
          <h2 class="auth-title">注册</h2>
          <form class="auth-form" @submit.prevent="handleRegister">
            <div class="mb-4">
              <label class="block text-sm font-medium mb-2" for="register-username">用户名</label>
              <input
                v-model="registerUsername"
                type="text"
                id="register-username"
                class="auth-input"
                placeholder="请输入用户名"
                required
              />
            </div>
            <div class="mb-4">
              <label class="block text-sm font-medium mb-2" for="register-email">邮箱</label>
              <input
                v-model="registerEmail"
                type="email"
                id="register-email"
                class="auth-input"
                placeholder="请输入邮箱"
                required
              />
            </div>
            <div class="mb-6">
              <label class="block text-sm font-medium mb-2" for="register-password">密码</label>
              <input
                v-model="registerPassword"
                type="password"
                id="register-password"
                class="auth-input"
                placeholder="请输入密码"
                required
              />
            </div>
            <button type="submit" class="auth-button">注册</button>
          </form>
          <p class="auth-link">
            已有账号？
            <a href="#" @click.prevent="toggleForm">登录</a>
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <script>

  import "@/assets/resign.css"
  import { registerUser, loginUser } from "@/services/regist_login.js"

  export default {
    name: 'LoginResign',
    data() {
      return {
        isLoginForm: true, // 控制显示登录还是注册表单
        loginEmail: '',
        loginPassword: '',
        registerUsername: '',
        registerEmail: '',
        registerPassword: '',
      };
    },
    methods: {
      toggleForm() {
        this.isLoginForm = !this.isLoginForm;
      },
      handleLogin() {
        // 处理登录逻辑
        loginUser(this.loginEmail, this.loginPassword)
        .then((message) => {
           alert(message.message);
           localStorage.setItem('jwt_key',message.token);
           this.$router.push("/gptchatmanager");
         })
        .catch((error) => {
           console.error(error);
           alert('登录失败，用户名或密码错误');
        });
      },
      handleRegister() {
        // 处理注册逻辑
        registerUser(this.registerUsername, this.registerEmail, this.registerPassword)
        .then((message) => {
           alert(message.message);
         })
        .catch((error) => {
           console.error(error);
           alert('注册失败！');
          });
      },
    },
  };
  </script>
  
  <style scoped>
  /* 自定义样式 */
  </style>