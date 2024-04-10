<template>
  <footer>
    <div class="container">
      <div class="left">
        <img src="../../public/assets/logo_noir.svg" alt="">
        <p>6 Rue sainte Catherine <br> 69003 Lyon <br> contact@melodious.com </p>
      </div>
      <div class="reseaux">
        <img src="../../public/assets/twitter.svg" alt="" class="icon">
        <img src="../../public/assets/youtube.svg" alt="" class="icon">
        <img src="../../public/assets/instagram.svg" alt="" class="icon">
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'SiteFooter'
}
</script>

<style scoped>

footer {
  margin-top: 7.5vh;
  padding-top: 20vh;
  background-image:url("../../public/assets/vague.svg") ;
  background-size: cover;
  width: 100vw;
  height: 25vh;
  background-repeat: no-repeat;
}

p {
  margin-top: 2vh;
  color: white;
}

.container {
  display: flex;
  justify-content: space-between;
  padding: 0 5vw;
}

.reseaux {
  display: flex;
}

.left {
  margin-top: 0vh;
}

.icon {
  margin :10px;
}

/* Media Query pour les écrans de petite taille */
@media only screen and (max-width: 768px) {
  footer {
    padding-top: 10vh;
    height: auto;
  }

  .container {
    flex-direction: column;
    align-items: center;
    padding: 0 2vw;
  }

  .left {
    text-align: center;
    margin-top: 5vh;
  }

  .reseaux {
    margin-top: 5vh;
  }

  p {
    text-align: center;
  }
}
</style>
