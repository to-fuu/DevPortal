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
          <h3>Forum</h3>
          <div class="mt-3">
            <v-card
              v-for="(th, t) in threads"
              :key="t"
              class="mb-3"
              :to="{ name: 'ThreadView', params: { id: $route.params.id, tid: th.id } }"
            >
              <v-list-item three-line>
                <v-list-item-content>
                  <div class="overline mb-4">{{th.poster}}</div>
                  <v-list-item-title class="headline mb-2">
                    <h5>{{th.title}}</h5>
                  </v-list-item-title>

                  <v-list-item-subtitle class="mt-2">{{th.body}}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-card>
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
import axios from "axios";

export default {
  components: {},
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
    update: 0,
    forum: {},
    threads: {},
    projectOwner: {}
  }),
  methods: {
    // Triggered when `childToParent` event is emitted by the child.
    ChangeSubPage(value) {
      this.page = value;
    },
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
        });
    },
    LoadForums() {
      axios
        .get("http://localhost:8000/forums?proj=" + this.$route.params.id)
        .then(response => {
          this.forum = response.data[0];
          console.log(response.data);

          this.LoadThreads();
        });
    },
    LoadThreads() {
      axios
        .get("http://localhost:8000/threads?forum=" + this.forum.id)
        .then(response => {
          this.threads = response.data;
          this.threads.forEach(element => {
            axios.get(element.poster).then(r => {
              element.poster = r.data.username;
            });
          });
          console.log(response.data);
        });
    },
    GetUserName(link) {
      let un = "";
      axios.get(link).then(response => {
        un = response.data.username;
        return un;
      });
      return un;
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
        url: "http://localhost:8000/tasks/",
        data: JSON.stringify(postData)
      }).then(this.LoadTasks());
    }
  },
  mounted() {
    this.LoadProject();
    this.LoadForums();
  }
};
</script>
