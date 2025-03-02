import { createRouter, createWebHistory } from 'vue-router';
import HomeNavigation from '@/components/home.vue';
import WeatherForecast from '@/components/weather.vue';
import GPTManager from '@/components/manager.vue';
import LoginResign from '@/components/login_resign.vue';


const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeNavigation
  },
  {
    path: '/weather',
    name: 'Weather',
    component: WeatherForecast
  },
  {
    path: '/gptchatmanager',
    name: 'GPTChatManager',
    component: GPTManager 
  },
  {
    path: '/register',
    name: 'Register',
    component: LoginResign
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});



export default router;
