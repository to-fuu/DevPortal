<template>
  <v-row justify="space-around" class="searchbar">
    <v-text-field
      dense
      rounded
      filled
      solo
      dark
      flat
      width="200"
      label="Search ..."
      prepend-inner-icon="mdi-magnify"
      class="searchfield"
    ></v-text-field>
    <v-avatar class="mx-2" height="40" width="40">
      <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
    </v-avatar>
  </v-row>
</template>


<style>
.searchbar {
  position: absolute;
  top: 40px;
  right: 40px;
}
.searchfield {
  height: 40px !important;
  background: white !important;
  width: 196px;
}

.searchfield .v-input__slot {
  background: #34495e !important;
}
.searchfield .v-input__slot:hover {
  background: #476079 !important;
}
</style>

<script lang="ts">
export default {
  data: () => ({
    //
  })
};
</script>