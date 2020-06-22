<template>
  <v-expansion-panels dark multiple>
    <v-expansion-panel class="task">
      <v-expansion-panel-header>
        {{ title }}
        <div class="status"></div>
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <p>{{ desc }}</p>
        <v-divider></v-divider>
        <br />Contributions
        <v-card class="my-3 pa-3" light v-for="(p, t) in contribs" :key="t">
          <v-card-actions>
            <span>{{p.user.username}}</span>
            <v-divider class="mx-5" vertical></v-divider>
            <span class>{{p.updated}}</span>
            <v-spacer></v-spacer>
            <div v-if="$store.state.userlogged !== ''">
              <v-btn
                v-if="projectOwnerId == $store.state.userlogged.pk && $store.state.userlogged.pk!==''"
                small
                class="mx-1"
                color="success"
              >Validate</v-btn>
              <v-btn
                v-if="projectOwnerId == $store.state.userlogged.pk && $store.state.userlogged.pk!==''"
                small
                class="mx-1"
                color="error"
              >Reject</v-btn>
              <v-btn v-if="ownerId == p.user.pk" class="mx-1" small color="error">Delete</v-btn>
            </div>
          </v-card-actions>
        </v-card>

        <br />
        <v-divider></v-divider>
        <br />

        <div class="mt-2">
          <v-chip
            :v-for="categories !== 'null'"
            class="mx-2 task-chip"
            v-for="(cat, categories) in categories"
            light
            label
            small
            :key="categories"
          >{{ cat }}</v-chip>

          <v-btn
            v-if="projectOwnerId == $store.state.userlogged.pk && $store.state.userlogged.pk!==''"
            light
            depressed
            color="error"
            small
            class="float-right mx-1"
            @click.stop="ToggleDeleteDialog()"
          >Delete</v-btn>
          <v-btn
            v-if="projectOwnerId == $store.state.userlogged.pk && $store.state.userlogged.pk!==''"
            light
            small
            depressed
            class="float-right mx-1"
            @click.stop="ToggleEditDialog()"
          >Edit</v-btn>
          <v-btn
            v-if="projectOwnerId != $store.state.userlogged.pk && $store.state.userlogged.pk!=='' && $store.state.userProfile.userType>1"
            light
            small
            depressed
            @click.stop="contribute()"
            class="float-right mx-1"
          >Contribute</v-btn>
        </div>
      </v-expansion-panel-content>
    </v-expansion-panel>

    <deleteD ref="deleteD" type="task" :title="title" :url="dataurl" />
    <editD
      ref="editD"
      :url="dataurl"
      :title="title"
      :taskData="{ title: this.title, desc: this.desc, date: this.date }"
    />
  </v-expansion-panels>
</template>

<script>
import axios from "axios";
import deleteD from "./Delete/Dialog.vue";
import editD from "./Edit/TaskDialog.vue";

export default {
  components: {
    deleteD,
    editD
  },
  props: ["dataurl", "projectOwnerId"],
  data: () => ({
    id: -1,
    title: "",
    desc: "",
    date: "",
    categories: "",
    dialog: false,
    contribs: [],
    ownerId: -1
  }),
  mounted() {
    this.LoadTask();
  },
  methods: {
    // Triggered when `childToParent` event is emitted by the child.

    LoadTask() {
      axios.get(this.dataurl).then(response => {
        this.title = response.data.title;
        this.desc = response.data.desc;
        this.date = response.data.date;
        this.id = response.data.id;
        if (response.data.categories != null)
          this.categories = response.data.categories.split(",");

        axios
          .get("http://localhost:8000/taskcontrib/?id=" + this.id)
          .then(resp => {
            this.contribs = resp.data;
            this.contribs.forEach(element => {
              axios.get(element.user.replace("/auth/", "/")).then(presp => {
                element.user = presp.data;
              });
            });
            this.ownerId = this.$store.state.userlogged.pk;
          });
      });
    },
    csrf() {
      return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken"))
        .split("=")[1];
    },
    contribute() {
      console.log(this.dataurl);
      const postData = {
        task: this.dataurl,
        progress: 1,
        user:
          "http://localhost:8000/auth/users/" +
          this.$store.state.userlogged.pk +
          "/"
      };

      axios({
        method: "post",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          Accept: "application/json",
          "X-CSRFToken": this.csrf()
        },
        url: "http://localhost:8000/taskcontrib/",
        data: JSON.stringify(postData)
      }).then(response => {
        this.$router.go();
      });
    },
    ToggleDeleteDialog() {
      this.$refs.deleteD.Toggle();
    },
    ToggleEditDialog() {
      this.$refs.editD.Toggle();
    }
  }
};
</script>

<style>
.task {
  background: #34495e !important ;
}
.task .body {
  background: white !important;
  color: black;
}
.status {
  position: absolute;
  left: 0;
  height: 100%;
  background: rgb(218, 85, 85);
  width: 8px;
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
}

.task-chip {
  justify-content: center;
  text-align: center;
}
</style>
