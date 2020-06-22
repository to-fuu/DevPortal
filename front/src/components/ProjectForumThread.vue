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
            <v-card dark class="mb-3">
              <v-list-item three-line>
                <v-list-item-content>
                  <div class="overline mb-4">
                    {{forum.poster}}
                    <v-divider vertical></v-divider>
                    {{forum.createdAt}}
                  </div>
                  <v-list-item-title class="headline mb-2">
                    <h5>{{forum.title}}</h5>
                  </v-list-item-title>

                  <v-list-item-subtitle class="mt-2">{{forum.body}}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-card>

            <v-card outlined v-for="(th, t) in threads" :key="t" class="mb-3">
              <v-list-item three-line>
                <v-list-item-content>
                  <div class="overline mb-4">
                    {{th.poster}}
                    <v-divider vertical></v-divider>
                    {{th.createdAt}}
                  </div>

                  <v-list-item-title class="mb-2">
                    <p>{{th.body}}</p>
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-card>

            <div v-if="$store.state.userlogged !== ''">
              <br />Reply
              <br />
              <v-textarea class="mt-2" solo name="input-7-4" label="Say something" v-model="reply"></v-textarea>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn dark depressed color @click="Send()">Send</v-btn>
              </v-card-actions>
            </div>
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
    projectOwner: {},
    reply: ""
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
        .get("http://localhost:8000/threads?id=" + this.$route.params.tid)
        .then(response => {
          this.forum = response.data[0];
          console.log(this.forum);
          this.LoadThreads();
        });
    },
    LoadThreads() {
      axios
        .get("http://localhost:8000/threadPosts?th=" + this.$route.params.tid)
        .then(response => {
          this.threads = response.data;
          this.threads.forEach(element => {
            axios.get(element.poster).then(r => {
              element.poster = r.data.username;
            });
          });
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
    csrf() {
      return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken"))
        .split("=")[1];
    },
    Send() {
      const postData = {
        title: "_",
        body: this.reply,
        thread: "http://localhost:8000/threads/" + this.$route.params.tid + "/",
        poster:
          "http://localhost:8000/auth/users/" +
          this.$store.state.userlogged.pk +
          "/"
      };
      console.log(JSON.stringify(postData));
      axios({
        method: "post",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          Accept: "application/json",
          "X-CSRFToken": this.csrf()
        },
        url: "http://localhost:8000/threadPosts/",
        data: JSON.stringify(postData)
      }).then(this.$router.go());
    }
  },
  mounted() {
    this.LoadProject();
    this.LoadForums();
  }
};
</script>
