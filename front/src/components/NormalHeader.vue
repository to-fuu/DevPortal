<template>
  <v-card class="fill-height sharp-card" height="164" outlined tile>
    <v-list-item-content class="pa-5 header" style="height:100%">
      <v-list-item-title class="headline font-weight-bold header-title pl-5">{{
        headerTitle
      }}</v-list-item-title>
    </v-list-item-content>
  </v-card>
</template>

<style>
.sharp-card {
  border-radius: 0px;
}

.header {
  display: flex;
  justify-content: flex-end;
  align-content: flex-end;
}
.header-title {
  vertical-align: bottom;
}
</style>

<script>
export default {
  props: ["headerTitle"],
  data: () => ({})
};
</script>
