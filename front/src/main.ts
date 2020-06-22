import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import "vuetify/dist/vuetify.min.css";
import Navigation from "./components/Navigation.vue";
import ProjectHeader from "./components/ProjectHeader.vue";
import taskview from "./components/TaskView.vue";
import ProjectPage from "./components/ProjectPage.vue";
import CreatePage from "./components/CreatePage.vue";
import sourcecode from "./components/SourceCode.vue";
import pageHeader from "./components/NormalHeader.vue";
import profileHeader from "./components/ProfileHeader.vue";
import CreateForm from "./components/CreateForm.vue";
import EditProjForm from "./components/EditProjectForm.vue";
// import store from "./store";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);
Vue.use(vuetify);

Vue.config.productionTip = false;

Vue.component("nav-drawer", Navigation);
Vue.component("proj-header", ProjectHeader);
Vue.component("v-task", taskview);
Vue.component("v-page", ProjectPage);
Vue.component("v-source", sourcecode);
Vue.component("create-page", CreatePage);
Vue.component("page-header", pageHeader);
Vue.component("profile-header", profileHeader);
Vue.component("create-form", CreateForm);
Vue.component("edit-project-form", EditProjForm);

const store = new Vuex.Store({
  state: {
    userlogged: "",
    userProfile: "",
    token: "",
  },
  mutations: {
    saveUserLogged(state, loggedUser) {
      state.userlogged = loggedUser;
    },
    saveUserProfile(state, userProfile) {
      state.userProfile = userProfile;
    },
    saveToken(state, token) {
      state.token = token;
    },
  },
  actions: {
    saveUserLogged(context, loggedUser) {
      context.commit("saveUserLogged", loggedUser);
    },
    saveUserProfile(context, userProfile) {
      context.commit("saveUserProfile", userProfile);
    },
    saveToken(context, token) {
      context.commit("saveToken", token);
    },
  },
  plugins: [createPersistedState()],
});

new Vue({
  router,
  vuetify,
  store: store,
  render: (h) => h(App),
}).$mount("#app");
