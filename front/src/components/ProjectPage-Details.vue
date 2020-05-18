<template>
  <div style="height:100vh">
    <v-card height="100%" style="background:#f6f7f9 !important; overflow:hidden !important">
      <nav-drawer />
      <v-card class="fill-height page-content sharp-card" height="182" outlined>
        <proj-header
          v-on:SetSubPage="ChangeSubPage"
          :projectname="projectName"
          :categories="categories"
          :key="update"
        />
        <div class="pa-3 pt-5 p-body">
          <div class="mt-3">
            <v-card>
              <v-card-title>{{projectName}}</v-card-title>
              <v-card-text>{{projectDesc}}</v-card-text>
            </v-card>
          </div>
        </div>
      </v-card>
    </v-card>
  </div>
</template>

<style >
.page-content {
  margin-left: 256px;
  overflow-y: scroll;
  height: 100vh !important;
  background: #f6f7f9 !important;
}

.p-body {
  background: #f6f7f9 !important;
}
</style>

<script>
import categorySelect from "./CategorySelect.vue";
import technologySelect from "./TechnologySelect.vue";
import gitSource from "./GithubExplorer.vue";
import editD from "./Edit/TaskDialog.vue";

import axios from "axios";

export default {
  components: {
    categorySelect,
    technologySelect,
    gitSource
  },
  data: () => ({
    page: 1,
    dialog: false,
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    tasks: [],
    repo: "",
    url: "",
    projectName: "",
    projectDesc: "",
    categories: [],
    dataFetched: false,
    update: 0
  }),
  methods: {
    // Triggered when `childToParent` event is emitted by the child.
    ChangeSubPage(value) {
      this.page = value;
    },

    LoadProject() {
      axios
        .get("http://127.0.0.1:8000/projects/" + this.$route.params.id)
        .then(response => {
          this.repo = response.data.repo;
          this.url = response.data.url;
          this.projectName = response.data.title;
          this.projectDesc = response.data.detailedDesc;
          if (response.data.categories != null)
            this.categories = response.data.categories.split(",");
          this.LoadTasks();
        });
    },

    LoadTasks() {
      axios.get("http://127.0.0.1:8000/tasks/").then(response => {
        const tasks = response.data;
        tasks.forEach(element => {
          if (this.url == element.project) {
            this.tasks.push(element);
          }
        });
        this.dataFetched = true;
      });
    },
    AddTask() {
      const postData = {
        title: document.getElementById("title").value,
        desc: document.getElementById("desc").value,
        date: document.getElementById("date").value,
        project: this.url
      };
      axios({
        method: "post",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          Accept: "application/json"
        },
        url: "http://127.0.0.1:8000/tasks/",
        data: JSON.stringify(postData)
      }).then(this.LoadTasks());
    }
  },
  mounted() {
    this.LoadProject();
  }
};
</script>