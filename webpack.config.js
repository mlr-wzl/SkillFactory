const HtmlWebpackPlugin = require('html-webpack-plugin');

//module.exports = {
//    mode: 'development',
//    entry: './src/index.js',
//   devServer: {
//     hot: "only",
//   },
//    plugins: [
//           new HtmlWebpackPlugin({
//        title: 'Development',
//      }),
//    ],
//    output: {
//      filename: 'main.js',
//    },
//  };
var config = {
     entry: './src/index.js',
};

  module.exports = (env, argv) => {
      plugins: [
           new HtmlWebpackPlugin({
        title: 'Development',
        }),
    ];
    output: {
      filename: 'main.js';
        };
  if (argv.mode === 'development') {
    config.devtool = 'source-map';
       devServer: {
     hot: "only";
   };

  }

  if (argv.mode === 'production') {

  }

  return config;
};
