<template>
  <div class="mobile-home">
    <van-nav-bar title="主页" fixed placeholder/>
    <van-button class="nav-button" round block type="info" @click="navigateToWeather">天气查询</van-button>
    <van-button class="nav-button" round block type="primary" @click="navigateToChat">GPT聊天</van-button>
  </div>
</template>

<script>
export default {
  name:'HomeNavigation',
  methods: {
    navigateToWeather() {
      this.$router.push('/weather');
    },
    navigateToChat() {
      this.$router.push('/gptchatmanager');
    }
  }
}
</script>

<style scoped>
.mobile-home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f0f8ff;
}

.nav-button {
  margin: 15px 0;
  width: 80%;
}

.van-nav-bar {
  background-color: #42b983;
}

.van-nav-bar__title {
  color: white;
}
</style>
