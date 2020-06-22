<template>
  <div style="height:100vh; background:#f6f7f9 !important">
    <v-card height="100%">
      <nav-drawer />

      <v-card class="fill-height page-content sharp-card" height="182" outlined>
        <profile-header
          :user="this.$store.state.userlogged"
          :profile="this.$store.state.userProfile"
          :projects="projects.length"
          :isAdmin="isAdmin"
        />

        <v-container class="pa-5 pt-5 p-body" grid-list-xl fluid>
          <h3 class="ml-2 mb-4">My Contributions</h3>
          <v-layout row wrap>
            <v-flex xs4 v-for="(p, t) in contribs" :key="t">
              <v-card class="mx-auto" outlined>
                <v-list-item three-line>
                  <v-list-item-content>
                    <div class="overline mb-4">OVERLINE</div>
                    <v-list-item-title class="headline mb-1">
                      <h3>{{p.task.title}}</h3>
                    </v-list-item-title>
                    <v-list-item-subtitle></v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-card-actions>
                  <v-btn text :to="{ name: 'Project', params: { id: p.task.project } }">Project</v-btn>
                  <v-btn text color="error" depressed>Drop</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-card>
  </div>
</template>

<script >
import axios from "axios";
axios.defaults.withCredentials = true;
export default {
  data() {
    return {
      projects: [],
      isAdmin: false,
      contribs: []
    };
  },
  methods: {
    getProjectID(url) {
      const split = url.split("/");
      return split[split.length - 2];
    }
  },
  created() {
    axios(
      "http://newsapi.org/v2/everything?q=technology&from=2020-05-21&sortBy=publishedAt&apiKey=dfe92ce15ec245f6bff49c88db87e1fa",
      {
        method: "get",
        withCredentials: false,
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Content-Type": "application/json",
          "Access-Control-Allow-Credentials": "true",
          "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS,POST,PUT",
          "Access-Control-Allow-Headers":
            "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
        }
      }
    ).then(pres => {
      console.log(pres.data);
    });

    axios.get("http://localhost:8000/my_projects/").then(pres => {
      this.projects = pres.data;
      console.log(this.projects);
    });
    axios.get("http://localhost:8000/rest-auth/user/isAdmin").then(pres => {
      this.isAdmin = pres.data === "True";
    });
    axios
      .get(
        "http://localhost:8000/taskcontrib/?uid=" +
          this.$store.state.userlogged.pk
      )
      .then(pres => {
        this.contribs = pres.data;
        this.contribs.forEach(element => {
          axios.get(element.task).then(tres => {
            element.task = tres.data;

            element.task.project = this.getProjectID(element.task.project);
          });
          console.log(element);
        });
      });
  }
};
</script>