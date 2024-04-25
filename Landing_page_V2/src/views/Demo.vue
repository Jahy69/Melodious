<script>
	import { useAuth0 } from '@auth0/auth0-vue';

	export default {
		setup() {
			const { loginWithRedirect, isAuthenticated } = useAuth0();

			return {
				login: () => {
					loginWithRedirect();
				},
				isAuthenticated,
			};
		},
		data() {
			return {
				chat_history: [],
				chat_box_repertory: [],
				input: '',
				loading: false,
			};
		},
		methods: {
			async SendBot(query) {
				if (!query) return;
				var objDiv = document.getElementById('chatbox');
				this.loading = true;
				this.input = '';
				await this.chat_box_repertory.push({ author: 'client', text: query });

				objDiv.scroll(0, objDiv.scrollHeight);

				var myHeaders = new Headers();
				myHeaders.append('Content-Type', 'application/json');

				var raw = JSON.stringify({
					query: query,
				});

				var requestOptions = {
					method: 'POST',
					headers: myHeaders,
					body: raw,
					redirect: 'follow',
				};

				let botResponse;
				await fetch('https://melodious69-8eecb5339a18.herokuapp.com/chat', requestOptions)
					.then((response) => response.text())
					.then((result) => (botResponse = JSON.parse(result)))
					.catch((error) => console.log('error', error));
				console.log(botResponse);
				let answer = botResponse.answer;
				this.chat_history.push([query, answer]);
				await this.chat_box_repertory.push({ author: 'server', text: answer });
				objDiv.scroll(0, objDiv.scrollHeight);

				this.loading = false;
			},
		},
	};
</script>

<template>
	<div class="demo">
		<div class="header">
			<div class="logo">
				<img style="width: 65px" src="../assets/logo.svg" alt="" />
			</div>
			<div class="navbar">
				<RouterLink class="nav-btn" to="/">Accueil</RouterLink>
				<RouterLink class="nav-btn" to="/fonctionnalites">Fonctionnalités</RouterLink>
				<div v-if="!isAuthenticated" class="nav-btn" @click="login">Demo</div>
				<RouterLink v-if="isAuthenticated" class="nav-btn" to="/demo">Demo</RouterLink>
				<RouterLink class="nav-btn" to="/a-propos">À propos</RouterLink>
				<div v-if="!isAuthenticated" class="login" @click="login">Connexion</div>
				<RouterLink v-if="isAuthenticated" class="login" to="/profil">Profil</RouterLink>
			</div>
		</div>

		<div class="content">
			<div class="demo-left">
				<div class="chatboxCont">
					<div class="chatboxHeader">
						<img class="logoHeader" src="../assets/logo.svg" alt="logo" />
						<p class="textHeader">Melodious</p>
					</div>
					<div class="chatbox" id="chatbox">
						<div class="imessage">
							<div :class="[message.author == 'server' ? 'from-them' : 'from-me']" v-for="(message, idx) in chat_box_repertory" :key="idx">
								<div v-if="message.author == server" class="msgLogo"></div>
								<p :class="[message.author == 'server' ? 'from-them' : 'from-me']">
									<span>{{ message.text }}</span>
								</p>
							</div>
						</div>
					</div>
					<div class="inputBox">
						<input v-if="!loading" class="inputUser" type="text" @keyup.enter="SendBot(input)" v-model="input" placeholder="Parle-moi de la funk" />
						<input v-if="!loading" class="send" type="button" @click="SendBot(input)" value />
					</div>
				</div>
			</div>
			<div class="demo-right">
				<div class="title">ESSAYEZ GRATUITEMENT <span style="font-family: 'Neuropolitical'">Melodious</span></div>
				<div class="text">
					Notre chatbot intelligent utilise l'intelligence artificielle pour enrichir votre expérience musicale de manière interactive et éducative. Voici ce que vous pouvez faire avec Melodious : <br /><br />•
					Explorer des genres musicaux : De la pop au baroque, découvrez les subtilités et les histoires derrière divers genres musicaux.<br /><br />
					• Découvrir des artistes et des chansons : Trouvez de nouveaux favoris avec des recommandations personnalisées basées sur vos goûts.<br /><br />
					• Apprendre des techniques musicales : Obtenez des explications sur les techniques utilisées dans vos morceaux préférés.<br /><br />
					• Écouter des anecdotes musicales : Plongez dans l'histoire et les origines des chansons et des mouvements musicaux.<br /><br />
					Tapez simplement votre question ou votre intérêt et laissez vous guider par l'expertise de notre AI.
				</div>
				<RouterLink class="btn" to="/profil">Mettre à niveau</RouterLink>
			</div>
		</div>
	</div>
</template>

<style scoped>
	.demo {
		height: 100vh;
		background-image: url('../assets/background.png');
		background-size: cover;
		background-repeat: no-repeat;
		display: flex;
		flex-direction: column;
	}
	.content {
		height: calc(100vh - 100px);
		display: flex;
		justify-content: space-around;
		margin-top: 7vh;
	}
	.header {
		height: 100px;
		width: 100%;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.logo {
		margin-left: 50px;
		margin-top: 5px;
	}
	.navbar {
		z-index: 1000;
		height: 100px;
		width: 100%;
		display: flex;
		justify-content: flex-end;
		align-items: center;
	}
	.nav-btn {
		font-family: 'neuropolitical', sans-serif;
		font-size: 0.85rem;
		color: #bdbcbc;
		padding: 3px 0px;
		margin: 7px 20px;
		cursor: pointer;
		border-bottom: 2px solid transparent;
	}
	.login {
		font-family: 'neuropolitical', sans-serif;
		background-color: #9c8978;
		padding: 5px 10px;
		color: #171717;
		border-radius: 100px;
		width: 120px;
		display: flex;
		justify-content: center;
		margin-right: 35px;
		margin-left: 45px;
		cursor: pointer;
		border-bottom: 0px solid transparent !important;
	}
	a {
		text-decoration: none !important;
		display: flex;
		justify-content: center;
	}
	.demo-left {
		width: 50vw;
		height: 680px;
	}
	.demo-right {
		width: 37vw;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.chatboxCont {
		display: flex;
		flex-direction: column;
		height: 100%;
		width: 100%;
		border-radius: 10px;
		box-shadow: 0px 0px 10px 2px rgba(15, 26, 41, 0.2);
		background: rgba(255, 255, 255, 0.4);
	}
	.chatboxHeader {
		display: flex;
		flex-direction: row;
		height: 80px;
		background-color: #c6c6c6;
		border-radius: 10px 10px 0px 0px;
		align-items: center;
	}
	.logoHeader {
		width: 40px;
		height: 40px;
		margin-left: 25px;
		margin-right: 20px;
	}
	.textHeader {
		font-family: 'Neuropolitical';
		font-style: normal;
		font-weight: 400;
		font-size: 30px;
		line-height: 36px;
		color: #3f3b36;
	}
	.chatbox {
		height: 100%;
		overflow: scroll;
		overflow-x: hidden;
		padding-top: 15px;
		padding-bottom: 25px;
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
		content: '';
		height: 1rem;
		position: absolute;
	}
	p.from-me {
		align-self: flex-end;
		background-color: #c69c6d;
		color: #0f1a29;
		margin-right: 15px !important;
	}
	div.from-me {
		align-self: flex-end;
	}
	p.from-me::before {
		border-bottom-left-radius: 0.8rem 0.7rem;
		border-right: 1rem solid #c69c6d;
		right: -0.35rem;
		transform: translate(0, -0.1rem);
	}
	p.from-me::after {
		background: #8c8987;
		border-bottom-left-radius: 0.5rem;
		right: -40px;
		transform: translate(-30px, -2px);
		width: 10px;
	}
	p[class^='from-'] {
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
		background-color: #edeef6;
		color: #0f1a29;
		margin-left: 45px;
	}
	p.from-them:before {
		border-bottom-right-radius: 0.8rem 0.7rem;
		border-left: 1rem solid #edeef6;
		left: -0.35rem;
		transform: translate(0, -0.1rem);
	}
	p.from-them::after {
		background-color: #b8b1a9;
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
		border-radius: 10px;
	}
	.chatbox::-webkit-scrollbar-thumb {
		background-color: #9c8978;
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
		background-color: transparent;
		display: flex;
		font-size: 0.85rem;
		height: 100%;
		width: 100%;
		padding-left: 15px;
		margin-left: 18px;
		border: 1px solid #d9d9d9;
		border-radius: 8px;
	}
	::placeholder {
		color: #3f3b36;
		font-size: 0.85rem;
		font-weight: 300;
		vertical-align: middle;
	}
	input:focus-visible {
		outline-color: #c69c6d;
	}
	.send {
		width: 30px;
		height: 30px;
		margin-right: 30px;
		margin-left: 15px;
		background: url('../assets/send.svg');
		background-position: center;
		background-repeat: no-repeat;
		border-style: none;
		cursor: pointer;
	}
	.btn {
		margin-top: 25px;
		display: flex;
		font-weight: 700;
		justify-content: center;
		padding: 5px 10px;
		color: #171717;
		width: 180px;
		align-items: center;
		margin-right: 35px;
		margin-left: 45px;
		cursor: pointer;
		background: linear-gradient(90deg, #998675 0%, #c7b299 100%);
		border: 1px solid #bdbcbc;
		border-radius: 15px;
	}
	.title {
		margin-top: 20px;
		width: 350px;
		font-weight: 400;
		font-size: 25px;
		line-height: 30px;
		color: #c6c6c6;
		text-align: center;
	}
	.text {
		margin-top: 20px;
		font-style: normal;
		font-weight: 400;
		font-size: 16px;
		line-height: 24px;
		display: flex;
		align-items: center;
		color: #c6c6c6;
	}
	.router-link-exact-active {
		border-bottom: 2px solid #bdbcbc;
	}
</style>
