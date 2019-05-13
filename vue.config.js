var webpack = require('webpack')
const path = require('path')

module.exports = {
  configureWebpack: {
    plugins: [
      new webpack.ProvidePlugin({
        Vue: ['vue/dist/vue.esm.js', 'default'],
        jQuery: 'jquery',
        'window.jQuery': 'jquery',
        $: 'jquery',
        moment: 'moment',
      }),
    ],
  },

}
