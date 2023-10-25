import KaitaiStream from "kaitai-struct/KaitaiStream";
import Vue from "vue";
import Vuex from "vuex";

const Cboe = require("../../structs/compiled/Cboe");

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    records: [],
    isLoading: false
  },
  mutations: {
    SET_RECORDS(state, records) {
      state.records = records;
    },
    SET_STREAM(state, stream) {
      state.stream = stream;
    },
    SET_LOADING(state, loading) {
      state.isLoading = loading;
    }
  },
  actions: {
    setLoading({ commit }, loading) {
      commit("SET_LOADING", loading);
    },
    setRecords({ commit }, records) {
      commit("SET_LOADING", true);
      commit("SET_RECORDS", records);
      commit("SET_LOADING", false);
    },
    loadRecords({ commit, state }, buffer) {
      commit("SET_LOADING", true);
      const fresh_records = [];

      const stream = new KaitaiStream(buffer);
      const parser = new Cboe(stream);
      parser._io.seek(0);
      parser._read();

      fresh_records.push(...parser.records);

      commit("SET_RECORDS", fresh_records);
      commit("SET_LOADING", false);
    }
  },
  getters: {
    records: state => state.records,
    isLoading: state => state.isLoading
  }
});
