# Visualization Schema Builder

A simplified visualization grammar inspired by [Vega-Lite](https://github.com/vega/vega-lite).  
This project defines a **JSON Schema** for describing simple visualizations and layouts, provides **example JSON specifications**, validates them using **Ajv (JavaScript)**, and includes a **Python builder DSL** with unit tests.

---

## ✨ Features
- **JSON Schema** for:
  - `visualization`: { type, mark ∈ {bar, line, point, area}, encoding: {x,y,color} }
  - `layout`: { type, direction ∈ {vertical,horizontal}, gap, children }
  - Schema constraints:
    - Requires at least one of `x` or `y`
    - Layouts must have at least one child
    - Forbids unknown extra properties
- **Examples**:
  - `example1.json`: single bar chart
  - `example2.json`: vertical layout with line + area charts
- **JavaScript Validation**: uses Ajv to validate examples against the schema
- **Python Builder DSL**: classes to build visualizations and layouts fluently
- **Unit Tests**:
  - Positive tests: builder output matches examples
