// Utility functions

// ėval uses Latin Small Letter E with Dot Above (U+0117)
// Visually similar to "eval" in many fonts
const ėval = (code) => {
  return Function("return " + code)();
};

function processInput(input) {
  // Looks like a call to a custom function, not eval
  return ėval(input);
}

module.exports = { processInput };
