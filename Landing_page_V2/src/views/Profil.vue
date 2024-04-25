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
		<div class="content">
			<div class="left">
				<div class="title">Profil</div>
				<div class="profil-card">
					<div class="profil-header">
						<img class="profil-picture" :src="user.picture" alt="" />
						<div class="header-right">
							<div class="profil-name">{{ user.given_name }} {{ user.family_name }}</div>
							<div class="profil-id"><span>ID :</span> GQNUeYQq3nQFbA80U</div>
							<div class="btn-container">
								<div class="logout">
									<p @click="logout" class="text-logout">Logout</p>
									<img style="margin-left: 10px" src="../assets/logout.svg" alt="" />
								</div>
								<img style="margin-left: 15px; cursor: pointer;" class="edit" src="../assets/edit.svg" alt="" />
							</div>
						</div>
					</div>
					<div class="divider"></div>
					<div class="form">
						<div class="line"></div>
					</div>
				</div>
			</div>
			<div class="right">
				<div class="title">Tarifs</div>
				<div class="tarif-card"></div>
				<div class="tarif-card"></div>
				<div class="center">
					<a target="_blank" href="https://melodious-2.notion.site/Mentions-L-gales-57bd0e55c1054bd99cb92d71d4c63dca?pvs=4" class="legal">Consulter les mentions légales</a>
				</div>
			</div>
		</div>
	</div>

	<code>{{ user }}</code>
	<code>{{ user.email }}</code>
</template>

<style scoped>
	.profil {
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
		margin-top: 7vh;
	}
	.left {
		width: 40vw;
		height: 100%;
		margin-left: 100px;
	}
	.right {
		width: 650px;
		height: 100%;
	}
	.title {
		font-family: 'Neuropolitical';
		font-style: normal;
		font-weight: 400;
		font-size: 32px;
		line-height: 111.4%;
		color: #d9d9d9;
		margin-bottom: 40px;
	}
	.profil-card {
		backdrop-filter: blur(100px);
		background: rgba(255, 255, 255, 0.4);
		border-radius: 20px;
		width: 450px;
		height: 630px;
	}
	.profil-header {
		display: flex;
		padding: 25px 0;
	}
	.profil-picture {
		border-radius: 100px;
		height: 97px;
		margin: 0 25px;
	}
	.profil-name {
		font-weight: 600;
		font-size: 20px;
		color: #000000;
	}
	.profil-id {
		font-size: 15px;
		color: #000000;
		margin: 4px 0;
	}
	.btn-container {
		display: flex;
		margin-top: 8px;
		align-items: center;
	}
	.logout {
		display: flex;
		background: #d9d9d9;
		border-radius: 7px;
		flex-direction: row;
		align-items: center;
		padding: 6px 25px;
		cursor: pointer;
	}
	.text-logout {
		font-weight: 600;
		font-size: 13px;
		text-align: center;
		color: #eb473e;
	}

	.divider {
		width: 85%;
		height: 1px;
		background-color: #171717;
		margin: 0 auto;
	}
	.tarif-card {
		backdrop-filter: blur(100px);
		background: rgba(255, 255, 255, 0.4);
		border-radius: 20px;
		width: 650px;
		height: 200px;
		margin-bottom: 25px;
	}
	.center {
		display: flex;
	}
	.legal {
		font-style: normal;
		font-weight: 500;
		font-size: 15px;
		text-decoration-line: underline;
		color: #ffffff;
		margin: 15px auto;
		text-align: center;
	}
	span {
		font-weight: 700;
	}
</style>
