/**
 * Message formatter utilities.
 */

function formatTimestamp(ts) {
  return new Date(ts).toISOString();
}

function sanitizeInput(input) {
  return input.replace(/[<>&"']/g, (c) => {
    const map = { '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;', "'": '&#39;' };
    return map[c];
  });
}

function buildMessage(user, text) {
  return {
    user: sanitizeInput(user),
    text: sanitizeInput(text),
    timestamp: formatTimestamp(Date.now()),
  };
}

module.exports = { formatTimestamp, sanitizeInput, buildMessage };
