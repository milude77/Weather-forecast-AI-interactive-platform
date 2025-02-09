<template>
  <div class="home-navigation">
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
</template>

<script>
import '@/assets/home.css';

export default {
  name: 'HomeNavigation'
};
</script>

<style scoped>
</style>