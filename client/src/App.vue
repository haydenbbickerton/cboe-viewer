<template>
  <div id="app">
    <Viewer/>
  </div>
</template>

<script>
import Vue from "vue";
import Viewer from "./components/Viewer.vue";
import Buefy from "buefy";
import "buefy/dist/buefy.css";

Vue.use(Buefy);

export default {
  name: "app",
  components: {
    Viewer
  }
};
</script>

<style lang="scss">
code {
  white-space: pre;
  border: 1px solid #bbbbbb;
  color: #e42f53;
}
</style>
