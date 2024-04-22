<template>
	<div>
    <div class="header-padding"></div>
		<h1>Profil</h1>
    <pre v-if="isAuthenticated">
        <code>{{ user }}</code>
      </pre>
    <button @click="logout">Log out</button>
	</div>
</template>

<script>
  import { useAuth0 } from '@auth0/auth0-vue';

  export default {
    setup() {
      const { logout, user, isAuthenticated } = useAuth0();

      return {
        logout: () => {
          logout({ logoutParams: { returnTo: window.location.origin } });
        },
        user,
        isAuthenticated
      };
    }
  };
</script>

<style scoped>
  .header-padding {
  padding-top: 125px;
}
</style>