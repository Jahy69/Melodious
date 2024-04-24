<script setup>
	import { useAuth0 } from '@auth0/auth0-vue';

	const { loginWithRedirect, isAuthenticated } = useAuth0();

	const login = () => {
		loginWithRedirect();
	};
</script>

<template>
	<div class="about">
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
			<div class="left">
				<div class="title">Notre histoire</div>
				<div class="text">
					Tout a commencé lors d'une soirée où nous avons eu une idée : et si on pouvait rendre <span>la découverte</span> de la musique <span>aussi excitante que l'écoute</span> elle-même ? <br /><br />
					Imaginez une plateforme où chaque chanson vous <span>apprend</span> quelque chose de nouveau, vous fait <span>ressentir</span> le rythme non seulement dans vos oreilles mais aussi dans votre cœur.
					<span>C’est ça, Melodious.</span> <br /><br />
					Utilisant <span>l'intelligence artificielle</span>, nous personnalisons votre voyage musical pour qu'il soit aussi <span>unique</span> que <span>vos goûts.</span> <br /><br />
					<span>Rejoignez-nous</span> pour redécouvrir votre musique d'une manière que vous n'avez jamais imaginée. Prêts à voir la musique différemment ? <br /><br />
					<span>Avec Melodious, chaque note a une histoire.</span>
				</div>
			</div>
			<div class="right">
				<div class="title">Notre équipe</div>
				<div class="team-container">
					<div class="team">
						<img class="team-img" src="../assets/alexis.png" alt="" />
						<div class="name">Alexis Crocilla</div>
						<div class="job">Chef de projet</div>
					</div>
					<div class="team">
						<img class="team-img" src="../assets/enzo.png" alt="" />
						<div class="name">Enzo Boucherand</div>
						<div class="job">Spécialiste IA</div>
					</div>
					<div class="team">
						<img class="team-img" src="../assets/loic.png" alt="" />
						<div class="name">Loïc Chazeau</div>
						<div class="job">Développeur</div>
					</div>
					<div class="team">
						<img class="team-img" src="../assets/jimmy.png" alt="" />
						<div class="name">Jimmy Cassarino</div>
						<div class="job">UX/UI Designer</div>
					</div>
				</div>
				<div class="image-container">
					<img class="image" src="../assets/about.png" alt="">
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
	.about {
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
		padding: 10px 20px;
		cursor: pointer;
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
	}
	a {
		text-decoration: none;
	}
	.content {
		height: calc(100vh - 100px);
		display: flex;
		justify-content: space-evenly;
	}
	.left {
		width: 42vw;
		height: 100%;
		display: flex;
		flex-direction: column;
		margin-left: 5vw;
	}
	.right {
		width: 42vw;
		height: 100%;
		display: flex;
		flex-direction: column;
	}
	.title {
		font-family: 'Neuropolitical';
		font-style: normal;
		font-weight: 400;
		font-size: 32px;
		line-height: 111.4%;
		color: #d9d9d9;
		margin-bottom: 60px;
		margin-top: 60px;
	}
	.text {
		font-style: normal;
		font-weight: 400;
		font-size: 23px;
		line-height: 111.4%;
		color: #d9d9d9;
		width: 90%;
	}
	span {
		font-weight: 700;
	}
	.team-container {
		display: flex;
	}
	.team {
		margin: 0px 20px;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.team-img {
		height: 100px;
		margin-bottom: 10px;
	}
	.name {
		text-align: center;
		font-style: normal;
		font-weight: 400;
		font-size: 15px;
		line-height: 111.4%;
		color: #ffffff;
		margin: 10px 0px;
	}
	.job {
		text-align: center;
		font-style: normal;
		font-weight: 400;
		font-size: 11px;
		line-height: 111.4%;
		color: #ffffff;
	}
	.image-container {
		height: 60%;
		margin-top: 100px;
		margin-left: 70px;
	}
	.image {
		height: 500px;
	}
</style>
