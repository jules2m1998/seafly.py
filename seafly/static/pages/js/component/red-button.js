
Vue.component('RedButton', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<v-btn color="primary" class="mb-2" :to="{name: \'devis\'}" large>DEVIS GRATUIT</v-btn>'
})