<template>
  <div style="height:100vh">
    <v-card height="100%" style="background:#f6f7f9 !important; overflow:hidden !important">
      <nav-drawer />
      <v-card class="fill-height page-content sharp-card" height="182" outlined>
        <proj-header
          :projectname="projectName"
          :categories="categories"
          :key="update"
          :user="projectOwner"
        />
        <div class="pa-3 pt-5 p-body">
          <div v-if="dataFetched">
            <gitSource :repoRoot="repo" />
            <!-- <v-source></v-source> -->
            <br />
            <div v-for="(task, t) in tasks" :key="t">
              <v-task :dataurl="task.url" :projectOwnerId="projectOwner.pk" />
              <br />
            </div>
            <br />
            <v-btn
              @click.stop="dialog = true"
              block
              outlined
              color="#34495e"
              v-if="projectOwner.pk == this.$store.state.userlogged.pk"
            >New Task</v-btn>
            <v-dialog v-model="dialog" max-width="500" class="pa-3">
              <v-card>
                <v-card-title class="headline">Add new task</v-card-title>
                <v-divider></v-divider>

                <v-card-text class="mt-3">
                  <v-form v-on:submit.prevent="AddTask()" id="addTask-form">
                    <v-text-field filled label="Task name" id="title"></v-text-field>
                    <v-text-field filled label="Task description" id="desc"></v-text-field>
                    <v-menu
                      ref="menu"
                      v-model="menu"
                      :close-on-content-click="false"
                      :return-value.sync="date"
                      transition="scale-transition"
                      offset-y
                      max-width="290px"
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on }">
                        <v-text-field
                          id="date"
                          v-model="date"
                          label="End date"
                          append-icon="mdi-calendar"
                          readonly
                          filled
                          v-on="on"
                        ></v-text-field>
                      </template>
                      <v-date-picker no-title scrollable>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                        <v-btn text color="primary" @click="$refs.menu.save(date)">OK</v-btn>
                      </v-date-picker>
                    </v-menu>
                    <categorySelect ref="catsRef" />
                    <technologySelect ref="techsRef" />
                  </v-form>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>

                  <v-btn color="green darken-1" text @click="dialog = false">Cancel</v-btn>

                  <v-btn
                    color="green darken-1"
                    text
                    @click="dialog = false"
                    form="addTask-form"
                    type="submit"
                  >Submit</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </div>
          <div v-else>
            <v-progress-circular indeterminate color="red"></v-progress-circular>
          </div>
        </div>
      </v-card>
    </v-card>
  </div>
</template>

<style>
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
// axios.defaults.withCredentials = true;

export default {
  components: {
    categorySelect,
    technologySelect,
    gitSource
  },
  data: () => ({
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
    update: 0,
    projectOwner: {}
  }),
  methods: {
    // Triggered when `childToParent` event is emitted by the child.

    LoadProject() {
      axios
        .get("http://localhost:8000/projects/" + this.$route.params.id)
        .then(response => {
          this.repo = response.data.repo;
          this.url = response.data.url;
          this.projectName = response.data.title;
          this.projectDesc = response.data.detailedDesc;
          if (response.data.categories != null)
            this.categories = response.data.categories.split(",");
          const split = response.data.owner.split("/");
          axios
            .get("http://localhost:8000/users/" + split[split.length - 2])
            .then(urep => {
              this.projectOwner = urep.data;
            });

          this.LoadTasks();
        });
    },

    LoadTasks() {
      axios.get("http://localhost:8000/tasks/").then(response => {
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
        project: this.url,
        categories: this.$refs.catsRef.GetChips().toString(),
        technologies: this.$refs.techsRef.GetChips().toString()
      };
      axios({
        method: "post",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          Accept: "application/json",
          "X-CSRFToken": this.csrf()
        },
        url: "http://localhost:8000/tasks/",
        data: JSON.stringify(postData)
      }).then(this.LoadTasks());
    },
    csrf() {
      return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken"))
        .split("=")[1];
    }
  },
  mounted() {
    console.log(this.csrf());
    this.LoadProject();
  }
};
</script>
