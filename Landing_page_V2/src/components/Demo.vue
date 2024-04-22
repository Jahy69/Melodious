<script setup>
	import { ref } from "vue";

	const bg = ref("#ffffff");
	const secondary = ref("#0f1a29");
	const primary = ref("#CDFB0A");
	
	const chat_history = ref([])
	const chat_box_repertory = ref([])
	const input = ref("")
	const loading = ref(false)
	
	async function SendBot(query){
		if (!query)
		return
		var objDiv = document.getElementById("chatbox");
		loading.value = true
		input.value = ""
		// ptit await pour attendre qu'il ai biens envoyé affiché le message pour alligner le scroll dessus 
		await chat_box_repertory.value.push({author:'client',text:query})

		objDiv.scroll(0,objDiv.scrollHeight)

		var myHeaders = new Headers();
		myHeaders.append("Content-Type", "application/json");
		
		var raw = JSON.stringify({
			"query": query,
			"chat_history": chat_history.value
		});
	
		var requestOptions = {
			method: 'POST',
			headers: myHeaders,
			body: raw,
			redirect: 'follow'
		};

		let botResponse
		await fetch("http://127.0.0.1:5000/chatbot", requestOptions)
			.then(response =>response.text())
			.then(result => botResponse = JSON.parse(result))
			.catch(error => console.log('error', error));


		let answer = botResponse.response.answer
		chat_history.value.push([query, answer])
		await chat_box_repertory.value.push({author:'server',text:answer})
		// ptit await pour attendre qu'il ai biens envoyé affiché le message pour alligner le scroll dessus et enlever le load
		objDiv.scroll(0,objDiv.scrollHeight)

		loading.value = false

		
	}
</script>

<template>
	<div class="demo" id="demo">
		<div class="header-padding"></div>
		<div class="demo-container">
			<div class="demo-left">
				<div class="chatboxCont">
					<div class="chatboxHeader">
						<img class="logoHeader" src="../assets/logo.png" alt="logo" />
						<p class="textHeader">L1Bot</p>
					</div>
					<div class="chatbox" id="chatbox" ref="chatbox">
						<div class="imessage">
							<div :class="[message.author == 'server' ? 'from-them' : 'from-me']"
							v-for="(message,idx) in chat_box_repertory" v-bind:key="idx"
							>
								<div v-if="message.author == server" class="msgLogo"></div>
								<p :class="[message.author == 'server' ? 'from-them' : 'from-me']">
									<span>{{message.text}}</span>
								</p>
								
							</div>
						</div>
					</div>
					<div class="spacer">
						<div class="loader"></div>
					</div>
					<div class="inputBox">
						<input v-if="!loading" class="inputUser" type="text" v-on:keyup.enter="SendBot(input)" v-model="input" placeholder="Combien de buts a marqués Mbappé en 2018-2019" />
						<input  v-if="!loading" class='send' type="button"  v-on:click="SendBot(input)" value />
					</div>
				</div>
			</div>
			<div class="demo-right">
				<div class="title">Démo de notre L1Bot</div>
				<div class="subtitle">Essayer gratuitement notre L1Bot et découvrez les statistique de la ligue 1</div>
				<div class="subtitle">
					Soyez aux premières loges des performances des équipes, explorez les données en profondeur, et faites l'expérience d'une
					immersion totale dans le monde captivant des statistiques sportives
				</div>
				<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank"><div class="btn">Découvrez tous nos Bots</div></a>
			</div>
		</div>
	</div>
</template>

<style scoped>
	.demo {
		height: 100vh;
		background: linear-gradient(315deg, rgba(255, 255, 255, 1) 20%, rgba(205, 250, 12, 0.4907388126148897) 100%);
	}
	.header-padding {
		padding-top: 65px;
	}
	a {
		text-decoration: none !important;
		margin-top: 20%;
		display: flex;
		justify-content: center;
	}
	.demo-container {
		display: flex;
		justify-content: space-around;
		align-items: center;
		height: calc(100% - 80px);
	}
	.demo-left {
		width: 50vw;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: auto;
		margin-top: 70px;
	}
	.chatboxCont {
		display: flex;
		flex-direction: column;
		width: 65%;
		border-radius: 10px;
		box-shadow: 0px 0px 10px 2px rgba(15, 26, 41, 0.2);
		background-color: v-bind(bg);
	}
	.chatboxHeader {
		display: flex;
		flex-direction: row;
		height: 60px;
		background-color: v-bind(primary);
		border-radius: 10px 10px 0px 0px;
		align-items: center;
	}
	.logoHeader {
		width: 40px;
		height: 40px;
		margin-left: 35px;
	}
	.textHeader {
		color: v-bind(secondary);
		font-size: 1.15rem;
		font-weight: 500;
		margin-left: 20px;
	}
	.chatbox {
		height: 380px;
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
		color: v-bind(secondary);
		margin-right: 15px !important;
	}
	div.from-me {
		align-self: flex-end;
		display: contents;
	}
	p.from-me::before {
		border-bottom-left-radius: 0.8rem 0.7rem;
		border-right: 1rem solid #edeef6;
		right: -0.35rem;
		transform: translate(0, -0.1rem);
	}
	p.from-me::after {
		background-color: v-bind(bg);
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
		background-color: v-bind(secondary);
		color: v-bind(bg);
		margin-left: 20px;
	}
	p.from-them:before {
		border-bottom-right-radius: 0.8rem 0.7rem;
		border-left: 1rem solid v-bind(secondary);
		left: -0.35rem;
		transform: translate(0, -0.1rem);
	}
	p.from-them::after {
		background-color: v-bind(bg);
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
		background-color: v-bind(primary);
		border-radius: 10px;
	}
	.msgLogo {
		width: 25px;
		height: 25px;
		background: url("../assets/logo.svg");
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
		color: v-bind(secondary);
		opacity: 0.5;
		font-size: 0.85rem;
		font-weight: 300;
		vertical-align: middle;
	}
	input:focus-visible {
		outline-color: v-bind(primary);
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
		cursor:not-allowed;
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

	.demo-right {
		width: 40vw;
		height: 70%;
		padding-right: 7vw;
		display: flex;
		flex-direction: column;
	}
	.title {
		font-size: 2.8rem;
		font-weight: 500;
		line-height: 1.3;
	}
	.subtitle {
		font-size: 1.1rem;
		padding-top: 5vh;
		line-height: 1.3;
	}
	.btn {
		font-size: 0.9rem;
		width: 210px;
		padding: 10px 10px;
		display: flex;
		justify-content: center;
		align-items: center;
		color: v-bind(bg);
		background-color: v-bind(secondary);
		border-radius: 10px;
	}
	.btn:hover {
		font-weight: 700;
		opacity: 0.9;
	}
</style>
