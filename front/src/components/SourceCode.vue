<template>
  <v-card class="mx-auto" elevation="4">
    <v-list>
      <v-subheader class>
        <p class="title">Project name</p>
        <div class="sc-details subtitle">
          Last updated 5 minutes ago
          <v-btn dark class="download ml-2">Download</v-btn>
        </div>
      </v-subheader>
      <v-list-item-group v-model="item" color="primary">
        <v-list-item v-for="(item, i) in items" :key="i">
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    item: 1,
    items: [
      { text: "Folder", icon: "mdi-folder-outline" },
      { text: "Folder2", icon: "mdi-folder-outline" },
      { text: "File1", icon: "mdi-file-outline" },
      { text: "File2", icon: "mdi-file-outline" }
    ]
  })
};
</script>
<style >
.download {
  background: #34495e !important ;
}
.sc-details {
  position: absolute;
  right: 16px;
}
</style>