<template>
  <div style="height:100vh; background:#f6f7f9 !important">
    <v-card height="100%">
      <nav-drawer />
      <v-card class="fill-height page-content sharp-card" height="182" outlined>
        <NormalHeader headerTitle="INDEX" />

        <v-container class="pa-5 pt-5 p-body" grid-list-xl fluid>
          <br />
          <Searchbar />
          <div v-if="this.$store.state.userlogged ===''|| this.$store.state.userProfile.showStats">
            <h3 class="ml-2 mb-4">STATS</h3>
            <v-layout row wrap>
              <v-flex xs4 class>
                <v-card class="mx-auto" outlined>
                  <v-list-item three-line>
                    <v-list-item-content>
                      <div class="overline mb-4">Projects created</div>
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
                        <h1>{{taskContribs}}</h1>
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
                      <div class="overline mb-4">Tasks</div>
                      <v-list-item-title class="headline mb-1">
                        <h1>{{tasks}}</h1>
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
                      <div class="overline mb-4">Threads</div>
                      <v-list-item-title class="headline mb-1">
                        <h1>{{threads}}</h1>
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
                        <h1>{{posts}}</h1>
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
          </div>
          <div v-if="this.$store.state.userlogged ===''|| this.$store.state.userProfile.showRNDM">
            <h3 class="ml-2 my-4">FEELING LUCKY</h3>

            <v-layout row wrap>
              <v-flex class>
                <v-card class="mx-auto" outlined>
                  <v-list-item three-line>
                    <v-list-item-content>
                      <div class="overline mb-4">random project</div>
                      <v-list-item-title class="headline mb-1">
                        <h3 class="mb-2">{{randomProject.title}}</h3>
                      </v-list-item-title>
                      <span>{{randomProject.detailedDesc}}</span>
                    </v-list-item-content>
                  </v-list-item>

                  <v-card-actions>
                    <v-btn text :to="{ name: 'Project', params: { id: randomProject.id} }">View</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>

            <v-divider></v-divider>
          </div>
          <div
            v-if="this.$store.state.userlogged ===''|| this.$store.state.userProfile.showLeaders"
          >
            <h3 class="ml-2 my-4">LEADERBOARD</h3>

            <v-layout row wrap style="align-items:flex-end">
              <v-flex xs4 class>
                <v-card class="mx-auto text-center" dark color="warning" outlined>
                  <v-list-item three-line>
                    <v-list-item-content>
                      <div
                        v-if="topProfiles.length>0"
                        class="overline mb-4"
                      >{{topProfiles[0].point}} points</div>
                      <v-list-item-title class="headline mb-1">
                        <h1
                          v-if="topUsers.length>0"
                          class="mb-2"
                          style="text-transform:uppercase"
                        >{{topUsers[0].username}}</h1>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-card>
              </v-flex>
              <v-flex xs4 class>
                <v-card class="mx-auto text-center" dark color="primary" outlined>
                  <v-list-item three-line>
                    <v-list-item-content>
                      <div
                        v-if="topProfiles.length>1"
                        class="overline mb-4"
                      >{{topProfiles[1].point}} points</div>
                      <v-list-item-title class="headline mb-1">
                        <h2
                          v-if="topUsers.length>1"
                          class="mb-2"
                          style="text-transform:uppercase"
                        >{{topUsers[1].username}}</h2>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-card>
              </v-flex>

              <v-flex xs4 class>
                <v-card class="mx-auto text-center" dark color="success" outlined>
                  <v-list-item three-line>
                    <v-list-item-content>
                      <div
                        class="overline mb-4"
                        v-if="topProfiles.length==3"
                      >{{topProfiles[2].point}} points</div>
                      <v-list-item-title class="headline mb-1">
                        <h3
                          v-if="topUsers.length==3"
                          class="mb-2"
                          style="text-transform:uppercase"
                        >{{topUsers[2].username}}</h3>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-card>
              </v-flex>
            </v-layout>
            <v-divider></v-divider>
          </div>

          <h3 class="ml-2 mt-4">ACTIVITY LOG</h3>
          <br />

          <v-card dark class="pa-4" flat color="primary">
            <v-list-item v-for="activity in activities" :key="activity.id">
              <v-list-item-content>
                <v-list-item-title>{{activity.created}} : {{activity.title}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-card>
          <br />
          <div v-if="this.$store.state.userlogged ===''|| this.$store.state.userProfile.showNews">
            <v-divider></v-divider>

            <h3 class="ml-2 my-4">LATEST TECH NEWS</h3>

            <v-layout row wrap>
              <v-flex class v-for="n in news" :key="n.url">
                <v-card class="mx-auto" outlined>
                  <v-list-item three-line>
                    <v-list-item-content>
                      <div class="overline mb-4">{{n.author}}</div>
                      <v-list-item-title class="headline mb-1">
                        <h4 class="mb-2">{{n.title}}</h4>
                      </v-list-item-title>
                      <span>{{n.description}}</span>
                    </v-list-item-content>
                    <v-list-item-avatar tile size="80" color="grey">
                      <v-img v-if="n.urlToImage" :src="n.urlToImage"></v-img>
                    </v-list-item-avatar>
                  </v-list-item>

                  <v-card-actions>
                    <v-btn text :href="n.url">View</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>

            <v-divider></v-divider>
          </div>
        </v-container>
      </v-card>
    </v-card>
  </div>
</template>

<script >
import axios from "axios";
// axios.defaults.withCredentials = true;
import Searchbar from "./SearchBar.vue";
import NormalHeader from "./NormalHeader.vue";

export default {
  components: {
    Searchbar,
    NormalHeader
  },
  data() {
    return {
      projects: [],
      threads: 0,
      posts: 0,
      tasks: 0,
      taskContribs: 0,
      randomProject: {},
      activities: {},
      topProfiles: [],
      topUsers: [],
      news: []
    };
  },
  created() {
    fetch(
      "http://newsapi.org/v2/everything?q=technology&from=2020-06-01&sortBy=publishedAt&apiKey=dfe92ce15ec245f6bff49c88db87e1fa"
    )
      .then(res => res.json())
      .then(res => {
        console.log(res);
        this.news = res.articles;
      })
      .catch(err => {
        console.log(err);
      });

    axios.get("http://localhost:8000/projects/").then(pres => {
      this.projects = pres.data;
      const datal = pres.data.length;
      this.randomProject = pres.data[Math.floor(Math.random() * datal)];
    });

    axios.get("http://localhost:8000/threads/").then(pres => {
      this.threads = pres.data.length;
    });

    fetch("http://localhost:8000/threadPosts/")
      .then(res => res.json())
      .then(res => {
        this.posts = res.length;
      })
      .catch(err => {
        console.log(err);
      });

    axios.get("http://localhost:8000/tasks/").then(pres => {
      this.tasks = pres.data.length;
    });

    axios.get("http://localhost:8000/taskcontrib/").then(pres => {
      this.taskContribs = pres.data.length;
    });

    fetch("http://localhost:8000/activities/?act")
      .then(res => res.json())
      .then(res => {
        this.activities = res;
      })
      .catch(err => {
        console.log(err);
      });

    axios.get("http://localhost:8000/profiles/").then(pres => {
      this.topProfiles = pres.data;
      this.topProfiles.sort(function(a, b) {
        if (a.point > b.point) return -1;
        if (a.point < b.point) return 1;
        return 0;
      });
      this.topProfiles.forEach(element => {
        const slice = element.user.slice("/");
        axios
          .get("http://localhost:8000/users/" + slice[slice.length - 2])
          .then(upres => {
            this.topUsers.push(upres.data);
            console.log(this.topUsers);
          });
      });
    });
  }
};
</script>