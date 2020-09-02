var ExtractTextPlugin = require('extract-text-webpack-plugin');
var UglifyJsPlugin = require('uglifyjs-webpack-plugin')
var webpack = require('webpack');
var path = require('path');

module.exports = function(env) {
  env = env || {};
  var _env = env.NODE_ENV ? env.NODE_ENV : 'production';

  return {
    entry: {
      app: './website/static/js/src/app.js',
    },
    output: {
      filename: 'js/build/[name].bundle.js',
      path: _env === 'dev' ? path.resolve(__dirname, './static/') : path.resolve(__dirname, './website/static/')
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          loader: 'babel-loader',
          query: {
            presets: ['react'],
            plugins:['transform-object-rest-spread']
          }
        },
        {
          test: /\.(ttf|otf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
          loader: 'file-loader',
          options: {
            name: '[name].[ext]',
            publicPath: 'fonts',
            outputPath: 'css/build/fonts'
          }
        },
        {
          test: /\.scss$|\.css$/,
          loader: ExtractTextPlugin.extract([
            {
              loader: 'css-loader',
              options: {
                minimize: true
              }
            },
            {
              loader: 'sass-loader',
              // TODO: implement something like this:
              // https://github.com/webpack-contrib/sass-loader/issues/218#issuecomment-287535193
              /*options: {
                data: '@import shared/vars;',
                // includePaths:
              }*/
            }
          ])
        }
      ]
    },
    plugins: [
      new ExtractTextPlugin("css/build/styles.bundle.css"),
      new webpack.DefinePlugin({
        'process.env': {
          'NODE_ENV': JSON.stringify('production')
        }
      }),
      new UglifyJsPlugin()
    ]
  }
}
