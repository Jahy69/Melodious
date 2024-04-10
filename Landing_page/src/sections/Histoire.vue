<template>
  <div id="histoire" class="txt">
    <h1>Notre Histoire</h1>
    <p class="para">
      Melodious est né de l'ambition de transformer la musique en une langue universelle,
      capable de relier les émotions et les récits de chacun dans un monde où chaque moment de notre vie est rythmé par une mélodie.
      En reconnaissant les défis posés par la diversité musicale et la connectivité intergénérationnelle dans l'ère numérique,
      Melodious a été conçu pour être plus qu'une simple application : un guide personnel dans votre exploration musicale.
    </p>
  </div>

  <div class="container">
    <div class="card">
      <img src="../../public/assets/alexis.svg" alt="alexis"  class="photo">
      <p class="name">Alexis Crocilla</p>
      <p class="role">Chef de projet</p>
    </div>
    <div class="card">
      <img src="../../public\assets\enzo.svg" alt="enzo"  class="photo">
      <p class="name">Enzo Boucherand</p>
      <p class="role">Spécialiste IA</p>
    </div>
    <div class="card">
      <img src="../../public\assets\axel.svg" alt="axel"  class="photo">
      <p class="name">Axel Point</p>
      <p class="role">Développeur</p>
    </div>
    <div class="card">
      <img src="../../public\assets\jimmy.svg" alt="jimmy" class="photo">
      <p class="name">Jimmy Cassarino</p>
      <p class="role">UX/UI designer</p>
    </div>

  </div>

</template>

<script>
export default {
  name: 'SiteHistoire'
}
</script>

<style scoped>

h1{
  text-align: center;
  font-size: 6vh;
}

.txt {
  margin-top: 5vh;
}

.para{
  font-size: 3vh;
  padding: 6vh;
  text-align: center;
}

.container{
  display: flex;
  justify-content: space-evenly;
  margin-top: 10vh;
}

card{
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
}

.name{
  font-size: 3vh;
  display: flex;
  justify-content: space-evenly;
  padding-top: 2vh;
  font-weight: bold;
  text-align: center;
}

.role{
  font-size: 2vh;
  text-align: center;
}

/* Media Query pour les petits écrans */
@media only screen and (max-width: 768px) {
  .container {
    flex-wrap: wrap;
    justify-content: center;
  }

  .card {
    width: 45%;
    margin-bottom: 20px;
  }

  .photo {
    width: 100%;
  }
}

</style>
