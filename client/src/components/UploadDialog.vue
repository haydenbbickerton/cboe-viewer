<template>
  <b-field class="file">
    <b-upload v-model="file" @input="fileChanged" :loading="isLoading" native>
      <a class="button is-primary">
        <b-icon pack="fas" icon="upload"></b-icon>
        <span>Click to upload</span>
      </a>
    </b-upload>
    <template v-if="file">
      <span class="file-name">{{ file.name }}</span>
      <b-button type="is-danger" outlined @click="reset">Reset</b-button>
    </template>
  </b-field>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import { debug, isNullOrUndefined } from "util";

export default {
  data() {
    return {
      file: null
    };
  },
  computed: {
    ...mapGetters(["isLoading"])
  },
  methods: {
    reset() {
      this.file = null;
      this.$store.dispatch("setRecords", []);
      this.$store.dispatch("setLoading", false);
    },
    readBlob(blob, mode, ...args) {
      return new Promise(function(resolve, reject) {
        var reader = new FileReader();
        reader.onload = function() {
          resolve(reader.result);
        };
        reader.onerror = function(e) {
          reject(e);
        };
        reader["readAs" + mode[0].toUpperCase() + mode.substr(1)](
          blob,
          ...args
        );
      });
    },
    fileChanged(value) {
      if (isNullOrUndefined(value)) {
        this.reset();
      } else {
        this.readBlob(value, "ArrayBuffer")
          .then(res => {
            this.$store.dispatch("loadRecords", res);
          })
          .catch(err => {
            console.error(err);
            this.reset();
            this.$toast.open({
              duration: 5000,
              message: `File could not be parsed: ${err}`,
              position: "is-bottom",
              type: "is-danger"
            });
          });
      }
    },
    promptUpload() {
      this.$dialog.prompt({
        message: `Upload the file`,
        inputAttrs: {
          type: "file",
          required: true
        }
      });
    }
  }
};
</script>
