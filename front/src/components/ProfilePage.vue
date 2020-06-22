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
          showSettings="true"
        />

        <v-container class="pa-5 pt-5 p-body" grid-list-xl fluid>
          <h3 class="ml-2 mb-4">Stats</h3>
          <v-layout row wrap>
            <v-flex xs4 class>
              <v-card class="mx-auto" outlined>
                <v-list-item three-line>
                  <v-list-item-content>
                    <div class="overline mb-4">Projects</div>
                    <v-list-item-title class="headline mb-1">
                      <h1>{{projects.length}}</h1>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-card-actions>
                  <v-btn text :to="{ name: 'MyProjects'}">View</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
            <v-flex xs4 class>
              <v-card class="mx-auto" outlined>
                <v-list-item three-line>
                  <v-list-item-content>
                    <div class="overline mb-4">Contributions</div>
                    <v-list-item-title class="headline mb-1">
                      <h1>{{validated}}</h1>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>

                <v-card-actions>
                  <span class="mx-2">
                    <h4 style="display:inline-block">validated</h4>
                    out of {{contribs.length}} contributions
                  </span>
                  <v-btn text style="opacity:0; z-index:-10">Button</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
            <v-flex xs4 class>
              <v-card class="mx-auto" outlined>
                <v-list-item three-line>
                  <v-list-item-content>
                    <div class="overline mb-4">Thread posts</div>
                    <v-list-item-title class="headline mb-1">
                      <h1>100</h1>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-card-actions>
                  <v-btn text style="opacity:0; z-index:-10">Button</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
            <v-flex xs6 class>
              <v-card class="mx-auto" color="primary" dark outlined>
                <v-list-item three-line>
                  <v-list-item-content>
                    <div class="overline mb-4">Points</div>
                    <v-list-item-title class="headline mb-1">
                      <h1>{{this.$store.state.userProfile.point}}</h1>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-card-actions>
                  <v-btn text style="opacity:0; z-index:-10">Button</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
            <v-flex xs6 class>
              <v-card class="mx-auto" color="primary" dark outlined>
                <v-list-item three-line>
                  <v-list-item-content>
                    <div class="overline mb-4">Global Rank</div>
                    <v-list-item-title class="headline mb-1">
                      <h1>1</h1>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-card-actions>
                  <v-btn text style="opacity:0; z-index:-10">Button</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
          <v-divider></v-divider>
          <h3 class="ml-2 my-4">Activities log</h3>
        </v-container>
      </v-card>
    </v-card>
  </div>
</template>

<script >
import axios from "axios";
// axios.defaults.withCredentials = true;

export default {
  data() {
    return {
      projects: [],
      isAdmin: false,
      contribs: [],
      validated: 0
    };
  },
  created() {
    axios.get("http://localhost:8000/my_projects/").then(pres => {
      this.projects = pres.data;
    });

    axios.get("http://localhost:8000/rest-auth/user/isAdmin/").then(pres => {
      this.isAdmin = pres.data === "True";
    });

    axios
      .get(
        "http://localhost:8000/taskcontrib/?uid=" +
          this.$store.state.userlogged.pk
      )
      .then(pres => {
        this.contribs = pres.data;
        pres.data.forEach(element => {
          if (element.progress == 2) this.validated++;
        });

        console.log(pres.data);
      });
  }
};
</script>