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
				<img src="../assets/logo.svg" alt="">
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
					<img class="image" src="../assets/home.png" alt="">
				</div>
				<div class="content">
					<div class="text-container">
						<div class="text">AI Powered Music</div>
						<div class="cta">
							<p class="cta-text">Explorer</p>
							<img class="cta-icone" src="../assets/explore.svg" alt="">
						</div>
					</div>
					<div class="social">
						<div class="divider"></div>
						<img class="icone" src="../assets/twitter.svg" alt="">
						<img class="icone" src="../assets/linkedin.svg" alt="">
						<img class="icone" src="../assets/facebook.svg" alt="">
						<img class="icone" src="../assets/instagram.svg" alt="">
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
		color: #BDBCBC;
    font-size: 7rem;
    writing-mode: vertical-rl;
    text-orientation: mixed;
    font-family: "neuropolitical", sans-serif;
	}
	.col {
		display: flex;
		flex-direction: column;
		width: 90vw;
	}
	.row {
		display: flex;
		flex-direction: row;
		height: 100%;
	}
	.navbar {
		height: 100px;
		width: 100%;
		display: flex;
		justify-content: flex-end;
		align-items: center;
	}
	.nav-btn {
		font-family: "neuropolitical", sans-serif;
		font-size: 0.85rem;
		color: #BDBCBC;
		padding: 10px 20px;
		cursor: pointer;
	}
	.login {
		font-family: "neuropolitical", sans-serif;
		background-color: #9C8978;
		padding: 5px 10px;
		color : #171717;
		border-radius: 100px;
		width: 120px;
		display: flex;
		justify-content: center;
		margin-right: 35px;
		margin-left: 45px;
		cursor: pointer;
	}
	.image-container {
		width: 60%;
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
		-webkit-text-stroke: 1px #BDBCBC;
		color: transparent;

	}
	.cta {
		margin-top: 25px;
		display: flex;
		font-weight: 700;
		padding: 5px 10px;
		color : #171717;
		width: 140px;
		align-items: center;
		margin-right: 35px;
		margin-left: 45px;
		cursor: pointer;
		background: linear-gradient(90deg, #998675 0%, #C7B299 100%);
		border: 1px solid #BDBCBC;
		border-radius: 15px;
	}
	.cta-text {
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
		margin-top: 18%;
	}
	.divider {
		height: 1px;
		width: 100px;
		background-color: #BDBCBC;
		margin: 0 15px;
	}
	.icone {
		height: 25px;
		margin: 10px;
	}
	a {
		text-decoration: none;
	}
</style>