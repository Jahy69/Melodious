<template>
  <div id="Acceuil" class="container">
    <img src="../../public/assets/robot.svg" />
    <div class="cta">
      <h1>
        Explorez l'univers <br />musical avec <br />
        Melodious
      </h1>
      <p>
        L'IA conversationnelle qui vous guide à travers les mélodies, les
        histoires et les rythmes.
      </p>
      <a class="bouton" href="#demo">Essayez Melodious</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "SiteBot",
};
</script>

<style scoped>
.container {
  background-image: url("../../public/assets/blob.svg");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: 20%;
  height: 80vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 3vh;
  margin-top: 4vh;
}

.cta {
  width: 45%;
  margin-left: 5vw;
  text-align: center;
}

img {
  height: auto;
  width: 25%;
}

h1 {
  font-size: 10vh;
  text-align: start;
  font-weight: bolder;
}

p {
  font-size: 2vh;
  text-align: start;
  margin-top: 2vh;
  font-weight: bold;
  margin-bottom: 6vh;
}

.bouton {
  text-decoration: none;
  border-radius: 50px;
  padding: 2vh 2vw;
  font-family: "Inria Sans", sans-serif;
  border: none;
  font-size: 2.5vh;
  font-weight: bold;
  cursor: pointer;
  background-color: #000000;
  color: rgb(255, 255, 255);
  transition: color 0.3s ease;
}

.bouton:hover {
  color: #9b85c5;
}

.button:focus {
  outline: none;
}

@media only screen and (max-width: 768px) {
  .container {
    flex-direction: column;
    text-align: center;
  }

  .cta {
    width: 80%;
    margin: 0 auto;
    margin-top: 20px;
  }

  img {
    width: 50%;
  }
}
</style>
