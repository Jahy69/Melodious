<script>
// Import useAuth0 from @auth0/auth0-vue
import { useAuth0 } from "@auth0/auth0-vue";

export default {
  // Setup function to initialize the component
  setup() {
    // Destructure loginWithRedirect and isAuthenticated from useAuth0
    const { loginWithRedirect, isAuthenticated } = useAuth0();

    // Return an object containing login function and isAuthenticated flag
    return {
      // Login function to redirect user to Auth0 login page
      login: () => {
        loginWithRedirect();
      },
      // isAuthenticated flag to check if the user is authenticated
      isAuthenticated,
    };
  },
  // Data function to initialize component data
  data() {
    // Return an object containing chat_history, chat_box_repertory, input, and loading
    return {
      // Array to store chat history
      chat_history: [],
      // Array to store chat box repertory
      chat_box_repertory: [],
      // Input value for user message
      input: "",
      // Loading flag to show loading state
      loading: false,
    };
  },
  // Methods object containing SendBot function
  methods: {
    // Async function to send message to bot and receive response
    async SendBot(query) {
      // Check if query is not empty
      if (!query) return;
      // Get chatbox element
      var objDiv = document.getElementById("chatbox");
      // Set loading flag to true
      this.loading = true;
      // Clear input value
      this.input = "";
      // Push user message to chat_box_repertory
      await this.chat_box_repertory.push({ author: "client", text: query });

      // Scroll to bottom of chatbox
      objDiv.scroll(0, objDiv.scrollHeight);

      // Initialize headers and request options
      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");

      var raw = JSON.stringify({
        query: query,
      });

      var requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow",
      };

      // Initialize botResponse variable
      let botResponse;
      // Fetch response from bot API
      await fetch(
        "https://melodious69-8eecb5339a18.herokuapp.com/chat",
        requestOptions
      )
        // Parse response as text
       .then((response) => response.text())
        // Parse response as JSON and assign to botResponse variable
       .then((result) => (botResponse = JSON.parse(result)))
        // Log error if any
       .catch((error) => console.log("error", error));
      // Log botResponse
      console.log(botResponse);
      // Get answer from botResponse
      let answer = botResponse.answer;
      // Push user message and bot response to chat_history
      this.chat_history.push([query, answer]);
      // Push bot response to chat_box_repertory
      await this.chat_box_repertory.push({ author: "server", text: answer });
      // Scroll to bottom of chatbox
      objDiv.scroll(0, objDiv.scrollHeight);

      // Set loading flag to false
      this.loading = false;
    },
  },
};
</script>

<template>
  <!-- Demo component -->
  <div class="demo">
    <!-- Header component -->
    <div class="header">
      <!-- Logo component -->
      <div class="logo">
        <img style="width: 65px" src="../assets/logo.svg" alt="" />
      </div>
      <!-- Navbar component -->
      <div class="navbar">
        <!-- Navigation links -->
        <RouterLink class="nav-btn" to="/">Accueil</RouterLink>
        <RouterLink class="nav-btn" to="/fonctionnalites"
          >Fonctionnalités</RouterLink
        >
        <!-- Demo button for unauthenticated users -->
        <div v-if="!isAuthenticated" class="nav-btn" @click="login">Demo</div>
        <!-- Demo link for authenticated users -->
        <RouterLink v-if="isAuthenticated" class="nav-btn" to="/demo"
          >Demo</RouterLink
        >
        <RouterLink class="nav-btn" to="/a-propos">À propos</RouterLink>
        <!-- Login button for unauthenticated users -->
        <div v-if="!isAuthenticated" class="login" @click="login">
          Connexion
        </div>
        <!-- Profile link for authenticated users -->
        <RouterLink v-if="isAuthenticated" class="login" to="/profil"
          >Profil</RouterLink
        >
      </div>
    </div>

    <!-- Content component -->
    <div class="content">
      <!-- Demo-left component -->
<div class="demo-left">
        <!-- Chatbox component -->
        <div class="chatbox" id="chatbox">
          <!-- Chatbox repertory component -->
          <div class="chatbox-repertory" v-for="(item, index) in chat_box_repertory" :key="index">
            <!-- Chatbox repertory message component -->
            <div class="chatbox-repertory-message" v-if="item.author === 'client'">
              <!-- User message component -->
              <div class="user-message">
                <p>{{ item.text }}</p>
              </div>
            </div>
            <!-- Chatbox repertory message component -->
            <div class="chatbox-repertory-message" v-else>
              <!-- Bot message component -->
              <div class="bot-message">
                <p>{{ item.text }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Input component -->
        <div class="input">
          <!-- Input field component -->
          <input
            type="text"
            placeholder="Type your message here..."
            v-model="input"
            @keyup.enter="SendBot(input)"
          />
          <!-- Send button component -->
          <button @click="SendBot(input)">Send</button>
        </div>
      </div>

      <!-- Demo-right component -->
      <div class="demo-right">
        <!-- Title component -->
        <div class="title">
          <h1>Découvrez notre solution</h1>
        </div>
        <!-- Description component -->
        <div class="description">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit
            tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.
          </p>
        </div>
        <!-- Image component -->
        <div class="image">
          <img src="../assets/demo.svg" alt="" />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Global styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Inter", sans-serif;
  background-color: #f5f5f5;
}

a {
  text-decoration: none;
  color: #000;
}

button {
  cursor: pointer;
  background-color: #000;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  margin-left: 10px;
}

button:hover {
  background-color: #333;
}

/* Demo component styles */
.demo {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;
}

.logo {
  display: flex;
  align-items: center;
  justify-content: center;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-btn {
  padding: 10px 20px;
  margin-right: 10px;
  border-radius: 5px;
  background-color: #fff;
  box-shadow: 0px 2px 5pxrgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.nav-btn:hover {
  background-color: #f5f5f5;
}

.login {
  padding: 10px 20px;
  border-radius: 5px;
  background-color: #000;
  color: #fff;
  transition: all 0.3s ease;
}

.login:hover {
  background-color: #333;
}

.content {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  padding-top: 100px;
  gap: 50px;
}

.demo-left {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 50%;
  height: 100%;
}

.chatbox {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  width: 100%;
  height: 70%;
  background-color: #fff;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  padding: 20px;
  overflow-y: scroll;
}

.chatbox-repertory {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  width: 100%;
  margin-bottom: 20px;
}

.chatbox-repertory-message {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  margin-bottom: 10px;
}

.user-message {
  display: flex;
  align-items: center;
  justify-content: center;
  width: fit-content;
  background-color: #000;
  color: #fff;
  padding: 10px 20px;
  border-radius: 10px;
  margin-right: 20px;
}

.bot-message {
  display: flex;
  align-items: center;
  justify-content: center;
  width: fit-content;
  background-color: #f5f5f5;
  padding: 10px 20px;
  border-radius: 10px;
  margin-left: 20px;
}

.input {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 10%;
  background-color: #fff;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  padding: 20px;
  gap: 10px;
}

.input input {
  width: 80%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.demo-right {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 50%;
  height: 100%;
}

.title {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 20%;
}

.description {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 40%;
}

.description p {
  text-align: center;
  font-size: 20px;line-height: 1.5;
}

.image {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 40%;
}

.image img {
  width: 80%;
  height: 80%;
  object-fit: contain;
}
</style>