<template>
  <v-dialog v-model="dialog" max-width="500" class="pa-3">
    <v-card>
      <v-card-title class="headline">Add new task</v-card-title>
      <v-divider></v-divider>

      <v-card-text class="mt-3">
        <v-form v-on:submit.prevent="Update()" id="addTask-form">
          <v-text-field filled label="Task name" id="title" :value="taskData.title"></v-text-field>
          <v-text-field filled label="Task description" id="desc" :value="taskData.desc"></v-text-field>
          <v-menu
            ref="menu"
            v-model="menu"
            :close-on-content-click="false"
            :return-value.sync="taskData.date"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                id="date"
                v-model="date"
                label="End date"
                append-icon="mdi-calendar"
                readonly
                filled
                :value="taskData.date"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker no-title scrollable>
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
              <v-btn text color="primary" @click="$refs.menu.save(date)">OK</v-btn>
            </v-date-picker>
          </v-menu>
          <!-- <categorySelect /> -->
          <technologySelect />
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn color="green darken-1" text @click="dialog = false">Cancel</v-btn>

        <v-btn
          color="green darken-1"
          text
          @click="dialog = false"
          form="addTask-form"
          type="submit"
        >Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";
import technologySelect from "../TechnologySelect.vue";

export default {
  components: {
    technologySelect
  },
  props: ["title", "taskData", "url"],
  data: () => ({
    dialog: false,
    menu: false,
    date: new Date().toISOString().substr(0, 10)
  }),
  methods: {
    Toggle() {
      this.dialog = !this.dialog;
    },
    csrf() {
      return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken"))
        .split("=")[1];
    },
    Update() {
      const postData = {
        title: document.getElementById("title").value,
        desc: document.getElementById("desc").value,
        date: document.getElementById("date").value
      };
      console.log(postData);
      axios({
        method: "put",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          Accept: "application/json",
          "X-CSRFToken": this.csrf()
        },
        url: this.url,
        data: JSON.stringify(postData)
      }).then(response => {
        this.$router.go();
      });
    }
  }
};
</script>
