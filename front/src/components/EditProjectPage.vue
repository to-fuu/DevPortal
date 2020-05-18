<template>
  <div style="height:100vh">
    <v-card height="100%" style="background:#f6f7f9 !important">
      <nav-drawer />

      <v-card class="fill-height page-content sharp-card" height="182" outlined>
        <page-header headerTitle="Edit project" />

        <div class="pa-3 pt-5 p-body">
          <edit-project-form />
        </div>
      </v-card>
    </v-card>
  </div>
</template>


<style >
.page-content {
  margin-left: 256px;
}

.p-body {
  background: #f6f7f9 !important;
}
</style>