Vue.use(vuetify)
Vue.component('RedButton', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<v-btn color="primary" class="mb-2" style="background: #ed120b; color: white"" large>DEVIS GRATUIT</v-btn>'
});