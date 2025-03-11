<template>
  <div id="app">
    <!-- 飘雪背景 -->
    <div class="snow"></div>
    <div class="snow"></div>
    <div class="snow"></div>
    <div class="snow"></div>
    <div class="snow"></div>
    <div class="snow"></div>

    <!-- 主内容 -->
    <div class="container">
      <div class="weather_module">
      <router-link to="/weather" >
        <img src="@/assets/img/weather.png" alt="">
      </router-link>
    </div>
    <div class="GPT_module">
      <router-link to="/gptchatmanager" >
        <img src="@/assets/img/gptmanager.png" alt="">
      </router-link>
    </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'HomeNavigation',

};
</script>

<style>
/* 全局样式 */


/* 飘雪效果 */
@keyframes fall {
  0% { top: -10%; }
  100% { top: 95%; }
}

.snow {
  position: absolute;
  top: -10%;
  width: 20px; /* 雪花变大 */
  height: 20px; /* 雪花变大 */
  background-color: white;
  border-radius: 50%;
  filter: blur(2px); /* 模糊效果增强 */
  animation: fall 5s linear infinite; /* 飘落速度变慢 */
}

.snow:nth-child(1) {
  left: 5%;
  animation-delay: 0s;
}

.snow:nth-child(2) {
  left: 20%;
  animation-delay: 2s;
}

.snow:nth-child(3) {
  left: 35%;
  animation-delay: 4s;
}

.snow:nth-child(4) {
  left: 50%;
  animation-delay: 6s;
}

.snow:nth-child(5) {
  left: 65%;
  animation-delay: 8s;
}

.snow:nth-child(6) {
  left: 80%;
  animation-delay: 10s;
}

/* 主容器 */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  gap: 20px;
}
</style>