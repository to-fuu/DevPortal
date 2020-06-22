<template>
  <v-container class="fill-height" fluid style="background: #e2e2e4">
    <v-row align="center" justify="center">
      <v-card class="mx-auto" max-width="344" elevation="24" dark style="background:#34495e">
        <v-list-item three-line>
          <v-list-item-content>
            <div class="overline mb-4">SIGN UP</div>
            <p>Fill the fields below to join</p>

            <v-form>
              <v-text-field
                v-model="username"
                :rules="nameRules"
                :counter="10"
                label="Username"
                required
              ></v-text-field>

              <v-text-field v-model="email" :rules="[rules.required, rules.email]" label="E-mail"></v-text-field>

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

              <v-text-field
                :rules="[rules.required, rules.min]"
                :type="show ? 'text' : 'password'"
                v-model="password2"
                name="input-10-2"
                label="Retype password"
                hint="Must match password"
              ></v-text-field>
            </v-form>
            <div class="overline">Have an account already?</div>
          </v-list-item-content>
        </v-list-item>

        <v-card-actions>
          <v-container fluid class="mb-0 py-0">
            <v-row align="center" justify="center">
              <v-btn block light @click.stop="Register">REGISTER</v-btn>
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
      username: "",
      password: "",
      password2: "",
      email: "",
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
    Register() {
      axios("http://localhost:8000/rest-auth/", {
        method: "post",
        data: {
          username: this.username,
          email: this.email,
          password1: this.password,
          password2: this.password2
        },
        headers: {
          "X-CSRFToken": this.csrf()
        }
      })
        .then(pres => {
          this.$router.push("/Login");
        })
        .catch(error => {
          console.log(error.response);
        });
    }
  }
};
</script>
