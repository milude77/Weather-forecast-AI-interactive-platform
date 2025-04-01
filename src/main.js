import isMobile from 'is-mobile';
import initPceApp from './pc/main.js';
import initMobileApp from './mobile/main.js';

if (isMobile()) {   
    initMobileApp(); 
} else {
    initPceApp(); 
}