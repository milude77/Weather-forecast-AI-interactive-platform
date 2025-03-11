<template>
  <div id="app" :class="backgroundClass">
    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'App',
  computed: {
    backgroundClass() {
      // 根据当前路由返回对应的背景类名
      switch (this.$route.name) {
        case 'Home':
          return 'home-bg';
        case 'Weather':
          return 'weather-bg';
        case 'GPTChatManager':
          return 'chat-bg';
        case 'Register':
          return 'register-bg';
        default:
          return 'default-bg';
      }
    },
  },
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
  height: 100%;
  font-family: 'Arial', sans-serif;
  transition: background-color 0.5s ease; /* 背景色切换动画 */
}

/* 不同页面的背景色 */
.home-bg {
  background: #e0f7ff; /* 首页背景色 */
}

.weather-bg {
  background:  #fff6bd; /* 天气预报页面背景色 */
}

.chat-bg {
  background: linear-gradient(to bottom, #FFB6C1,#e8cefd); /* AI 聊天页面背景色 */
}

.register-bg{
  background: linear-gradient(to bottom, #FFB6C1,#e8cefd); /* 注册页面背景色 */
}

.default-bg {
  background: #ffffff; /* 默认背景色 */
}

</style>
