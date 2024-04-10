<template>
  <h1 id="fonctionnalité" class="titre">Fonctionnalités Clés</h1>
  <div class="container">
    <div class="card">
      <h1 class="content1">Exploration Intuitive</h1>
      <p class="content2">
        Découvrez des genres musicaux variés à travers des conversations
        naturelles.
      </p>
    </div>

    <div class="card">
      <h1 class="content1">Expertise Assurée</h1>
      <p class="content2">
        Des informations approfondies sur l'histoire, le rythme, les influences
        et bien plus encore.
      </p>
    </div>

    <div class="card">
      <h1 class="content1">Vérification des Faits</h1>
      <p class="content2">
        Accédez à des sources fiables pour enrichir vos connaissances musicales.
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "SiteFeatures",
};
</script>

<style scoped>
.titre {
  margin-top: 10vh;
  justify-content: center;
  text-align: center;
  font-size: 5vh;
}

.card {
  width: calc(33.33% - 20px);
  margin: 0 10px;
  height: auto;
  background-color: #f2f2f2;
  border-radius: 20px;
  text-align: center;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
}

.content1 {
  font-size: 3.5vh;
  margin-top: 3vh;
}

.content2 {
  margin: 4vh;
  font-size: 3vh;
}

.container {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  margin-top: 10vh;
}

@media only screen and (max-width: 768px) {
  .card {
    width: calc(50% - 20px);
  }
}
</style>
