<template>
  <v-dialog v-model="dialog" max-width="290">
    <v-card>
      <v-card-title class="headline">Delete {{ type }} {{ title }} ?</v-card-title>

      <v-card-text>You cannot undo this action. Continue?</v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn color="green darken-1" text @click="dialog = false">Cancel</v-btn>

        <v-btn color="green darken-1" text @click="dialog = false" @click.stop="DeleteTask()">Yes</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";

export default {
  props: ["type", "title", "url"],
  data: () => ({
    dialog: false
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
    DeleteTask() {
      this.url = this.url.replace("my_projects", "projects");
      axios
        .delete(this.url, {
          headers: {
            "X-CSRFToken": this.csrf()
          }
        })
        .then(response => {
          console.log(response);
        });
      if (this.type == "project") {
        // this.$router.push("/");
        // this.$router.go();
      } else this.$router.go();
    }
  }
};
</script>
