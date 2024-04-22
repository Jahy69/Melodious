<script setup>
import { ref } from "vue";
import { useAuth0 } from '@auth0/auth0-vue';

const bg = ref("#ffffff");
const secondary = ref("#0f1a29");
const primary = ref("#CDFB0A");

const { loginWithRedirect, isAuthenticated } = useAuth0();

let header;
function handleScroll(scrollY) {
  header = document.getElementById("bg-header");
  if (scrollY > 70) header.classList.add("bg-white");
  else header.classList.remove("bg-white");
}
window.addEventListener("scroll", (event) => {
  handleScroll(window.scrollY);
});

const login = () => {
  loginWithRedirect();
};
</script>

<template>
  <div class="header-bar" id="bg-header">
    <div class="navigation">
      <RouterLink class="btn-nav" to="/">Accueil</RouterLink>
      <div v-if="!isAuthenticated" class="btn-nav" @click="login">Démo</div>
			<RouterLink v-if="isAuthenticated" class="btn-nav" to="/demo">Démo</RouterLink>
      <RouterLink class="btn-nav" to="/qui-sommes-nous">Qui sommes-nous ?</RouterLink>
      <div v-if="!isAuthenticated" class="login" @click="login">Connexion</div>
			<RouterLink v-if="isAuthenticated" class="login" to="/profil">Profil</RouterLink>
    </div>
  </div>
</template>

<style scoped>
.header-bar {
  z-index: 1000;
  position: fixed;
  width: 100%;
  height: 65px;
  display: flex;
  transition: background-color 0.5s ease;
}
.bg-white {
  background-color: v-bind(bg);
  box-shadow: 0px 5px 10px 1px rgba(15, 26, 41, 0.2);
}
a {
  display: flex;
  align-items: center;
  text-decoration: none !important;
}
.logo {
  width: 29.5vw;
  display: flex;
  justify-content: left;
  align-items: center;
  padding-left: 3vw;
}

.logo-img {
  width: 35px;
  height: 35px;
  margin-right: 10px;
}

.logo-text {
  color: v-bind(secondary);
  font-size: 1.1rem;
  font-weight: 600;
}

.navigation {
  width: 100%;
  display: flex;
  justify-content: end;
  align-items: center;
  margin-right: 2vw;
}

.btn-nav {
  color: v-bind(secondary);
  padding: 15px 25px;
  font-size: 0.9rem;
  font-weight: 600;
	cursor: pointer;
}

.login {
  font-size: 0.9rem;
  width: 125px;
  padding: 10px 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: v-bind(bg);
  background-color: v-bind(secondary);
  border-radius: 10px;
  margin-left: 3vw;
}

.login:hover {
  font-weight: 700;
	cursor: pointer;
}
</style>
