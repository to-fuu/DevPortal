<template>
  <v-app>
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import Home from "./components/Home.vue";
import axios from "axios";
axios.defaults.withCredentials = true;

export default Vue.extend({
  name: "App",

  data: () => ({
    //
  }),
  mounted() {
    if (this.$store.state.token) {
      axios.get("http://localhost:8000/profile").then(pres => {
        // console.log(pres.data[0]);
        this.$store.dispatch("saveUserProfile", pres.data[0]);
      });
    }
  }
});
</script>

<style>
body {
  overflow: hidden !important;
}
html {
  overflow: hidden;
}
</style>
