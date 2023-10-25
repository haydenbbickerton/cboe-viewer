<template>
  <section>
    <b-table
      :data="records ? records : []"
      ref="table"
      paginated
      per-page="25"
      detailed
      striped
      narrow
      icon-pack="fa"
      detail-key="idx"
      :loading="isLoading"
      :mobile-cards="false"
    >
      <template slot-scope="props">
        <b-table-column
          width="40"
          field="data.timestamp.value"
          label="Timestamp"
          sortable
        >{{ props.row.data.timestamp.value }}</b-table-column>

        <b-table-column
          field="data.messageType.value"
          label="Type"
          width="40"
          sortable
          centered
        >{{ props.row.data.messageType.value }}</b-table-column>

        <b-table-column field="raw" label="RAW">
          <code>{{ props.row.raw }}</code>
        </b-table-column>
      </template>

      <template slot="detail" slot-scope="props">
        <article>
          <RecordItem :record="props.row.data"/>
        </article>
      </template>

      <template slot="empty">
        <section class="section">
          <div class="content has-text-grey has-text-centered">
            <p>Please upload a file</p>
          </div>
        </section>
      </template>
    </b-table>
  </section>
</template>

<script>
import { mapGetters } from "vuex";

import RecordItem from "./RecordItem";

export default {
  name: "Record-List",
  props: ["records"],
  data() {
    return {
      showDetailIcon: true
    };
  },
  components: {
    RecordItem
  },
  computed: {
    ...mapGetters(["isLoading"]),
    currentRecords() {}
  }
};
</script>

<style lang="scss" scoped>
.table {
  table-layout: fixed;
}

.record {
  display: flex;
  min-height: 24px;
  box-sizing: border-box;
}
</style>
