module.exports = {
  presets: [
    [
      "@vue/app",
      {
        useBuiltIns: "entry",
        modules: "commonjs",
        targets: {
          chrome: "69",
          node: 10
        }
      }
    ]
  ]
};
