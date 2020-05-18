<template>
  <v-expansion-panels dark multiple>
    <v-expansion-panel class="task">
      <v-expansion-panel-header>
        {{title}}
        <div class="status"></div>
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        {{desc}}
        <br />
        <div class="mt-2">
          <v-chip
            :v-for="categories!=='null'"
            class="mx-2 task-chip"
            v-for="(cat, categories) in categories"
            light
            label
            small
            :key="categories"
          >{{cat}}</v-chip>

          <v-btn
            light
            color="error"
            small
            class="float-right mx-1"
            @click.stop="ToggleDeleteDialog()"
          >Delete</v-btn>
          <v-btn light small class="float-right mx-1" @click.stop="ToggleEditDialog()">Edit</v-btn>
        </div>
      </v-expansion-panel-content>
    </v-expansion-panel>

    <deleteD ref="deleteD" type="task" :title="title" :url="dataurl" />
    <editD
      ref="editD"
      :url="dataurl"
      :title="title"
      :taskData="{ title:this.title,desc:this.desc,date:this.date }"
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
  props: ["dataurl"],
  data: () => ({
    title: "",
    desc: "",
    date: "",
    categories: "",
    dialog: false
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
        if (response.data.categories != null)
          this.categories = response.data.categories.split(",");
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