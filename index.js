var windowUtilsJs = require("node-gyp-build")(__dirname);

function getWindowTitle(buffer) {
  return windowUtilsJs.getWindowTitle(buffer);
}

module.exports = {
  getWindowTitle: getWindowTitle,
};
