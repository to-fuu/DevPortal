<template>
  <v-navigation-drawer
    v-model="drawer"
    :expand-on-hover="expandOnHover"
    :mini-variant="miniVariant"
    :right="right"
    :permanent="permanent"
    :src="bg"
    color="#34495e"
    absolute
    dark
    style="border-radius:0!important"
  >
    <v-list dense nav class="py-0">
      <v-list-item two-line :class="miniVariant && 'px-0'">
        <v-list-item-content>
          <v-list-item-title>PORTAIL</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list-item v-for="item in items" :key="item.title" link :to="{ name: item.link}">
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>

      <v-list-item link :to="{ name: 'Login'}">
        <v-list-item-icon>
          <v-icon>mdi-login</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>Login</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item link :to="{ name: 'Register'}">
        <v-list-item-icon>
          <v-icon>mdi-account-plus</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>Register</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <div v-if="$route.params.id">
        <v-list-item two-line :class="miniVariant && 'px-0'">
          <v-list-item-content>
            <v-list-item-title>Project Name</v-list-item-title>
            <v-list-item-subtitle>User</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item
          v-for="item in projectItems"
          :key="item.title"
          link
          :to="{ name: item.link, params: {id: $route.params.id }}"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </div>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      items: [
        { title: "Home", icon: "mdi-home", link: "Home" },
        { title: "Profile", icon: "mdi-account", link: "Profile" },
        { title: "Create", icon: "mdi-plus", link: "Create Project" },
        {
          title: "My projects",
          icon: "mdi-format-list-bulleted",
          link: "MyProjs"
        },
        { title: "Events", icon: "mdi-calendar", link: "Events" }
      ],
      projectItems: [
        { title: "Details", icon: "mdi-information-outline", link: "Details" },
        { title: "Code", icon: "mdi-code-tags", link: "Project" },
        { title: "Tasks", icon: "mdi-message-outline", link: "Project" },
        { title: "Forum", icon: "mdi-format-list-bulleted", link: "Forum" },
        { title: "Edit", icon: "mdi-circle-edit-outline", link: "Edit" }
      ],
      color: "primary",
      colors: ["primary", "blue", "success", "red", "teal"],
      right: false,
      permanent: true,
      miniVariant: false,
      expandOnHover: false,
      background: false
    };
  },
  computed: {
    bg() {
      return this.background
        ? "https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg"
        : undefined;
    }
  }
};
</script>

<style >
</style>