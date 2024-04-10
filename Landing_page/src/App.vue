
<script setup>
import SiteHeader from "./layouts/Header.vue";
import SiteBot from "./sections/Bot.vue";
import SiteHistoire from "./sections/Histoire.vue";
import SiteFeatures from "./sections/Features.vue";
import SitePrix from "./sections/Prix.vue";
import SiteAvis from "./sections/Avis.vue";
import SiteFooter from "./layouts/Footer.vue";
import SiteDemo from "./sections/Demo.vue";
</script>


<template>
  <SiteHeader />
  <SiteBot />
  <SiteHistoire />
  <SiteFeatures />
  <SitePrix />
  <SiteAvis />
  <SiteDemo />
  <SiteFooter />
</template>


<style>
#app {
  font-family: "Inria Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow: hidden;
}
</style>
