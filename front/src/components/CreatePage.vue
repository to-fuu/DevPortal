<template>
  <div style="height:100vh; background:#f6f7f9 !important">
    <v-card height="100%">
      <nav-drawer />

      <v-card class="fill-height page-content sharp-card" height="182" outlined>
        <page-header headerTitle="Create a project" />

        <div class="pa-3 pt-5 p-body">
          <create-form />
        </div>
      </v-card>
    </v-card>
  </div>
</template>

<script>
export default {
  created() {
    if (this.$store.state.userProfile.userType == 1) this.$router.push("/");
    if (this.$store.state.userlogged === "") this.$router.push("/");
  },
  methods: {
    //
  }
};
</script>

<style>
.page-content {
  margin-left: 256px;
}

.p-body {
  background: #f6f7f9 !important;
}
</style>
