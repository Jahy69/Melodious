<script setup>
	import { ref } from "vue";

	import Facebook from "../assets/vue/facebook.vue";
	import Twitter from "../assets/vue/twitter.vue";
	import Instagram from "../assets/vue/instagram.vue";
	import Linkedin from "../assets/vue/linkedin.vue";

	const bg = ref("#ffffff");
	const secondary = ref("#0f1a29");
	const primary = ref("#CDFB0A");
</script>

<template>
	<div class="footer">
		<div class="logo">
			<a href="#header" style="padding: 10px 20px">
				<img class="logo-img" src="../assets/footerlogo.svg" alt="logo" />
				<p class="logo-text">Insights Bot</p>
			</a>
		</div>
		<div class="subtitle">
			"Explorez le monde des statistiques sportives avec Insights Bot"
		</div>
		<div class="navigation">
			<a href="#header">
			<div class="tab">Accueil</div>
		</a>
		<a href="#features">
			<div class="tab">Fonctionnalités</div>
		</a>
			<a href="#demo">
			<div class="tab">Démo</div>
		</a>
			<a href="#price">
			<div class="tab">Prix</div>
		</a>
			<a href="#contact">
			<div class="tab">Contact</div>
		</a>
		</div>
		<div class="reseaux">
			<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">
				<div class="logo1">
					<Facebook />
				</div>
			</a>
			<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">
				<div class="logo1">
					<Twitter />
				</div>
			</a>
			<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">
				<div class="logo1">
					<Instagram />
				</div>
			</a>
			<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">
				<div class="logo1">
					<Linkedin />
				</div>
			</a>
		</div>
		<div class="border"></div>
		<div class="bottom">
			<div class="right">© 2024 Insights Bot, Tous droits réservés</div>
			<div class="term-container">
				<div class="term">Mentions légales</div>
				<div class="cookie">Cookies</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
	.footer {
		background-color: v-bind(secondary);
	}
	a {
		display: flex;
		align-items: center;
		text-decoration: none !important;
	}
	.logo {
		display: flex;
		justify-content: center;
		align-items: center;
		padding-top: 2.5%;
	}

	.logo-img {
		width: 35px;
		height: 35px;
		margin-right: 10px;
	}

	.logo-text {
		color: v-bind(bg);
		font-size: 1.1rem;
		font-weight: 600;
	}
	.subtitle {
		padding-top: 1.2%;
		margin: auto;
		text-align: center;
		width: 40vw;
		font-size: 0.9rem;
		font-weight: 300;
		opacity: 0.8;
		line-height: 1;
		color: v-bind(bg)
	}
	.navigation {
		display: flex;
		justify-content: center;
		padding-top: 1.8%;
	}
	.tab {
		color: v-bind(bg);
		padding: 15px 25px;
		font-size: 0.9rem;
		font-weight: 500;
	}
	.reseaux {
		display: flex;
		align-items: center;
		justify-content: center;
		padding-top: 1.8%;
	}
	.logo1 {
		margin: 0px 20px;
		width: 25px;
		height: 25px;
		border-radius: 100px;
		padding: 12px;
		cursor: pointer;
		transition: 0.5s all ease-in-out;
	}
	.logo1:hover {
		background-color: v-bind(primary);
		border-radius: 100px;
		padding: 12px;
		transform: translateY(0px) scale(1.1);
	}
	.border {
		margin: auto;
		margin-top: 3%;
		height: 1px;
		width: 90vw;
		background-color: v-bind(bg);
		opacity: 0.6;
	}
	.bottom {
		display: flex;
		justify-content: space-between;
		padding-top: 25px;
		padding-bottom: 1.7%;
	}
	.right {
		color: v-bind(bg);
		padding-left: 5vw;
		font-size: 0.95rem;
		font-weight: 400;
		line-height: 1;
	}
	.term-container {
		display: flex;
		color: v-bind(bg);
		padding-right: 5vw;
	}
	.term {
		font-size: 0.95rem;
		font-weight: 400;
		line-height: 1;
		padding-right: 50px;
	}
	.cookie {
		font-size: 0.95rem;
		font-weight: 400;
		line-height: 1;
	}
</style>
