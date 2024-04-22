<script setup>
	import { ref } from "vue";

	const bg = ref("#ffffff");
	const secondary = ref("#0f1a29");
	const primary = ref("#CDFB0A");
</script>

<template>
	<div class="companies">
		<div class="title">Ils nous ont fait confiance en utilisant nos Bots</div>
		<div class="logo-container">
			<img class="logo" src="../assets/ligue1.webp" alt="ligue1">
			<img class="logo" style="transform: scale(1.5);" src="../assets/nba.png" alt="nba">
			<img class="logo" src="../assets/rugby.png" alt="rugby">
			<img class="logo" style="transform: scale(1.4);" src="../assets/decathlon.png" alt="decathlon">
			<img class="logo" style="transform: scale(1.4);" src="../assets/ligueaura.png" alt="ligueaura">
		</div>
	</div>
</template>

<style scoped>
	.companies {
		height: 210px;
		background-color: v-bind(bg);
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.title {
		display: flex;
		justify-content: center;
		padding: 30px 0px;
		color: v-bind(secondary);
		opacity: 0.6;
		font-size: 1.2rem;
	}
	.logo-container {
		display: flex;
		justify-content: space-around;
		align-items: center;
		width: 85vw;
	}
	.logo {
		height: auto;
		width: 100px;
		margin-top: 1vh;
		display: flex;
		filter: invert(0%) sepia(0%) saturate(0%) hue-rotate(151deg) brightness(91%) contrast(102%);
	}
	.logo:hover {
		filter: none;
	}
</style>
