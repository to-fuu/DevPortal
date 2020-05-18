<template>
  <v-combobox
    v-model="chips"
    :items="items"
    chips
    clearable
    label="Pick at least one category"
    multiple
    filled
    no-data
    required
    id="categoryCB"
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
      items: ["AI", "Game Dev", "WEB"]
    };
  },

  methods: {
    remove(item) {
      this.chips.splice(this.chips.indexOf(item), 1);
      this.chips = [...this.chips];
    },
    GetChips() {
      return this.chips;
    },
    LoadCategories() {
      axios.get("http://127.0.0.1:8000/categories/").then(response => {
        const techs = response.data;
        techs.forEach(element => {
          this.items.push(element.name);
        });
      });
    }
  },
  mounted() {
    this.LoadCategories();
  }
};
</script>