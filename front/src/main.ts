import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import 'vuetify/dist/vuetify.min.css';
import Navigation from "./components/Navigation.vue";
import ProjectHeader from "./components/ProjectHeader.vue";
import taskview from "./components/TaskView.vue";
import ProjectPage from "./components/ProjectPage.vue";
import CreatePage from "./components/CreatePage.vue";
import sourcecode from "./components/SourceCode.vue";
import pageHeader from "./components/NormalHeader.vue";
import CreateForm from "./components/CreateForm.vue";
import EditProjForm from "./components/EditProjectForm.vue";

Vue.use(vuetify);

Vue.config.productionTip = false;


Vue.component("nav-drawer", Navigation);
Vue.component("proj-header", ProjectHeader);
Vue.component("v-task", taskview);
Vue.component("v-page", ProjectPage);
Vue.component("v-source", sourcecode);
Vue.component("create-page", CreatePage);
Vue.component("page-header", pageHeader);
Vue.component("create-form", CreateForm);
Vue.component("edit-project-form", EditProjForm);

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");
