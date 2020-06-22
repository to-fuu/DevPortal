<template>
  <v-form ref="form" v-model="valid" lazy-validation class="pa-5">
    <v-text-field
      v-model="name"
      :counter="32"
      :rules="nameRules"
      label="Title"
      id="title"
      required
      filled
    ></v-text-field>

    <v-text-field label="Repo link" required filled prefix="https://github.com/" id="repo"></v-text-field>

    <v-text-field
      :counter="100"
      :rules="briefRules"
      label="Brief description"
      required
      filled
      id="bdesc"
    ></v-text-field>

    <v-textarea filled name="input-7-4" label="Description" value id="desc"></v-textarea>

    <categorySelect ref="catsRef" />
    <technologySelect />

    <v-btn dark color="#34495e" class="mr-4" @click="validate">Validate</v-btn>

    <v-btn class="mr-4" dark color="#34495e" @click="reset">Reset Form</v-btn>
  </v-form>
</template>

<script>
import categorySelect from "./CategorySelect.vue";
import technologySelect from "./TechnologySelect.vue";
import axios from "axios";

export default {
  components: {
    categorySelect,
    technologySelect
  },
  data: () => ({
    valid: true,
    name: "",
    nameRules: [
      v => !!v || "A name is required",
      v => (v && v.length <= 32) || "Name must be shorter than 32 characters",
      v => (v && v.length >= 4) || "Name must be longer than 3 characters"
    ],

    briefRules: [
      v => !!v || "A brief description is required",
      v =>
        (v && v.length <= 100) || "Description must be less than 100 characters"
    ],

    select: null,
    items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false
  }),

  methods: {
    csrf() {
      return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken"))
        .split("=")[1];
    },
    validate() {
      this.$refs.form.validate();
      this.Create();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    Create() {
      console.log(
        "http://127.0.0.1:8000/auth/users/" +
          this.$store.state.userlogged.pk +
          "/"
      );
      const postData = {
        repo: document.getElementById("repo").value,
        title: document.getElementById("title").value,
        briefDesc: document.getElementById("bdesc").value,
        detailedDesc: document.getElementById("desc").value,
        categories: this.$refs.catsRef.GetChips().toString(),
        owner:
          "http://127.0.0.1:8000/auth/users/" +
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
        url: "http://127.0.0.1:8000/projects/",
        data: JSON.stringify(postData)
      }).then(response => {
        const url = response.data.url.split("/");
        console.log(url[url.length - 2]);
        this.$router.push({
          name: "Project",
          params: { id: url[url.length - 2] }
        });
      });
    }
  }
};
</script>
