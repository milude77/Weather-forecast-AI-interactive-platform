import { createApp } from 'vue'
import App from './App.vue'
import router from './index.js'
import ElementPlus from 'element-plus'
import Vant from 'vant'
import 'vant/lib/index.css'
import 'element-plus/dist/index.css'

export default function initMobileApp(){
    createApp(App).use(Vant).use(router).use(ElementPlus).mount('#app')
}