<template>
  <h1 class="titre">Pricing</h1>
  <div class="pricing">
    <div class="container">
      <div class="top">
        <h1>Mensuel</h1>
        <p class="sticker">Populaire</p>
      </div>
      <div class="mid">
        <p>Soutenez le projet Melodious en nous payant un café.</p>
        <div class="prix">
          <h1>2.99€</h1>
          <h4 class="mois">/ mois</h4>
        </div>
      </div>
      <input class="bouton" type="button" value="S'abonner">
    </div>
    <div class="container">
      <div class="top">
        <h1>Annuel</h1>
      </div>
      <div class="mid">
        <p>Rejoingnez la communautée privé de beta test afin de découvrir en avant première les dernières versions de Melodious.</p>
        <div class="prix">
          <h1>29.99€</h1>
          <h4 class="mois">/ an</h4>
        </div>
      </div>
      <input class="bouton" type="button" value="S'abonner">
    </div>
  </div>
</template>

<script>
export default {
  name: 'SitePrix'
}
</script>

<style scoped>
.titre {
  margin-top: 10vh;
  justify-content: center;
  text-align: center;
  font-size: 5vh;
}

.pricing {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  margin-top: 5vh;
}

.container {
  width: 45%;
  height: auto;
  border: 1px solid #000000;
  border-radius: 20px;
  text-align: left;
  margin-bottom: 5vh;
  padding: 1vh;
}

.top {
  display: flex;
  margin: 2vh;
}

.mid {
  margin-left: 2vh;
  font-size: 2vh;
}

.prix {
  display: flex;
  margin-top: 2vh;
}

.mois {
  margin-top: 1.8vh;
  margin-left: 1vh;
}

.sticker {
  font-weight: bold;
  font-size: 2.2vh;
  width: 40%;
  height: 30px;
  background-color: #6FA4E5;
  border-radius: 34px;
  text-align: center;
  margin-left: auto;
  margin-right: 2vh;
  margin-top: 0.5vh;
  color: #FFFFFF;
}

.bouton {
  border-radius: 7px;
  padding: 1vh 2vw;
  font-family: 'Inria Sans', sans-serif;
  font-size: 2.5vh;
  font-weight: bold;
  cursor: pointer;
  background-color: #000000;
  color: #FFFFFF;
  margin-left: 2vh;
  margin-top: 2vh;
  outline: none;
  border: none;
}

.bouton:hover {
  background-color: #FFFFFF;
  color: #000000;
  border: 1px solid black;
}

@media only screen and (max-width: 768px) {
  .container {
    width: 90%;
    margin: 0 auto;
  }
}
</style>
