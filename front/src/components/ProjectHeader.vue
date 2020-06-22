<template>
  <v-card class="fill-height sharp-card pt-5" height="164" outlined tile>
    <v-list-item three-line>
      <v-list-item-content class="pl-5">
        <!-- <v-breadcrumbs class="px-0" :items="items"></v-breadcrumbs> -->
        <router-link :to="{ name: 'Profile', params: { id: user.pk } }">
          <v-list-item-subtitle style="text-transform:uppercase">{{user.username}}</v-list-item-subtitle>
        </router-link>

        <v-list-item-title class="headline font-weight-bold">
          {{ projectname }}
          <router-link
            :to="{ name: 'Edit', params: { id: $route.params.id } }"
            v-if="user.pk == this.$store.state.userlogged.pk"
          >
            <v-icon small class="pb-4 my-0">mdi-pencil-outline</v-icon>
          </router-link>
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-divider></v-divider>
    <Searchbar />

    <v-card-actions>
      <v-btn class="topmenu-btn" text :to="{ name: 'Details', params: { id: $route.params.id } }">
        <v-icon small class="mr-1">mdi-information-outline</v-icon>DETAILS
      </v-btn>
      <v-btn class="topmenu-btn" text :to="{ name: 'Project', params: { id: $route.params.id } }">
        <v-icon small class="mr-1">mdi-code-tags</v-icon>CODE
      </v-btn>
      <v-btn class="topmenu-btn" text :to="{ name: 'Forum', params: { id: $route.params.id } }">
        <v-icon small class="mr-1">mdi-message-outline</v-icon>FORUM
      </v-btn>
      <!-- <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn class="topmenu-btn" text v-on="on">
            <v-icon small class="mr-1">mdi-dots-horizontal</v-icon>More
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="(item, index) in moreItems" :key="index">
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>-->

      <v-divider vertical class="mx-2"></v-divider>

      <v-chip
        :v-for="categories !== 'undefined'"
        class="topmenu-chip mx-2"
        v-for="(cat, categories) in categories"
        :key="categories"
        dark
      >{{ cat }}</v-chip>
      <!-- <v-chip class="topmenu-chip topmenu-chip-small mx-2" dark>+</v-chip> -->
    </v-card-actions>
  </v-card>
</template>

<style>
.sharp-card {
  border-radius: 0px;
}
.topmenu-btn {
  min-width: 96px;
}
.topmenu-chip {
  width: 96px;
  border-radius: 4px !important;
  justify-content: center;
  background: #34495e !important;
}

.topmenu-chip-small {
  width: 48px;
}
</style>

<script>
import Searchbar from "./SearchBar.vue";

export default {
  components: {
    Searchbar
  },
  props: ["projectname", "categories", "user", "userid"],
  data: () => ({
    items: [
      {
        text: "Dashboard",
        disabled: false,
        href: "breadcrumbs_dashboard"
      },
      {
        text: "Link 1",
        disabled: false,
        href: "breadcrumbs_link_1"
      },
      {
        text: "Link 2",
        disabled: true,
        href: "breadcrumbs_link_2"
      }
    ],
    moreItems: [
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me 2" }
    ],
    taskDialog: false
  })
};
</script>
