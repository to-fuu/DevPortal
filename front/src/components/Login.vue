<template>
  <v-container class="fill-height" fluid style="background: #e2e2e4">
    <v-row align="center" justify="center">
      <v-card class="mx-auto" max-width="344" elevation="24" dark style="background:#34495e">
        <v-list-item three-line>
          <v-list-item-content>
            <div class="overline mb-4">WELCOME BACK</div>

            <v-form>
              <v-text-field
                v-model="firstname"
                :rules="nameRules"
                :counter="10"
                label="Username"
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
              <v-btn block light>LOGIN</v-btn>
            </v-row>
            <v-row align="center" justify="center" class="mt-2">
              <v-btn block light>SIGN UP</v-btn>
            </v-row>
          </v-container>
        </v-card-actions>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      show: false,
      password: "Password",
      rules: {
        required: value => !!value || "Required.",
        min: v => v.length >= 8 || "Min 8 characters",
        emailMatch: () => "The email and password you entered don't match"
      }
    };
  }
};
</script>