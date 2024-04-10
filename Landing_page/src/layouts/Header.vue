<template>
  <header>
    <div class="container">
      <img src="../../public/assets/logo.svg" class="logo" />
      <nav class="liste">
        <a class="navigationLink" href="./">Accueil</a>
        <a class="navigationLink" href="#histoire">À Propos</a>
        <a class="navigationLink" href="#fonctionnalité">Fonctionnalité</a>
      </nav>
      <img src="../../public/assets/robert.svg" class="robert" />
    </div>
  </header>
</template>

<script>
export default {
  name: "SiteHeader",
};
</script>

<style scoped>
header {
  background-color: #ffffff;
  padding: 20px 0;
  margin-top: 3vh;
}

h1 {
  margin: 0;
}

.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

nav {
  flex: 1;
  display: flex;
  justify-content: space-around;
  margin: 20px 0;
}

.navigationLink {
  font-weight: bold;
  cursor: pointer;
  color: black;
  text-decoration: none;
}
</style>
