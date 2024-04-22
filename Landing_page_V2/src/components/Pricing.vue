<script setup>
	import { ref } from "vue";

	const bg = ref("#ffffff");
	const secondary = ref("#0f1a29");
	const primary = ref("#CDFB0A");
</script>

<template>
	<div class="pricing" id="price">
		<div class="header-padding"></div>
		<div class="title">Nos offres d'abonnement adaptées à vous</div>
		<div class="pricing-container">
			<div class="pricing-row">
				<div class="card">
					<div class="card-row1">
						<div class="card-title">Essentiel</div>
					</div>
					<div class="card-row2">
						<div class="card-price">
							9,99€/mois
						</div>
					</div>
					<div class="card-row3">
						<div class="card-features">
							<img class="card-img" src="../assets/feature.svg" alt="features">
							<div class="card-text">Accès à une ligue sportive de votre choix</div>
						</div>
						<div class="card-features">
							<img class="card-img" src="../assets/feature.svg" alt="features">
							<div class="card-text">Mises à jour en temps réel</div>
						</div>
						<div class="card-features">
							<img class="card-img" src="../assets/feature.svg" alt="features">
							<div class="card-text">Personnalisation des alertes</div>
						</div>
					</div>
					<div class="card-row4">
						<div class="card-btn">Choisir cet abonnement</div>
					</div>
				</div>
				<div class="card">
					<div class="card-row1">
						<div class="card-title">Premium</div>
					</div>
					<div class="card-row2">
						<div class="card-price">
							19,99€/mois
						</div>
					</div>
					<div class="card-row3">
						<div class="card-features">
							<img class="card-img" src="../assets/feature.svg" alt="features">
							<div class="card-text">Accès illimité à toutes les ligues et sports</div>
						</div>
						<div class="card-features">
							<img class="card-img" src="../assets/feature.svg" alt="features">
							<div class="card-text">Analyse approfondie des statistiques</div>
						</div>
						<div class="card-features">
							<img class="card-img" src="../assets/feature.svg" alt="features">
							<div class="card-text">Notifications personnalisées</div>
						</div>
					</div>
					<div class="card-row4">
						<div class="card-btn">Choisir cet abonnement</div>
					</div>
				</div>
				<div class="card">
					<div class="card-row1">
						<div class="card-title">Pro</div>
					</div>
					<div class="card-row2">
						<div class="card-price">
							29,99€/mois
						</div>
					</div>
					<div class="card-row3">
						<div class="card-features">
							<img class="card-img" src="../assets/feature.svg" alt="features">
							<div class="card-text">Fonctionnalités de l'abonnement Premium</div>
						</div>
						<div class="card-features">
							<img class="card-img" src="../assets/feature.svg" alt="features">
							<div class="card-text">Rapports statistiques personnalisés</div>
						</div>
						<div class="card-features">
							<img class="card-img" src="../assets/feature.svg" alt="features">
							<div class="card-text">Assistance prioritaire 24/7</div>
						</div>
					</div>
					<div class="card-row4">
						<div class="card-btn">Choisir cet abonnement</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
	.pricing {
		height: 100vh;
		background: linear-gradient(225deg, rgba(255, 255, 255, 1) 20%, rgba(205, 250, 12, 0.4907388126148897) 100%);
	}
	.header-padding {
		padding-top: 65px;
	}
	.title {
		font-size: 1.8rem;
		font-weight: 500;
		line-height: 1.3;
		text-align: center;
		padding-top: 7vh;
		padding-bottom: 2vh;
	}
	.pricing-container {
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.pricing-row {
		width: 80vw;
		display: flex;
		margin-top: 10vh;
		justify-content: center;
	}
	.card {
		width: 100%;
		height: 400px;
		background-color: v-bind(bg);
		margin: 0px 45px;
		border-radius: 10px;
		transition: 0.4s all ease-in-out;
		box-shadow: 0px 0px 10px 2px rgba(15, 26, 41, 0.2);
	}
	.card:hover {
		transform: translateY(0px) scale(1.05);
	}
	.card-row1 {
		display: flex;
		align-items: center;
		justify-content: center;
		padding-top: 9%;
	}
	.card-title {
		font-size: 1.5rem;
		font-weight: 600;
	}
	.card-row2 {
		display: flex;
	}
	.card-price {
		font-size: 1.3rem;
		font-weight: 400;
		padding-top: 7%;
		margin: auto;
	}
	.card-row3 {
		display: flex;
		flex-direction: column;
		justify-content: center;
		padding-left: 20px;
		height: 180px;
	}
	.card-features {
		display: flex;
		align-items: center;
		padding-top: 20px;
	}
	.card-img {
		height: 20px;
	}
	.card-text {
		padding-left: 15px;
		font-size: 0.8rem;
		font-weight: 400;
		padding-right: 20px;
	}
	.card-row4 {
		display: flex;
		justify-content: center;
		align-items: end;
		height: 20%;
	}
	.card-btn {
		font-size: 0.9rem;
		width: 200px;
		padding: 10px 10px;
		display: flex;
		justify-content: center;
		align-items: center;
		color: v-bind(secondary);
		background-color: v-bind(primary);
		border-radius: 10px;
		cursor: pointer;
	}
	.card-btn:hover {
		font-weight: 700;
		opacity: 0.9;
	}
</style>
