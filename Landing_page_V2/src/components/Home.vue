<script setup>
	import { ref } from "vue";

</script>

<template>
	<div class="home">
    <div class="col-1">
      <p class="title">Melodious</p>
    </div>
    <div class="col-2">colonne 2</div>
    <div class="col-3">colonne 3</div>
	</div>
</template>

<style scoped>
	.home {
    display: flex;
    height: 100%;
  }
  .col-1 {
    width: 20vw;
    display: flex;
    justify-content: end;
  }
  .title {
    color: #BDBCBC;
    font-size: 6rem;
    writing-mode: vertical-rl;
    text-orientation: mixed;
    font-family: "neuropolitical", sans-serif;
  }
  .col-2 {
    width: 60vw;
  }
  .col-3 {
    width: 20vw;
  }
</style>
