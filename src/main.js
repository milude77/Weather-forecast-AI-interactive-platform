import isMobile from 'is-mobile';
import initPceApp from './pc/main.js';
import initMobileApp from './mobile/main.js';
console.log('是否是移动设备:', isMobile()); 

if (isMobile()) {   
    initMobileApp(); 
} else {
    initPceApp(); 
}