<script setup>
	import { ref } from "vue";

	const bg = ref("#ffffff");
	const secondary = ref("#0f1a29");
	const primary = ref("#CDFB0A");
</script>

<template>
	<div class="bots">
		<div class="title">Découvrez nos Bots de statistiques sportives</div>
		<div class="logo-container">
			<img class="logo" src="../assets/l1bot.png" alt="L1Bot">
			<img class="logo" src="../assets/l2bot.png" alt="L2Bot">
			<img class="logo" src="../assets/nbabot.png" alt="NBABot">
			<img class="logo" src="../assets/top14bot.png" alt="TOP14Bot">
			<img class="logo" src="../assets/prod2bot.png" alt="PROD2Bot">
		</div>
	</div>
</template>

<style scoped>
	.bots {
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
		justify-content: space-evenly;
		align-items: center;
		width: 75vw;
	}
	.logo {
		height: auto;
		width: 150px;
		display: flex;
		transition: 0.4s all ease-in-out;
	}
	.logo:hover {
		cursor: pointer;
		transform: translateY(0px) scale(1.07);
	}
</style>
