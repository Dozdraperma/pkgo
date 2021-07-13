const path = require('path');

module.exports = {
  mode: "production", // "production" | "development" | "none"
  entry: "./index.js", // string | object | array
  output: {
    // options related to how webpack emits results
    path:path.resolve(__dirname, "dist"), // string (default)
    filename: "bundle.js", // string (default)
  },
  module: {
    rules: [
      {
        test: /\.m?js$/,
        exclude: /(node_modules)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
            plugins: ['@babel/plugin-syntax-top-level-await'],
          }
        }
      }
    ]
  }
}
