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
    <v-list dense nav class="py-0" style="height:100%">
      <v-list-item-group color="indigo" active-class="border">
        <v-list-item two-line :class="miniVariant && 'px-0'">
          <v-list-item-content>
            <v-list-item-title>PORTAIL</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>

      <v-divider></v-divider>
      <div v-for="item in items" :key="item.title">
        <v-list-item link :to="{ name: item.link }" v-if="!item.disabled">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </div>

      <v-divider></v-divider>

      <v-list-item v-if="this.$store.state.token==''" link :to="{ name: 'Login' }">
        <v-list-item-icon>
          <v-icon>mdi-login</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>Login</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item v-if="this.$store.state.token==''" link :to="{ name: 'Register' }">
        <v-list-item-icon>
          <v-icon>mdi-account-plus</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>Register</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item v-if="this.$store.state.token!=''" link :to="{ name: 'Logout' }">
        <v-list-item-icon>
          <v-icon>mdi-logout</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>Logout</v-list-item-title>
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
          :to="{ name: item.link, params: { id: $route.params.id } }"
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
        { title: "Home", icon: "mdi-home", link: "Home", disabled: false },
        {
          title: "Profile",
          icon: "mdi-account",
          link: "MyProfile",
          disabled: this.$store.state.userlogged === ""
        },
        {
          title: "Create",
          icon: "mdi-plus",
          link: "Create Project",
          disabled: this.$store.state.userlogged === ""
        },
        {
          title: "My projects",
          icon: "mdi-format-list-bulleted",
          link: "MyProjs",
          disabled:
            this.$store.state.userProfile.userType == 1 ||
            this.$store.state.userlogged === ""
        },
        {
          title: "Events",
          icon: "mdi-calendar",
          link: "Events",
          disabled: false
        }
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

<style>
.v-list-item--active::before {
  background-color: transparent !important;
  background: transparent !important;
}
</style>
