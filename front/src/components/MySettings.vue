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
          <h3 class="ml-2 mb-4">My Settings</h3>

          <v-card class="mb-4">
            <v-card-actions class="ml-2">
              <v-switch label="Accout is public" flat inset v-model="pblc"></v-switch>
            </v-card-actions>
          </v-card>

          <v-card class="mb-4">
            <v-card-actions class="ml-2">
              <v-switch label="Show stats" flat inset v-model="stats"></v-switch>
            </v-card-actions>
          </v-card>

          <v-card class="mb-4">
            <v-card-actions class="ml-2">
              <v-switch label="Show leaderboards" flat inset v-model="lbs"></v-switch>
            </v-card-actions>
          </v-card>

          <v-card class="mb-4">
            <v-card-actions class="ml-2">
              <v-switch label="Show random projects" flat inset v-model="rndm"></v-switch>
            </v-card-actions>
          </v-card>

          <v-card class="mb-4">
            <v-card-actions class="ml-2">
              <v-switch label="Show activities" flat inset v-model="acts"></v-switch>
            </v-card-actions>
          </v-card>

          <v-card class="mb-4">
            <v-card-actions class="ml-2">
              <v-switch label="Show news" flat inset v-model="news"></v-switch>
            </v-card-actions>
          </v-card>

          <v-card-actions class="ml-2">
            <v-spacer></v-spacer>
            <v-btn color="gray" text outlined depressed>default</v-btn>
            <v-btn color="success" text outlined depressed @click.stop="update">save</v-btn>
          </v-card-actions>
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
      news: this.$store.state.userProfile.showNews,
      lbs: this.$store.state.userProfile.showLeaders,
      rndm: this.$store.state.userProfile.showRNDM,
      acts: this.$store.state.userProfile.showActs,
      pblc: this.$store.state.userProfile.isPublic,
      stats: this.$store.state.userProfile.showStats
    };
  },
  methods: {
    csrf() {
      return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken"))
        .split("=")[1];
    },
    update() {
      axios(
        "http://localhost:8000/profiles/" +
          this.$store.state.userProfile.id +
          "/",
        {
          method: "put",
          data: {
            user: this.$store.state.userProfile.user,
            age: this.$store.state.userProfile.age,
            level: this.$store.state.userProfile.level,
            point: this.$store.state.userProfile.point,
            userType: this.$store.state.userProfile.userType,
            isPublic: this.pblc,
            showLeaders: this.lbs,
            showRNDM: this.rndm,
            showActs: this.acts,
            showStats: this.stats,
            showNews: this.news
          },
          headers: {
            "X-CSRFToken": this.csrf()
          }
        }
      )
        .then(pres => {
          console.log(pres.data);
        })
        .catch(error => {
          console.log(error.response);
        });
    }
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