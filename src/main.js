import isMobile from 'is-mobile';
import initPceApp from './pc_router/main.js';
import initMobileApp from './mobile_router/main.js';

if (isMobile()) {   
    initMobileApp(); 
} else {
    initPceApp(); 
}