<script setup>
	import { ref } from "vue";

	const bg = ref("#ffffff");
	const secondary = ref("#0f1a29");
	const primary = ref("#CDFB0A");
</script>

<template>
	<div class="features" id="features">
		<div class="header-padding"></div>
		<div class="title">Les fonctionnalités essentielles de nos Bots</div>
		<div class="features-container">
			<div class="features-row">
				<div class="card">
					<div class="card-row1">
						<img class="card-icon" src="../assets/card1.svg" alt="card1" />
						<div class="card-title">Polyvalence sportive</div>
					</div>
					<div class="card-row2">
						<div class="card-subtitle">
							S'adapte à n'importe quel sport, ligue ou compétition, offrant une couverture complète.
						</div>
					</div>
					<div class="card-row3">
						<div class="more">En apprendre plus</div>
						<img class="arrow" src="../assets/arrow.svg" alt="arrow" />
					</div>
				</div>
				<div class="card">
					<div class="card-row1">
						<img class="card-icon" src="../assets/card2.svg" alt="card2" />
						<div class="card-title">Analyse en temps réel</div>
					</div>
					<div class="card-row2">
						<div class="card-subtitle">
							Fournit des statistiques pour une compréhension en temps réel des performances sportives.
						</div>
					</div>
					<div class="card-row3">
						<div class="more">En apprendre plus</div>
						<img class="arrow" src="../assets/arrow.svg" alt="arrow" />
					</div>
				</div>
				<div class="card">
					<div class="card-row1">
						<img class="card-icon" src="../assets/card3.svg" alt="card3" />
						<div class="card-title">IA intuitive</div>
					</div>
					<div class="card-row2">
						<div class="card-subtitle">
							Utilise une IA avancée pour des interactions fluides et une compréhension des données.
						</div>
					</div>
					<div class="card-row3">
						<div class="more">En apprendre plus</div>
						<img class="arrow" src="../assets/arrow.svg" alt="arrow" />
					</div>
				</div>
			</div>
			<div class="features-row">
				<div class="card">
					<div class="card-row1">
						<img class="card-icon" src="../assets/card4.svg" alt="card4" />
						<div class="card-title">Personnalisation avancée</div>
					</div>
					<div class="card-row2">
						<div class="card-subtitle">
							Personnalisation des préférences pour recevoir des informations spécifiques et pertinentes.
						</div>
					</div>
					<div class="card-row3">
						<div class="more">En apprendre plus</div>
						<img class="arrow" src="../assets/arrow.svg" alt="arrow" />
					</div>
				</div>
				<div class="card">
					<div class="card-row1">
						<img class="card-icon" src="../assets/card5.svg" alt="card5" />
						<div class="card-title">Interface conviviale</div>
					</div>
					<div class="card-row2">
						<div class="card-subtitle">
							Une expérience utilisateur conçue pour rendre l'exploration des statistiques sportives accessible.
						</div>
					</div>
					<div class="card-row3">
						<div class="more">En apprendre plus</div>
						<img class="arrow" src="../assets/arrow.svg" alt="arrow" />
					</div>
				</div>
				<div class="card">
					<div class="card-row1">
						<img class="card-icon" src="../assets/card6.svg" alt="card6" />
						<div class="card-title">Notifications personnalisées</div>
					</div>
					<div class="card-row2">
						<div class="card-subtitle">
							Envoie des alertes et des mises à jour en fonction des intérêts et des équipes favorites de l'utilisateur.
						</div>
					</div>
					<div class="card-row3">
						<div class="more">En apprendre plus</div>
						<img class="arrow" src="../assets/arrow.svg" alt="arrow" />
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
	.features {
		height: 100vh;
		background: linear-gradient(135deg, rgba(255, 255, 255, 1) 20%, rgba(205, 250, 12, 0.4907388126148897) 100%);
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
	.features-container {
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.features-row {
		width: 85vw;
		display: flex;
		justify-content: space-around;
		margin-top: 4.5%;
	}
	.card {
		width: 100%;
		height: 190px;
		background-color: v-bind(bg);
		margin: 0px 25px;
		border-radius: 10px;
		cursor: pointer;
		transition: 0.4s all ease-in-out;
		box-shadow: 0px 0px 10px 2px rgba(15, 26, 41, 0.2);
	}
	.card:hover {
		transform: translateY(0px) scale(1.07);
		background-color: v-bind(primary);
	}
	.card-row1 {
		display: flex;
		align-items: center;
		padding-left: 20px;
		padding-top: 15px;
	}
	.card-icon {
		height: 40px;
		width: 40px;
	}
	.card-title {
		padding-left: 10px;
		font-size: 1rem;
		font-weight: 600;
	}
	.card-row2 {
		display: flex;
		padding-left: 40px;
		padding-top: 12.5px;
		padding-right: 30px;
	}
	.card-subtitle {
		font-size: 0.9rem;
		font-weight: 300;
	}
	.card-row3 {
		display: flex;
		align-items: center;
		padding-left: 40px;
		padding-top: 20px;
	}
	.more {
		font-size: 0.75rem;
		font-weight: 500;
	}
	.arrow {
		margin-left: 4px;
		height: 25px;
	}
</style>
