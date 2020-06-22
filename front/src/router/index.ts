import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/components/Index.vue";
import Login from "@/components/Login.vue";
import Logout from "@/components/Logout.vue";
import Register from "@/components/SignUp.vue";
import ResetPass from "@/components/RecoverPassword.vue";
import HelloWorld from "@/components/HelloWorld.vue";
import CreateProjPage from "@/components/CreatePage.vue";
import ProjectPage from "@/components/ProjectPage.vue";
import ProjectPageDetails from "@/components/ProjectPage-Details.vue";
import EditProject from "@/components/EditProjectPage.vue";
import Profile from "@/components/ProfilePage.vue";
import RandomProfile from "@/components/RandomProfilePage.vue";
import MyProjects from "@/components/MyProjs.vue";
import Forum from "@/components/ProjectForum.vue";
import ThreadView from "@/components/ProjectForumThread.vue";
import MyContribs from "@/components/MyContribs.vue";
import MySettings from "@/components/MySettings.vue";
import Search from "@/components/Search.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/logout",
    name: "Logout",
    component: Logout,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/login/recover",
    name: "Recover password",
    component: ResetPass,
  },
  {
    path: "/projects/create",
    name: "Create Project",
    component: CreateProjPage,
  },
  {
    path: "/projects/:id",
    name: "Project",
    component: ProjectPage,
  },
  {
    path: "/projects/:id/details",
    name: "Details",
    component: ProjectPageDetails,
  },
  {
    path: "/projects/:id/Edit",
    name: "Edit",
    component: EditProject,
  },
  {
    path: "/projects/:id/Forum",
    name: "Forum",
    component: Forum,
  },
  {
    path: "/projects/:id/Forum/Thread/:tid",
    name: "ThreadView",
    component: ThreadView,
  },
  {
    path: "/profile",
    name: "MyProfile",
    component: Profile,
  },
  {
    path: "/profile/contribs",
    name: "MyContribs",
    component: MyContribs,
  },
  {
    path: "/profile/settings",
    name: "MySettings",
    component: MySettings,
  },
  {
    path: "/profile/:id",
    name: "Profile",
    component: RandomProfile,
  },
  {
    path: "/profile/projects",
    name: "MyProjects",
    component: MyProjects,
  },
  {
    path: "/search/:q",
    name: "Search",
    component: Search,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
