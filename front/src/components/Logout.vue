<template>
  <div></div>
</template>

<script>
import axios from "axios";
axios.defaults.withCredentials = true;
export default {
  data() {
    return {};
  },
  created() {
    this.logout();
  },
  methods: {
    logout() {
      axios.get("http://localhost:8000/rest-auth/logout/").then(() => {
        this.$store.dispatch("saveToken", "");
        this.$store.dispatch("saveUserLogged", "");
        this.$store.dispatch("saveUserProfile", "");
        this.$router.push({ name: "Home" });
        this.$router.go();
      });
    }
  }
};
</script>
