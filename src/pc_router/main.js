import { createApp } from 'vue'
import App from './App.vue'
import router from './index.js'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'


export default function initPcApp(){
createApp(App).use(router).use(ElementPlus).mount('#app')
}