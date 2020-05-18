<template>
  <v-form ref="form" v-model="valid" lazy-validation class="pa-5">
    <v-text-field
      :counter="32"
      :rules="nameRules"
      label="Title"
      required
      filled
      id="title"
      :value="projectName"
    ></v-text-field>

    <v-text-field disabled v-model="repo" id="repo" label="Repo link" required filled :value="repo"></v-text-field>

    <v-text-field
      :counter="100"
      :rules="briefRules"
      label="Brief description"
      id="bdesc"
      required
      filled
      :value="projectBriefDesc"
    ></v-text-field>

    <v-textarea filled name="input-7-4" id="desc" label="Description" :value="projectDesc"></v-textarea>

    <categorySelect />

    <v-btn dark color="#34495e" class="mr-4" @click="validate">Validate</v-btn>

    <v-btn class="mr-4" dark color="#34495e" @click="reset">Clear Form</v-btn>
    <v-btn
      class="mr-4"
      dark
      color="#34495e"
      :to="{ name: 'Project', params: {id: $route.params.id } }"
    >Cancel</v-btn>
    <v-btn class="mr-4" color="error" @click.stop="ToggleDeleteDialog()">Delete project</v-btn>
    <deleteD ref="deleteD" type="project" :title="projectName" :url="url" />
  </v-form>
</template>

<script>
import categorySelect from "./CategorySelect.vue";
import axios from "axios";
import deleteD from "./Delete/Dialog.vue";

export default {
  components: {
    categorySelect,
    deleteD
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
    checkbox: false,
    repo: "",
    url: "",
    projectName: "",
    projectBriefDesc: "",
    projectDesc: ""
  }),

  methods: {
    LoadProjectData() {
      axios
        .get("http://127.0.0.1:8000/projects/" + this.$route.params.id)
        .then(response => {
          this.repo = response.data.repo;
          this.url = response.data.url;
          this.projectName = response.data.title;
          this.projectBriefDesc = response.data.briefDesc;
          this.projectDesc = response.data.detailedDesc;
        });
    },
    validate() {
      if (this.$refs.form.validate()) this.Update();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    ToggleDeleteDialog() {
      this.$refs.deleteD.Toggle();
    },
    Update() {
      const postData = {
        repo: document.getElementById("repo").value,
        title: document.getElementById("title").value,
        briefDesc: document.getElementById("bdesc").value,
        detailedDesc: document.getElementById("desc").value,
        updatedAt: new Date().toISOString()
      };
      console.log(postData);
      axios({
        method: "put",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          Accept: "application/json"
        },
        url: this.url,
        data: JSON.stringify(postData)
      });
    }
  },
  mounted() {
    this.LoadProjectData();
  }
};
</script>