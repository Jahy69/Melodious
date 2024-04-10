<template>
  <h1>Témoignage</h1>
  <div class="container">
    <div class="avis">
      <img src="../../public/assets/femme.svg" alt="objet" class="femme">
      <div class="avistxt">
        <h2>Lisa</h2>
        <p>Melodious a transformé ma manière d'explorer la musique. C'est comme avoir un ami musical toujours prêt à partager des anecdotes et des détails fascinants sur chaque genre. Une expérience immersive et instructive que je recommande vivement!</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SiteAvis'
}
</script>

<style scoped>

p {
  margin-top: 2vh;
  font-size: 2.2vh;
  text-align: left;
  font-style: italic;
}

h2 {
  margin-top: 4vh;
  font-size: 4vh;
}

h1 {
  text-align: center;
  margin-top: 10vh;
}

.avis {
  width: 70%;
  max-width: auto;
  height: auto;
  border-radius: 10px;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);
  display: flex;
  margin: 0 auto;
  padding: 20px;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  margin-top: 10vh;
}

.femme {
  margin-right: 3.5vh;
  width: 10vh;
  height: auto;
}

.avistxt {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

@media only screen and (max-width: 768px) {
  .avis {
    flex-direction: column;
  }
}
</style>
