<template>
  <v-container class="fill-height" fluid style="background: #e2e2e4">
    <v-row align="center" justify="center">
      <v-card class="mx-auto" max-width="344" elevation="24" dark style="background:#34495e">
        <v-list-item three-line>
          <v-list-item-content>
            <div class="overline mb-4">WELCOME BACK</div>

            <v-form>
              <v-text-field v-model="username" :counter="10" label="Username" required></v-text-field>
              <v-text-field
                v-model="email"
                :rules="[rules.emailMatch]"
                :counter="10"
                label="Email"
                required
              ></v-text-field>

              <v-text-field
                v-model="password"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[rules.required, rules.min]"
                :type="show ? 'text' : 'password'"
                name="input-10-1"
                label="Password"
                hint="At least 8 characters"
                counter
                @click:append="show = !show"
              ></v-text-field>
            </v-form>
            <div class="overline">Forgot your password?</div>
          </v-list-item-content>
        </v-list-item>

        <v-card-actions>
          <v-container fluid class="mb-0 py-0">
            <v-row align="center" justify="center">
              <v-btn block light @click="login">LOGIN</v-btn>
            </v-row>
            <v-row align="center" justify="center" class="mt-2">
              <v-btn block light @click="logout">SIGN UP</v-btn>
            </v-row>
          </v-container>
        </v-card-actions>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
axios.defaults.withCredentials = true;
export default {
  data() {
    return {
      show: false,
      username: "util1",
      email: "chebbi.ala@outlook.com",
      password: "b00bsarelove",
      rules: {
        required: value => !!value || "Required.",
        min: v => v.length >= 8 || "Min 8 characters",
        emailMatch: () => "The email and password you entered don't match"
      }
    };
  },
  created() {
    if (this.$store.state.token) this.$router.push("/");
  },
  methods: {
    csrf() {
      return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken"))
        .split("=")[1];
    },
    login() {
      const postData = {
        password: this.password,
        username: this.username,
        email: this.email
      };
      axios({
        method: "post",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          Accept: "application/json",
          "X-CSRFToken": this.csrf()
        },
        url: "http://localhost:8000/rest-auth/login/ ",
        data: JSON.stringify(postData)
      }).then(response => {
        console.log(response.data);
        if (this.$store.state.token != response.data.key)
          axios.get("http://localhost:8000/rest-auth/user/").then(res => {
            axios
              .get("http://localhost:8000/profiles/?id=" + res.data.pk)
              .then(pres => {
                console.log(pres.data[0]);
                this.$store.dispatch("saveToken", response.data.key);
                this.$store.dispatch("saveUserLogged", res.data);
                this.$store.dispatch("saveUserProfile", pres.data[0]);
                this.$router.push("/");
              });
          });
      });
    },
    logout() {
      axios.get("http://localhost:8000/rest-auth/logout/").then(res => {
        console.log(res);
        this.$store.dispatch("saveToken", "");
        this.$store.dispatch("saveUserLogged", "");
        this.$store.dispatch("saveUserProfile", "");
      });
    }
  }
};
</script>
