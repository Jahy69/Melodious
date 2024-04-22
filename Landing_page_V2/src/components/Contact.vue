<script setup>
	import { ref } from "vue";

	import Phone from "../assets/vue/phone.vue";
	import Mail from "../assets/vue/mail.vue";
	import Location from "../assets/vue/location.vue";

	const bg = ref("#ffffff");
	const secondary = ref("#0f1a29");
	const primary = ref("#CDFB0A");
</script>

<template>
	<div class="contact" id="contact">
		<div class="header-padding"></div>
		<div class="contact-container">
			<div class="information">
				<div class="title">Nous contactez</div>
				<div class="subtitle">
					Contactez-nous par email, par téléphone ou remplissez le formulaire pour envoyer un message à notre équipe. Une réponse
					vous sera fournie dans les 48 heures.
				</div>
				<div class="info">
					<div class="line">
						<div class="logo">
							<Phone />
						</div>
						<p class="infoText">04 56 43 32 34</p>
					</div>
					<div class="line">
						<div class="logo">
							<Mail />
						</div>
						<p class="infoText">contact@insightsbot.fr</p>
					</div>
					<div class="line">
						<div class="logo">
							<Location />
						</div>
						<p class="infoText">9 Rue Sainte-Catherine, 69001 Lyon</p>
					</div>
				</div>
			</div>
			<div class="form">
				<div class="formcontainer">
					<div class="title-form">Formulaire de contact</div>
					<p class="formText">Nom</p>
					<input placeholder="Nom" type="text" name id />
					<p class="formText">Email</p>
					<input placeholder="Email@gmail.com" type="text" name id />
					<p class="formText">Téléphone</p>
					<input placeholder="00 00 00 00 00" type="text" name id />
					<p class="formText">Message</p>
					<textarea placeholder="Message" type="textarea" rows="5" name id />
					<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank"><div class="btn-form">Envoyer</div></a>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
	.contact {
		height: 100vh;
	}
	.header-padding {
		padding-top: 65px;
	}
	.contact-container {
		display: flex;
		justify-content: space-around;
		align-items: center;
		height: calc(100% - 80px);
	}
	.information {
		width: 40vw;
	}
	.title {
		font-size: 3.2rem;
		font-weight: 500;
		line-height: 1.3;
	}
	.subtitle {
		font-size: 1.1rem;
		padding-top: 4vh;
		line-height: 1.3;
	}
	.info {
		padding-top: 3vh;
	}
	.line {
		display: flex;
		align-items: center;
		padding-top: 6vh;
	}
	.logo {
		padding-left: 2vw;
		width: 20px;
		height: 20px;
	}
	.infoText {
		font-size: 1.1rem;
		padding-left: 2vw;
		line-height: 1.3;
	}
	.form {
		display: flex;
		flex-direction: column;
		width: 27vw;
		border-radius: 15px;
		box-shadow: 0px 0px 15px 7px rgba(15, 26, 41, 0.2);
		background-color: #edeef6;
	}
	.formcontainer {
		display: flex;
		height: 100%;
		flex-direction: column;
		padding: 10px 30px;
	}
	.title-form {
		width: 100%;
		text-align: center;
		font-size: 1.2rem;
		font-weight: 600;
		padding-top: 2vh;
		line-height: 1.3;
		padding-bottom: 2vh;
	}
	.formText {
		font-size: 0.9rem;
		padding-top: 1vh;
		padding-bottom: 1vh;
		line-height: 1.3;
	}
	input {
		height: 35px;
		border-radius: 7px;
		border: 1px solid #c5c7cc;
		margin-bottom: 1vw;
		padding-left: 15px;
		font-size: 1.1rem;
		background-color: #f9f9fb !important;
	}
	::placeholder {
		color: #98969f;
		font-size: 0.75rem;
		font-family: "Montserrat", sans-serif;
	}
	input:focus-visible {
		outline-color: v-bind(primary);
	}
	textarea {
		border-radius: 7px;
		border: 1px solid #c5c7cc;
		margin-bottom: 12%;
		resize: none;
		padding-left: 15px;
		padding-top: 10px;
		font-size: 1.1em;
	}
	textarea:focus-visible {
		outline-color: v-bind(primary);
	}
	.btn-form {
		font-size: 0.9rem;
		width: 175px;
		padding: 10px 10px;
		display: flex;
		justify-content: center;
		align-items: center;
		color: v-bind(secondary);
		background-color: v-bind(primary);
		margin: 0px auto;
		border-radius: 10px;
		margin-bottom: 15px;
	}
	.btn-form:hover {
		font-weight: 700;
		opacity: 0.9;
	}
	a {
		display: flex;
		align-items: center;
		text-decoration: none !important;
	}
</style>
