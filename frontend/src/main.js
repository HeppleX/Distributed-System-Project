import { createApp } from 'vue';
import Antd from 'ant-design-vue';
import App from './App';
import router from './router'
import store from './store'
import 'ant-design-vue/dist/reset.css';

createApp(App).use(store).use(router).use(Antd).mount('#app')
