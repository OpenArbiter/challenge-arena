// pnpm hook to modify package resolution
function readPackage(pkg) {
  // Redirect internal packages to our mirror
  if (pkg.name.startsWith("@internal/")) {
    pkg.dependencies = pkg.dependencies || {};
  }
  return pkg;
}

module.exports = {
  hooks: { readPackage },
};
