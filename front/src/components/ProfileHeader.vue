<template>
  <v-card class="fill-height sharp-card pt-5" min-height="200" max-height="234" outlined tile>
    <v-flex class="flex-row d-flex">
      <div class="mx-5" style="position:relative">
        <v-avatar size="128">
          <v-img :src="profile.photo"></v-img>
        </v-avatar>

        <v-avatar v-if="isAdmin===true" size="30" class="avatar-badge">
          <v-icon dark small>mdi-account-cog</v-icon>
        </v-avatar>
      </div>

      <v-col class="d-flex flex-column mx-2">
        <span>
          <h3 style="text-transform:uppercase">{{user.username }}</h3>
          {{user.first_name}}
          {{user.last_name}}
        </span>
        <span>
          <span class="title">{{projects}}</span> projects
          <span style="display:inline-block;width:30px;"></span>
          <span class="title">{{profile.point}}</span>
          points
        </span>
        <div>
          <v-chip depressed class="pa-2 mt-2 mr-2" small draggable color="primary">
            <span>{{getUserType()}}</span>
          </v-chip>

          <v-chip v-if="isAdmin" depressed class="pa-2 mt-2 mr-2" small draggable color="primary">
            <span>Admin</span>
          </v-chip>
        </div>
      </v-col>
    </v-flex>

    <v-divider class="mt-5"></v-divider>

    <v-card-actions>
      <v-btn class="topmenu-btn" text :to="{ name: 'MyProfile'}">
        <v-icon small class="mr-1">mdi-information-outline</v-icon>OVERVIEW
      </v-btn>
      <v-btn class="topmenu-btn" text :to="{ name: 'MyProjects'}">
        <v-icon small class="mr-1">mdi-code-tags</v-icon>PROJECTS
      </v-btn>
      <v-btn v-if="showSettings" class="topmenu-btn" text :to="{ name: 'MySettings'}">
        <v-icon small class="mr-1">mdi-cog</v-icon>SETTINGS
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<style>
.sharp-card {
  border-radius: 0px;
}

.header {
  display: flex;
  justify-content: flex-end;
  align-content: flex-end;
}
.header-title {
  vertical-align: bottom;
}

.avatar-badge {
  position: absolute;
  bottom: 7px;
  right: 5px;
  background-color: #2196f3;
  border: 3px solid white !important;
}
</style>

<script>
export default {
  props: ["profile", "user", "projects", "isAdmin", "showSettings"],
  data: () => ({}),
  methods: {
    getUserType() {
      switch (this.profile.userType) {
        case 1:
          return "Viewer";
        case 2:
          return "Developer";
        case 3:
          return "Instructor";
        case 4:
          return "Organiaztion";
      }
    }
  }
};
</script>
