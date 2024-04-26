<script setup>
	import { useAuth0 } from '@auth0/auth0-vue';

	const { loginWithRedirect, isAuthenticated } = useAuth0();

	const login = () => {
		loginWithRedirect();
	};
</script>

<template>
	<div class="home">
		<div class="right-title">
			<div class="logo">
				<img src="../assets/logo.svg" alt="" />
			</div>
			<div class="title">Melodious</div>
		</div>
		<div class="col">
			<div class="navbar">
				<RouterLink class="nav-btn" to="/">Accueil</RouterLink>
				<RouterLink class="nav-btn" to="/fonctionnalites">Fonctionnalités</RouterLink>
				<div v-if="!isAuthenticated" class="nav-btn" @click="login">Demo</div>
				<RouterLink v-if="isAuthenticated" class="nav-btn" to="/demo">Demo</RouterLink>
				<RouterLink class="nav-btn" to="/a-propos">À propos</RouterLink>
				<div v-if="!isAuthenticated" class="login" @click="login">Connexion</div>
				<RouterLink v-if="isAuthenticated" class="login" to="/profil">Profil</RouterLink>
			</div>
			<div class="row">
				<div class="image-container">
					<img class="image" src="../assets/home.png" alt="" />
				</div>
				<div class="content">
					<div class="text-container">
						<div class="text">AI Powered Music</div>
						<div class="cta">
							<router-link class="cta-text" to="/fonctionnalites">Explorer</router-link>
							<img class="cta-icone" src="../assets/explore.svg" alt="" />
						</div>
					</div>
					<div class="social">
						<div class="divider"></div>
						<a target="_blank" href="">
							<img class="icone" src="../assets/twitter.svg" alt="" />
						</a>
						<a target="_blank" href="">
							<img class="icone" src="../assets/linkedin.svg" alt="" />
						</a>
						<a target="_blank" href="">
							<img class="icone" src="../assets/facebook.svg" alt="" />
						</a>
						<a target="_blank" href="https://www.instagram.com/melodious_fr/">
							<img class="icone" src="../assets/instagram.svg" alt="" />
						</a>
						<div class="divider"></div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
	.home {
		height: 100vh;
		background-image: url('../assets/background.png');
		background-size: cover;
		background-repeat: no-repeat;
		display: flex;
	}
	.right-title {
		height: 100%;
		width: 10vw;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.logo {
		width: 90px;
		margin-top: 35px;
	}
	.title {
		margin-top: 30px;
		color: #bdbcbc;
		font-size: 5.5rem;
		writing-mode: vertical-rl;
		text-orientation: mixed;
		font-family: 'neuropolitical', sans-serif;
	}
	.col {
		display: flex;
		flex-direction: column;
		width: 90vw;
	}
	.row {
		display: flex;
		flex-direction: row;
		height: calc(100vh - 100px);
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
	.image-container {
		width: 50%;
		height: 100%;
	}
	.image {
		position: absolute;
		height: 97vh;
		margin-left: 30px;
		top: 40px;
	}
	.content {
		width: 40%;
		height: 100%;
	}
	.text-container {
		height: 82%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.text {
		font-family: 'Neuropolitical';
		font-style: normal;
		font-weight: 400;
		font-size: 63px;
		line-height: 111.4%;
		text-align: center;
		width: 80%;
		-webkit-text-stroke: 1px #bdbcbc;
		color: transparent;
	}
	.cta {
		margin-top: 25px;
		display: flex;
		font-weight: 700;
		padding: 5px 10px;
		color: #171717;
		width: 140px;
		align-items: center;
		margin-right: 35px;
		margin-left: 45px;
		cursor: pointer;
		background: linear-gradient(90deg, #998675 0%, #c7b299 100%);
		border: 1px solid #bdbcbc;
		border-radius: 15px;
	}
	.cta-text {
		color: #171717;
		margin-right: 20px;
		margin-left: 20px;
	}
	.cta-icone {
		height: 30px;
	}
	.social {
		display: flex;
		justify-content: center;
		align-items: center;
		margin-top: 35px;
	}
	.divider {
		height: 1px;
		width: 100px;
		background-color: #bdbcbc;
		margin: 0 15px;
	}
	.icone {
		height: 25px;
		margin: 10px;
	}
	a {
		text-decoration: none;
	}
	.router-link-exact-active {
		border-bottom: 2px solid #bdbcbc;
	}
</style>
