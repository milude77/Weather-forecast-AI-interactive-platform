import { isMobile } from 'vue-device-detector';
import initPceApp from './pc/main.js';
import initMobileApp from './mobile/main.js';

console.log('是否是移动设备:', isMobile); // 打印设备检测结果

if (isMobile) {
    initMobileApp(); // 加载移动端代码
} else {
    initPceApp(); // 加载 PC 端代码
}