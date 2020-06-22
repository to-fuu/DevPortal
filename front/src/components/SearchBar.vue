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
      v-model="searchVal"
      @keydown.enter="search"
    ></v-text-field>
    <v-avatar class="mx-2" height="40" width="40">
      <img v-if="$store.state.userlogged!==''" :src="$store.state.userProfile.photo" alt="John" />
      <img
        v-else
        src="https://developers.google.com/web/images/contributors/no-photo.jpg"
        alt="nouser"
      />
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

<script >
export default {
  data() {
    return {
      searchVal: ""
    };
  },
  methods: {
    search() {
      if (this.searchVal == "") return;
      this.$router.push({ name: "Search", params: { q: this.searchVal } });
      this.$router.go();
    }
  }
};
</script>
