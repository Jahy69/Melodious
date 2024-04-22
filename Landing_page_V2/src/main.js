import { createApp } from 'vue'
import { createAuth0 } from '@auth0/auth0-vue';
import './style.css'
import App from './App.vue'
import router from './router';

const app = createApp(App);
  
  app.use(
    createAuth0({
      domain: "dev-95jqxbmj.eu.auth0.com",
      clientId: "X4FCB6U9Inz5bJ8LcxXOJmpO93cniDqh",
      authorizationParams: {
        redirect_uri: window.location.origin
      }
    })
  );

  app.use(router)
  
  app.mount('#app');