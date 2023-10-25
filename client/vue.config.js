// vue.config.js
module.exports = {
  runtimeCompiler: true,
  chainWebpack: config => config.resolve.symlinks(false),

  configureWebpack: {
    devtool: "source-map",
    output: {
      //   libraryTarget: "commonjs"
      //   libraryExport: "default"
    }
  },
  publicPath: '',
  css: {
    sourceMap: true
  },

  parallel: false
};
