<script>
	import { useAuth0 } from '@auth0/auth0-vue';

	export default {
		setup() {
			const { logout, user, isAuthenticated } = useAuth0();

			return {
				logout: () => {
					logout({ logoutParams: { returnTo: window.location.origin } });
				},
				user,
				isAuthenticated,
			};
		},
	};
</script>

<template>
	<div class="profil">
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
	</div>

	<div>
		<pre v-if="isAuthenticated">
        <code>{{ user }}</code>
      </pre>
		<button @click="logout">Log out</button>
	</div>
</template>

<style scoped>
	.profil {
		height: 100vh;
		background-image: url('../assets/background.png');
		background-size: cover;
		background-repeat: no-repeat;
		display: flex;
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
</style>
