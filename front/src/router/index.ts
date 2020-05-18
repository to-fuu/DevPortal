import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "@/components/Login.vue";
import Register from "@/components/SignUp.vue";
import ResetPass from "@/components/RecoverPassword.vue";
import HelloWorld from "@/components/HelloWorld.vue";
import CreateProjPage from "@/components/CreatePage.vue";
import ProjectPage from "@/components/ProjectPage.vue";
import ProjectPageDetails from "@/components/ProjectPage-Details.vue";
import EditProject from "@/components/EditProjectPage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/Home",
    name: "Home",
    component: HelloWorld
  }, {
    path: "/login",
    name: "Login",
    component: Login
  }, {
    path: "/register",
    name: "Register",
    component: Register
  }, {
    path: "/login/recover",
    name: "Recover password",
    component: ResetPass
  }, {
    path: "/projects/create",
    name: "Create Project",
    component: CreateProjPage
  },
  {
    path: "/projects/:id",
    name: "Project",
    component: ProjectPage
  },
  {
    path: "/projects/:id/details",
    name: "Details",
    component: ProjectPageDetails
  },
  {
    path: "/projects/:id/Edit",
    name: "Edit",
    component: EditProject
  },

  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  routes
});

export default router;
