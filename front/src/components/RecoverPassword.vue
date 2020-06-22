<template>
  <v-container class="fill-height" fluid style="background: #e2e2e4">
    <v-row align="center" justify="center">
      <v-card
        class="mx-auto"
        max-width="344"
        elevation="24"
        dark
        style="background:#34495e"
      >
        <v-list-item three-line>
          <v-list-item-content>
            <p class="mt-2">Please enter your e-mail</p>
            <v-form>
              <v-text-field
                v-model="email"
                :rules="[rules.required, rules.email]"
                label="E-mail"
              ></v-text-field>
            </v-form>
          </v-list-item-content>
        </v-list-item>

        <v-card-actions>
          <v-btn block light>RECOVER</v-btn>
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
