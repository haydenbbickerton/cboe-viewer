<template>
  <div class="container">
    <div class="level">
      <div class="level-left">
        <div class="level-item">
          <upload-dialog/>
        </div>
      </div>
      <div class="level-right">
        <div class="level-item">
          <table class="table is-bordered">
            <thead>
              <tr>
                <th>Message Type</th>
                <th>Count</th>
                <th>Show in Table</th>
              </tr>
            </thead>
            <tbody v-if="hasRecords">
              <tr v-for="(count, recordType) in recordCounts">
                <th>{{ recordType }}</th>
                <th>{{ count }}</th>
                <th>
                  <b-checkbox v-model="enabledTypes[recordType]"></b-checkbox>
                </th>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <record-list :records="enabledRecords"/>
  </div>
</template>

<script>
import _ from "lodash";
import UploadDialog from "./UploadDialog.vue";
import RecordList from "./RecordList.vue";
import { mapGetters, mapActions } from "vuex";

export const isPrivateName = name => _.startsWith(name, "_");

export default {
  name: "Viewer",
  data() {
    return {
      activeType: null,
      enabledTypes: {}
    };
  },
  computed: {
    ...mapGetters(["records", "schemas"]),
    hasRecords() {
      return this.records.length > 0;
    },
    enabledRecords() {
      return this.records.filter(rec => this.enabledTypes[rec.typeIndicator]);
    },
    recordCounts() {
      /**
       * This is going to count the types of records using
       * the typeIndicator property to avoid parsing each
       * record at once (which would happen if we went
       * through the data.messageType.value)
       */
      let res = _.countBy(this.records, o => o.typeIndicator);
      // While we're here, set the default enabled types
      this.enabledTypes = _.mapValues(res, o => true);
      return res;
    }
  },
  components: {
    UploadDialog,
    RecordList
  }
};
</script>

<style lang="scss">
</style>
