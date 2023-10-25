<template>
  <div class="block">
    <div class="raw-message">
      <div class="is-flex">
        <span v-for="([name, field], index) of fields" v-bind:key="name">
          <letters :content="field.value" :color="colors[index % colors.length]"/>
        </span>
      </div>
    </div>
    <hr>
    <table class="table is-bordered message-fields">
      <tbody>
        <tr v-for="([name, field], index) of fields" v-bind:key="name">
          <th class="has-text-centered">{{ name }}</th>
          <th>
            <letters :content="field.value" :color="colors[index % colors.length]"/>
          </th>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import filters from "@/filters";
import CircularJSON from "circular-json-es6";
import swatches from "@/colors";
import _ from "lodash";
import Vue from "vue";

Vue.component("letters", {
  props: ["content", "color"],
  template: `
    <div class="letters"><span><i
      v-for="letter of content"
      v-bind:style="{'background-color': color}"
    >{{letter}}</i></span></div>
  `
});

export default {
  name: "Block",
  data() {
    return {
      colors: swatches
    };
  },
  computed: {
    fields() {
      return _.chain(this.record)
        .thru(filters.omitPrivate)
        .mapValues(filters.omitPrivate)
        .toPairs()
        .sortBy(o => o.offset)
        .value();
    }
  },
  props: ["record"]
};
</script>

<style lang="scss">
.raw-message {
  display: grid;
  div {
    overflow: auto;
    overflow-y: hidden;
    white-space: nowrap;
  }
}
table.message-fields {
  th {
    padding: 0;
    .letters {
      padding: 0.25em 0.5em;
    }
  }
}

.letters {
  font-family: "Source Code Pro", monospace;
  background: #efefef;
  padding: unset;

  span {
    padding: unset;
    line-height: 25px;
    text-align: center;
    letter-spacing: unset;
    text-rendering: optimizeLegibility;
    white-space: pre;
  }

  i {
    font-style: normal;
    font-weight: 600;
    white-space: nowrap;
    display: inline-block;
    margin-right: 1px;
    padding: 0 5px;
    vertical-align: middle;
    height: 25px;
    width: 20px;
    color: white;
  }
}
</style>
