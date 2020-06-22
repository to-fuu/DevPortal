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
          <h3 class="ml-2 mb-4">My projects</h3>
          <v-layout row wrap>
            <v-flex xs4 v-for="(p, t) in projects" :key="t">
              <v-card class="mx-auto" outlined>
                <v-list-item three-line>
                  <v-list-item-content>
                    <div class="overline mb-4"></div>
                    <v-list-item-title class="headline mb-1">
                      <h3>{{p.title}}</h3>
                    </v-list-item-title>
                    <v-list-item-subtitle>{{p.briefDesc}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>

                <v-card-actions>
                  <v-btn text :to="{ name: 'Edit', params: { id: p.id } }">Edit</v-btn>
                  <v-btn text>Forum</v-btn>
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
      isAdmin: false
    };
  },
  created() {
    // axios(
    //   "http://newsapi.org/v2/everything?q=technology&from=2020-05-21&sortBy=publishedAt&apiKey=dfe92ce15ec245f6bff49c88db87e1fa",
    //   {
    //     method: "get",
    //     withCredentials: false,
    //     headers: {
    //       "Access-Control-Allow-Origin": "*",
    //       "Content-Type": "application/json",
    //       "Access-Control-Allow-Credentials": "true",
    //       "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS,POST,PUT",
    //       "Access-Control-Allow-Headers":
    //         "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
    //     }
    //   }
    // ).then(pres => {
    //   console.log(pres.data);
    // });

    axios.get("http://localhost:8000/my_projects/").then(pres => {
      this.projects = pres.data;
      console.log(this.projects);
    });
    axios.get("http://localhost:8000/rest-auth/user/isAdmin").then(pres => {
      this.isAdmin = pres.data === "True";
    });
  }
};
</script>