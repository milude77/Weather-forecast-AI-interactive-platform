import { createRouter, createWebHistory } from 'vue-router';
import HomeNavigation from '@/components/home.vue';
import WeatherForecast from '@/components/weather.vue';
import GPTManager from '@/components/manager.vue';


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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  switch (to.name) {
    case 'Home':
      document.body.style.backgroundColor = '';  // Home 页面背景色
      break;
    case 'Weather':
      document.body.style.background = '#fff9e6';  // Weather 页面背景色
      break;
    case 'GPTChatManager':
      document.body.style.background = 'linear-gradient(to bottom, #FFB6C1,#e8cefd)';  // GPTChatManager 页面背景色
      break;
  }
  next();
});

export default router;
