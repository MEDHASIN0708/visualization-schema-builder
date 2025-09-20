const Ajv = require("ajv");
const fs = require("fs");

const ajv = new Ajv({ allErrors: true });
const schema = JSON.parse(fs.readFileSync("./schema/visualization-schema.json", "utf8"));
const validate = ajv.compile(schema);

["./examples/example1.json", "./examples/example2.json"].forEach(file => {
  const data = JSON.parse(fs.readFileSync(file, "utf8"));
  const valid = validate(data);
  if (valid) {
    console.log(`${file} ✅ Valid`);
  } else {
    console.error(`${file} ❌ Invalid`, validate.errors);
  }
});
