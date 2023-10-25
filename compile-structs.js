var fs = require("fs");
var YAML = require("yamljs");
var KaitaiStructCompiler = require("kaitai-struct-compiler");

const languages = ["javascript", "python"];

var srcYaml = fs.readFileSync("./structs/cboe.ksy", "utf8");
var parsedYaml = YAML.parse(srcYaml);

var compiler = new KaitaiStructCompiler();

for (const lang of languages) {
  compiler
    .compile(lang, parsedYaml, false)
    .then(files => {
      for (const [key, value] of Object.entries(files)) {
        const fname = `./structs/compiled/${key}`;
        fs.writeFileSync(fname, value, "utf8");
        console.log(`${lang} parser created at ${fname}`);
      }
    })
    .catch(function(err) {
      console.log(err);
    });
}
