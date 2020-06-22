<template>
  <div style="height:100vh; background:#f6f7f9 !important">
    <v-card height="100%">
      <nav-drawer />

      <v-card class="fill-height page-content sharp-card" height="182" outlined>
        <profile-header
          :user="user"
          :profile="profile"
          :projects="projects.length"
          :isAdmin="isAdmin"
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
                      <h1>{{contribs.length}}</h1>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>

                <v-card-actions>
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
          </v-layout>
          <v-divider></v-divider>
          <h3 class="ml-2 my-4">Activities</h3>
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
      profile: {},
      user: {},
      projects: [],
      contribs: [],

      isAdmin: false
    };
  },
  beforeCreate() {
    if (this.$route.params.id == this.$store.state.userlogged.pk)
      this.$router.push({ name: "MyProfile" });

    axios
      .get("http://localhost:8000/profiles/?id=" + this.$route.params.id)
      .then(pres => {
        this.profile = pres.data[0];
      });

    axios
      .get("http://localhost:8000/users/" + this.$route.params.id)
      .then(pres => {
        this.user = pres.data;

        axios
          .get("http://localhost:8000/taskcontrib/?uid=" + this.user.pk)
          .then(cres => {
            this.contribs = cres.data;
            console.log(cres.data);
          });
      });
    axios
      .get("http://localhost:8000/projects/?id=" + this.$route.params.id)
      .then(pres => {
        this.projects = pres.data;
      });

    // axios.get("http://localhost:8000/rest-auth/user/isAdmin/").then(pres => {
    //   this.isAdmin = pres.data === "True";
    // });
  }
};
</script>