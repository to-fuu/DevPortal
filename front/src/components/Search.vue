<template>
  <div style="height:100vh; background:#f6f7f9 !important">
    <v-card height="100%">
      <nav-drawer />
      <v-card class="fill-height page-content sharp-card" height="182" outlined>
        <NormalHeader :headerTitle="'Results for ' +this.$route.params.q " />

        <v-container class="pa-5 pt-5 p-body" grid-list-xl fluid>
          <h4>Projects</h4>
          <br />
          <Searchbar />

          <div class="mb-5">
            <v-layout column wrap>
              <v-flex class v-for="n in pq" :key="n.id">
                <v-card class="mx-auto" outlined>
                  <v-list-item three-line>
                    <v-list-item-content>
                      <div class="overline mb-4">PROJECT</div>
                      <v-list-item-title class="headline mb-1">
                        <h4 class="mb-2">{{n.title}}</h4>
                      </v-list-item-title>
                      <span>{{n.briefDesc}}</span>
                    </v-list-item-content>
                  </v-list-item>

                  <v-card-actions>
                    <v-btn text :to="{ name: 'Project', params: { id: n.id } }">View</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>
          </div>

          <h4>Users</h4>
          <br />
          <Searchbar />

          <div class="mb-5">
            <v-layout column wrap>
              <v-flex class v-for="n in uq" :key="n.id">
                <v-card class="mx-auto" outlined>
                  <v-list-item three-line>
                    <v-list-item-content>
                      <div class="overline mb-4">PROJECT</div>
                      <v-list-item-title class="headline mb-1">
                        <h4 class="mb-2">{{n.username}}</h4>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>

                  <v-card-actions>
                    <v-btn text :to="{ name: 'Profile', params: { id: n.pk } }">View</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>
          </div>

          <h4>Tasks</h4>
          <br />
          <Searchbar />

          <div class="mb-5">
            <v-layout column wrap>
              <v-flex class v-for="n in tq" :key="n.id">
                <v-card class="mx-auto" outlined>
                  <v-list-item three-line>
                    <v-list-item-content>
                      <div class="overline mb-4">PROJECT</div>
                      <v-list-item-title class="headline mb-1">
                        <h4 class="mb-2">{{n.title}}</h4>
                      </v-list-item-title>
                      <span>{{n.desc}}</span>
                    </v-list-item-content>
                  </v-list-item>

                  <v-card-actions>
                    <v-btn text :to="{ name: 'Project', params: { id: n.id } }">View</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>
          </div>

          <h4>Threads</h4>
          <br />
          <Searchbar />

          <div class="mb-5">
            <v-layout column wrap>
              <v-flex class v-for="n in thq" :key="n.id">
                <v-card class="mx-auto" outlined>
                  <v-list-item three-line>
                    <v-list-item-content>
                      <div class="overline mb-4">PROJECT</div>
                      <v-list-item-title class="headline mb-1">
                        <h4 class="mb-2">{{n.title}}</h4>
                      </v-list-item-title>
                      <span>{{n.briefDesc}}</span>
                    </v-list-item-content>
                  </v-list-item>

                  <v-card-actions>
                    <v-btn text :to="{ name: 'Project', params: { id: n.id } }">View</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>
          </div>
        </v-container>
      </v-card>
    </v-card>
  </div>
</template>

<script >
import Searchbar from "./SearchBar.vue";
import NormalHeader from "./NormalHeader.vue";

export default {
  components: {
    Searchbar,
    NormalHeader
  },
  data() {
    return {
      pq: [],
      uq: [],
      tq: [],
      thq: []
    };
  },
  created() {
    console.log("ss");
    fetch("http://localhost:8000/projects?q=" + this.$route.params.q)
      .then(res => res.json())
      .then(res => {
        this.pq = res;
      })
      .catch(err => {
        console.log(err);
      });
    fetch("http://localhost:8000/users?q=" + this.$route.params.q)
      .then(res => res.json())
      .then(res => {
        this.uq = res;
      })
      .catch(err => {
        console.log(err);
      });
    fetch("http://localhost:8000/tasks?q=" + this.$route.params.q)
      .then(res => res.json())
      .then(res => {
        this.tq = res;
      })
      .catch(err => {
        console.log(err);
      });
    fetch("http://localhost:8000/threads?q=" + this.$route.params.q)
      .then(res => res.json())
      .then(res => {
        this.thq = res;
      })
      .catch(err => {
        console.log(err);
      });
  }
};
</script>