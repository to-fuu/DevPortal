<template>
  <v-combobox
    v-model="chips"
    :items="items"
    chips
    clearable
    label="Pick at least one technology"
    multiple
    filled
    no-data
    required
  >
    <template v-slot:selection="{ attrs, item, select, selected }">
      <v-chip
        v-bind="attrs"
        :input-value="selected"
        close
        @click="select"
        @click:close="remove(item)"
      >
        <v-avatar class="accent white--text" left v-text="item.slice(0, 1).toUpperCase()"></v-avatar>

        <strong>{{ item }}</strong>&nbsp;
      </v-chip>
    </template>
  </v-combobox>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      chips: [],
      items: [
        "C",
        "C++",
        "C#",
        "JAVA",
        "PYTHON",
        "DJANGO",
        "VUEJS",
        "JAVASCRIPT",
        "IONIC"
      ]
    };
  },

  methods: {
    remove(item) {
      this.chips.splice(this.chips.indexOf(item), 1);
      this.chips = [...this.chips];
    },
    LoadTechnologies() {
      axios.get("http://127.0.0.1:8000/technologies/").then(response => {
        const techs = response.data;
        techs.forEach(element => {
          this.items.push(element.name);
        });
      });
    },
    GetChips() {
      return this.chips;
    }
  },
  mounted() {
    this.LoadTechnologies();
  }
};
</script>