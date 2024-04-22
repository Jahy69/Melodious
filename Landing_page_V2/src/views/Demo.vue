<template>
  <div id="demo" class="demo">
    <div class="header-padding"></div>
    <div class="demo-container">
      <div class="demo-left">
        <div class="chatboxCont">
          <div class="chatboxHeader">
            <img
                class="logoHeader"
                src="../assets/logo.png"
                alt="logo"
            />
            <p class="textHeader">Melodious</p>
          </div>
          <div class="chatbox" id="chatbox">
            <div class="imessage">
              <div
                  :class="[message.author == 'server' ? 'from-them' : 'from-me']"
                  v-for="(message, idx) in chat_box_repertory"
                  :key="idx"
              >
                <div v-if="message.author == server" class="msgLogo"></div>
                <p
                    :class="[
                    message.author == 'server' ? 'from-them' : 'from-me',
                  ]"
                >
                  <span>{{ message.text }}</span>
                </p>
              </div>
            </div>
          </div>
          <div class="spacer">
            <div class="loader"></div>
          </div>
          <div class="inputBox">
            <input
                v-if="!loading"
                class="inputUser"
                type="text"
                @keyup.enter="SendBot(input)"
                v-model="input"
                placeholder="Parle-moi de la funk"
            />
            <input
                v-if="!loading"
                class="send"
                type="button"
                @click="SendBot(input)"
                value
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      chat_history: [],
      chat_box_repertory: [],
      input: "",
      loading: false,
    };
  },
  methods: {
    async SendBot(query) {
      if (!query) return;
      var objDiv = document.getElementById("chatbox");
      this.loading = true;
      this.input = "";
      await this.chat_box_repertory.push({ author: "client", text: query });

      objDiv.scroll(0, objDiv.scrollHeight);

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

      let botResponse;
      await fetch("https://melodious69-8eecb5339a18.herokuapp.com/chat", requestOptions)
          .then((response) => response.text())
          .then((result) => (botResponse = JSON.parse(result)))
          .catch((error) => console.log("error", error));
      console.log(botResponse);
      let answer = botResponse.answer;
      this.chat_history.push([query, answer]);
      await this.chat_box_repertory.push({ author: "server", text: answer });
      objDiv.scroll(0, objDiv.scrollHeight);

      this.loading = false;
    },
  },
};
</script>

<style scoped>
.demo {
  height: 100vh;
  background: white;
}
.header-padding {
  padding-top: 125px;
}
a {
  text-decoration: none !important;
  margin-top: 20%;
  display: flex;
  justify-content: center;
}
.demo-container {
  display: flex;
  height: 70vh;
}
.demo-left {
  margin-left: 10vw;
  width: 50vw;
}
.chatboxCont {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  border-radius: 10px;
  box-shadow: 0px 0px 10px 2px rgba(15, 26, 41, 0.2);
  background-color: white;
}
.chatboxHeader {
  display: flex;
  flex-direction: row;
  height: 80px;
  background-color: #9e81c1;
  border-radius: 10px 10px 0px 0px;
  align-items: center;
}
.logoHeader {
  background: white;
  border-radius: 250px;
  padding: 5px;
  width: 40px;
  height: 40px;
  margin-left: 35px;
}
.textHeader {
  color: white;
  font-size: 1.15rem;
  font-weight: 500;
  margin-left: 20px;
}
.chatbox {
  height: 100%;
  overflow: scroll;
  overflow-x: hidden;
  padding-top: 15px;
}
.imessage {
  border-radius: 0.25rem;
  display: flex;
  flex-direction: column;
  font-size: 0.9rem;
}
.imessage p {
  border-radius: 1.15rem;
  line-height: 1.25;
  max-width: 75%;
  padding: 0.5rem 0.875rem;
  position: relative;
  word-wrap: break-word;
}
.imessage p::before,
.imessage p::after {
  bottom: -0.1rem;
  content: "";
  height: 1rem;
  position: absolute;
}
p.from-me {
  align-self: flex-end;
  background-color: #edeef6;
  color: #0f1a29;
  margin-right: 15px !important;
}
div.from-me {
  align-self: flex-end;
}
p.from-me::before {
  border-bottom-left-radius: 0.8rem 0.7rem;
  border-right: 1rem solid #edeef6;
  right: -0.35rem;
  transform: translate(0, -0.1rem);
}
p.from-me::after {
  background-color: white;
  border-bottom-left-radius: 0.5rem;
  right: -40px;
  transform: translate(-30px, -2px);
  width: 10px;
}
p[class^="from-"] {
  margin: 0.3rem 0;
  width: fit-content;
}
p.from-me ~ p.from-me {
  margin: 0.25rem 0 0;
}
p.from-me ~ p.from-me:not(:last-child) {
  margin: 0.25rem 0 0;
}
p.from-me ~ p.from-me:last-child {
  margin-bottom: 0.5rem;
}
p.from-them {
  align-items: flex-start;
  background-color: #0f1a29;
  color: white;
  margin-left: 45px;
}
p.from-them:before {
  border-bottom-right-radius: 0.8rem 0.7rem;
  border-left: 1rem solid #0f1a29;
  left: -0.35rem;
  transform: translate(0, -0.1rem);
}
p.from-them::after {
  background-color: white;
  border-bottom-right-radius: 0.5rem;
  left: 20px;
  transform: translate(-30px, -2px);
  width: 10px;
}
.chatbox::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
.chatbox::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
}
.chatbox::-webkit-scrollbar-thumb {
  background-color: #cdfb0a;
  border-radius: 10px;
}
.msgLogo {
  width: 25px;
  height: 25px;
  background-size: 100%;
  background-position: center;
  background-repeat: no-repeat;
  margin-top: -20px;
  margin-left: 10px;
}
.inputBox {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 45px;
  margin-bottom: 18px;
}
.inputUser {
  background-color: #edeef6;
  display: flex;
  border-style: none;
  border-radius: 10px;
  font-size: 0.85rem;
  height: 100%;
  width: 100%;
  padding-left: 15px;
  margin-left: 18px;
}
::placeholder {
  color: #0f1a29;
  opacity: 0.5;
  font-size: 0.85rem;
  font-weight: 300;
  vertical-align: middle;
}
input:focus-visible {
  outline-color: #cdfb0a;
}
.send {
  width: 30px;
  height: 30px;
  margin-right: 30px;
  margin-left: 15px;
  background: url("../assets/send.svg");
  background-position: center;
  background-repeat: no-repeat;
  border-style: none;
  cursor: pointer;
}
.wait {
  width: 30px;
  height: 30px;
  margin-right: 30px;
  margin-left: 15px;
  background: url("../assets/send.svg");
  background-position: center;
  background-repeat: no-repeat;
  border-style: none;
  cursor: not-allowed;
}
.spacer {
  height: 30px;
}
.loader,
.loader:before,
.loader:after {
  border-radius: 50%;
  width: 1em;
  height: 1em;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
  -webkit-animation: load7 1.8s infinite ease-in-out;
  animation: load7 1.8s infinite ease-in-out;
}
.loader {
  top: -50px;
  color: #25166b;
  font-size: 10px;
  margin-left: 50px;
  text-indent: -9999em;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
  -webkit-animation-delay: -0.16s;
  animation-delay: -0.16s;
}
.loader:before,
.loader:after {
  content: "";
  position: absolute;
  top: 0px;
}
.loader:before {
  left: -2em;
  -webkit-animation-delay: -0.32s;
  animation-delay: -0.32s;
}
.loader:after {
  left: 2em;
}
</style>
