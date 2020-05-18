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

export default Vue.extend({
  name: "App",

  data: () => ({
    //
  })
});
</script>

<style >
body {
  overflow: hidden !important;
}
html {
  overflow: hidden;
}
</style>