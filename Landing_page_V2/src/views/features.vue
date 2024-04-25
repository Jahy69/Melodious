<script setup>
	import { useAuth0 } from '@auth0/auth0-vue';

	const { loginWithRedirect, isAuthenticated } = useAuth0();

	const login = () => {
		loginWithRedirect();
	};
</script>

<template>
	<div class="features">
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
			<div class="title">Les fonctionnalités essentielles de Melodious</div>
			<div class="row">
				<div class="card">
					<img class="icon" src="../assets/feature1.svg" alt="" />
					<div class="text-container">
						<div class="card-title">Votre assistant musical qui apprend avec vous</div>
						<div class="text">
							Notre chatbot utilise l'apprentissage adaptatif pour affiner ses recommandations et réponses en fonction de vos interactions passées. Plus vous l'utilisez, plus il devient précis, vous offrant une
							expérience véritablement personnalisée et évolutive.
						</div>
					</div>
				</div>
				<div class="card">
					<img class="icon" src="../assets/feature2.svg" alt="" />
					<div class="text-container">
						<div class="card-title">Comprenez l'art derrière la musique</div>
						<div class="text">
							Apprenez comment vos morceaux préférés sont construits avec des explications détaillées sur les techniques musicales utilisées. De la théorie musicale à la pratique, enrichissez votre appréciation
							de la musique.
						</div>
					</div>
				</div>
				<div class="card">
					<img class="icon" src="../assets/feature3.svg" alt="" />
					<div class="text-container">
						<div class="card-title">Élargissez vos horizons musicaux</div>
						<div class="text">
							Grâce à notre technologie avancée, découvrez des genres musicaux qui complètent vos goûts actuels. Plongez dans des styles similaires et laissez vous surprendre par la richesse de la musique qui
							vous était jusqu'alors inconnue.
						</div>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="card">
					<img class="icon" src="../assets/feature4.svg" alt="" />
					<div class="text-container">
						<div class="card-title">Explorez un monde de musique sur mesure</div>
						<div class="text">
							Naviguez à travers un univers musical personnalisé qui apprend de vos goûts pour vous recommander des artistes et des chansons alignés avec vos préférences personnelles. Découvrez des nouveautés
							et redécouvrez des classiques.
						</div>
					</div>
				</div>
				<div class="card">
					<img class="icon" src="../assets/feature5.svg" alt="" />
					<div class="text-container">
						<div class="card-title">Voyagez à travers l'histoire de la musique</div>
						<div class="text">
							Chaque morceau a une histoire. Découvrez les contextes historiques, les anecdotes et les inspirations derrière vos chansons et genres préférés, enrichissant ainsi votre expérience d'écoute.
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
	.features {
		height: 100vh;
		background-image: url('../assets/background.png');
		background-size: cover;
		background-repeat: no-repeat;
		display: flex;
		flex-direction: column;
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
	.content {
		height: calc(100vh - 100px);
	}
	.title {
		font-family: 'Neuropolitical';
		font-style: normal;
		font-weight: 400;
		font-size: 36px;
		line-height: 111.4%;
		text-align: center;
		color: #bdbcbc;
		margin-top: 7vh;
		margin-bottom: 10vh;
	}
	.row {
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.card {
		height: 150px;
		width: 430px;
		margin: 40px 15px;
		background: rgba(201, 191, 182, 0.5);
		border: 1px solid #bdbcbc;
		backdrop-filter: blur(100px);
		border-radius: 10px;
		display: flex;
		align-items: start;
	}
	.icon {
		width: 28px;
		margin-left: 20px;
		margin-top: 15px;
	}

	.text-container {
		display: flex;
		flex-direction: column;
		margin-top: 15px;
		margin-left: 15px;
	}
	.card-title {
		font-style: normal;
		font-weight: 700;
		font-size: 13.5px;
		color: #000000;
	}
	.text {
		margin-top: 7px;
		margin-right: 25px;
		font-weight: 500;
		font-size: 12px;
		line-height: 17px;
		color: #000000;
	}
	a {
		text-decoration: none;
	}
	.router-link-exact-active {
		border-bottom: 2px solid #bdbcbc;
	}
</style>
