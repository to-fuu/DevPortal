<template>
  <v-card class="mx-auto" elevation="4">
    <v-list>
      <v-subheader class>
        <p class="title">{{fullRepoName}}</p>
        <div class="sc-details subtitle">
          Last update on {{updateDate}}
          <v-btn dark class="download ml-2" :href="downloadUrl">Download</v-btn>
        </div>
      </v-subheader>
      <v-list-item-group v-model="item" color="primary">
        <v-list-item link v-if="path!=''" v-on:click="goTo('')">
          <v-list-item-icon></v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>...</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item v-for="(item, i) in files" :key="i" link v-on:click="goTo(item.name)">
          <v-list-item-icon>
            <v-icon v-text="item.icon" v-if="item.type=='dir'">mdi-folder-outline</v-icon>
            <v-icon v-text="item.icon" v-if="item.type=='file'">mdi-file-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.name"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>

<script>
import axios from "axios";
export default {
  name: "GithubExplorer",
  props: ["repoRoot", "lastUpdate"],
  data() {
    return {
      userName: "blueskythlikesclouds",
      repoName: "SkythTools",
      fullRepoName: "",
      downloadUrl: "",
      treeUrl: "",
      updateDate: "",
      files: [],
      url: "",
      path: "",
      ifShow: false,
      pathArray: ["contents"],
      item: 1
    };
  },
  mounted() {
    console.log(this.repoRoot);

    axios
      .get("https://api.github.com/repos/" + this.repoRoot)
      .then(response => {
        this.fullRepoName = response.data.name;
        this.downloadUrl = response.data.svn_url + "/archive/master.zip";
        this.treeUrl = response.data.contents_url.replace("{+path}", "");
        this.updateDate = response.data.updated_at.substring(0, 10);
        this.getFileTree();
      });
  },
  methods: {
    goTo(link) {
      if (this.treeUrl[this.treeUrl.length - 1] === "/")
        this.treeUrl = this.treeUrl.substring(0, this.treeUrl.length - 1);

      if (link === "") {
        this.treeUrl = this.treeUrl.substring(0, this.treeUrl.lastIndexOf("/"));
        this.path = this.treeUrl.substring(
          this.treeUrl.lastIndexOf("/").this.treeUrl.length
        );
      }

      this.path = link;
      this.treeUrl += "/" + link;
    },
    getFileTree() {
      if (this.treeUrl.length > 0) {
        axios.get(this.treeUrl).then(resp => {
          this.files = resp.data;
        });
      }
    }
  },
  watch: {
    treeUrl: function(newVal, oldVal) {
      this.getFileTree();
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style >
.container {
  width: 100%;
}
.search-input {
  width: 400px;
  border-radius: 5px;
}
.search-button {
  background: #222831;
  color: #eeeeee;
  width: 75px;
}
.index {
  text-align: center;
}
.folder-link {
  color: darkblue;
  font-weight: bold;
}
.file-link {
  color: black;
}
a {
  color: #007bff;
}
</style>