var windowUtilsJs = require("node-gyp-build")(__dirname);

function getWindowTitle(buffer) {
  return windowUtilsJs.getWindowTitle(buffer);
}

function allowWindowFullScreenTiling(buffer) {
  return windowUtilsJs.allowWindowFullScreenTiling(buffer);
}

module.exports = {
  getWindowTitle: getWindowTitle,
  allowWindowFullScreenTiling: allowWindowFullScreenTiling,
};
