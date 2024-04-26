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
								<img style="margin-left: 15px; cursor: pointer" class="edit" src="../assets/edit.svg" alt="" />
							</div>
						</div>
					</div>
					<div class="divider"></div>
					<div class="form">
						<div class="line">
							<div class="input-container">
								<div class="input-title">Nom</div>
								<input class="input" type="text" id="name" :value="user.family_name" />
							</div>
							<div class="input-container">
								<div class="input-title">Prénom</div>
								<input class="input" type="text" id="prenom" :value="user.given_name" />
							</div>
						</div>
						<div class="line">
							<div class="input-container">
								<div class="input-title">Email</div>
								<input class="input full" type="text" id="prenom" :value="user.email" />
							</div>
						</div>
						<div class="line">
							<div class="input-container">
								<div class="input-title">Téléphone</div>
								<input class="input full" type="text" id="prenom" value="07 89 88 45 66" />
							</div>
						</div>
						<div class="line">
							<div class="input-container">
								<div class="input-title">Adresse</div>
								<input style="width: 220px" class="input" type="text" id="prenom" value="9 Rue Sainte-Catherine" />
							</div>
							<div class="input-container">
								<div class="input-title">Code postal</div>
								<input style="width: 120px" class="input" type="text" id="prenom" value="69001" />
							</div>
						</div>
						<div class="data-container">
							<input class="checkbox" type="checkbox" id="data" name="data" checked />
							<label for="data" class="checkbox-label"></label>
							<p class="data">J'accepte que mes données personnelles soient utilisées</p>
						</div>
					</div>
					<div class="bottom">
						<div class="dl-btn">Télécharger mes données</div>
						<div class="delete-btn">Supprimer mes données</div>
					</div>
				</div>
			</div>
			<div class="right">
				<div class="title">Tarifs</div>
				<div class="tarif-card">
					<div class="tarif-left">
						<div class="tarif-title">Basique</div>
						<div class="tarif">0€ <span class="month">/ mois</span></div>
						<div class="tarif-text">Profitez d'une introduction gratuite à la découverte musicale enrichie par l'intelligence artificielle sans aucun coût.</div>
						<div class="tarif-btn1">OFFRE EN COURS</div>
					</div>
					<div class="tarif-right">
						<div class="features">Fonctionnalités</div>
						<div class="row">
							<img class="coche" src="../assets/check.svg" alt="" />
							<div class="features-text">Accès à Melodious</div>
						</div>
						<div class="row">
							<img class="coche" src="../assets/check.svg" alt="" />
							<div class="features-text">7 Questions par semaine</div>
						</div>
						<div class="row">
							<img class="coche" src="../assets/check.svg" alt="" />
							<div class="features-text">Découvertes quotidiennes</div>
						</div>
					</div>
				</div>
				<div class="tarif-card">
					<div class="tarif-left">
						<div class="tarif-title">Premium</div>
						<div class="tarif">5€ <span class="month">/ mois</span></div>
						<div class="tarif-text">Profitez d'un accès complet et illimité à toutes nos ressources, avec des fonctionnalités avancées pour une immersion totale.</div>
						<div class="tarif-btn2">Essayer</div>
					</div>
					<div class="tarif-right">
						<div class="features">Fonctionnalités</div>
						<div class="row">
							<img class="coche" src="../assets/check.svg" alt="" />
							<div class="features-text">Fonctionnalités basique</div>
						</div>
						<div class="row">
							<img class="coche" src="../assets/check.svg" alt="" />
							<div class="features-text">Accès illimité</div>
						</div>
						<div class="row">
							<img class="coche" src="../assets/check.svg" alt="" />
							<div class="features-text">Playlists personnalisées</div>
						</div>
						<div class="row">
							<img class="coche" src="../assets/check.svg" alt="" />
							<div class="features-text">Anecdotes et histoires</div>
						</div>
						<div class="row">
							<img class="coche" src="../assets/check.svg" alt="" />
							<div class="features-text">Support prioritaire</div>
						</div>
					</div>
				</div>
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
		text-decoration: none;
	}
	.content {
		height: calc(100vh - 100px);
		display: flex;
		margin-top: 4vh;
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
		margin-bottom: 20px;
	}
	.profil-card {
		backdrop-filter: blur(100px);
		background: rgba(255, 255, 255, 0.4);
		border-radius: 20px;
		width: 450px;
	}
	.profil-header {
		display: flex;
		padding: 15px 0;
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
		margin-bottom: 10px;
	}
	.tarif-card {
		backdrop-filter: blur(100px);
		background: rgba(255, 255, 255, 0.4);
		border-radius: 20px;
		height: 200px;
		margin-bottom: 25px;
		display: flex;
	}
	.tarif-left {
		width: 365px;
		height: 100%;
		margin-left: 25px;
		padding-top: 12px;
	}
	.tarif-title {
		font-family: 'Neuropolitical';
		font-weight: 400;
		font-size: 16px;
		color: #000000;
	}
	.tarif {
		font-weight: 500;
		font-size: 34px;
		color: #000000;
		margin-top: 5px;
		margin-bottom: 5px;
	}
	.month {
		font-weight: 500;
		font-size: 12px;
		color: #000000;
	}
	.tarif-text {
		font-weight: 600;
		font-size: 11px;
		color: #000000;
		margin-bottom: 15px;
	}
	.tarif-btn1 {
		background: rgba(217, 217, 217, 0.5);
		border: 1px solid #000000;
		border-radius: 20px;
		padding: 9px 13px;
		font-weight: 600;
		font-size: 12px;
		color: #000000;
		width: 130px;
		text-align: center;
		cursor: pointer;
	}
	.tarif-btn2 {
		border: 1px solid #000000;
		border-radius: 20px;
		padding: 9px 13px;
		font-weight: 600;
		font-size: 12px;
		color: #000000;
		width: 70px;
		text-align: center;
		cursor: pointer;
	}
	.tarif-right {
		height: 100%;
		padding-top: 12px;
		margin-left: 25px;
	}
	.features {
		font-weight: 600;
		font-size: 13px;
		color: #000000;
		margin-bottom: 10px;
	}
	.row {
		display: flex;
		margin-bottom: 5px;
	}
	.features-text {
		font-weight: 500;
		font-size: 12px;
		color: #000000;
		margin-left: 5px;
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
	.line {
		display: flex;
		justify-content: center;
		margin-bottom: 6px;
	}
	.input-container {
		margin: 0px 10px;
	}
	.input-title {
		font-weight: 600;
		font-size: 14px;
		color: #000000;
		margin-bottom: 3px;
	}
	.input {
		background: #d9d9d9;
		opacity: 0.6;
		border-radius: 5px;
		font-size: 15px;
		color: #000000;
		border: none;
		padding-left: 10px !important;
		padding: 4px 0px;
		width: 170px;
	}
	.full {
		width: 370px;
	}
	.data {
		font-weight: 400;
		font-size: 12px;
		color: #000000;
		margin-left: 10px;
		display: flex;
		align-items: center;
	}
	.data-container {
		display: flex;
		margin-top: 15px;
		margin-left: 33px;
	}
	.checkbox {
		display: none;
	}
	.checkbox-label {
		cursor: pointer;
		width: 17px;
		height: 17px;
		display: inline-block;
		background-color: #d9d9d9;
		border-radius: 3px;
		border: 3px solid transparent;
	}
	.checkbox:checked + .checkbox-label {
		background-color: #998675;
		border-radius: 3px;
		width: 17px;
		height: 17px;
		border-color: #d9d9d9;
	}
	.bottom {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-top: 30px;
		padding-bottom: 25px;
	}
	.dl-btn {
		border-radius: 7px;
		padding: 7px 30px;
		font-weight: 600;
		background: #d9d9d9;
		font-size: 13px;
		text-align: center;
		color: #0b0b0b;
		cursor: pointer;
	}
	.delete-btn {
		margin-top: 15px;
		border-radius: 7px;
		padding: 7px 30px;
		font-weight: 600;
		background: #f3afaf;
		font-size: 13px;
		text-align: center;
		color: #0b0b0b;
		cursor: pointer;
	}
	.router-link-exact-active {
		border-bottom: 2px solid #bdbcbc;
	}
</style>
