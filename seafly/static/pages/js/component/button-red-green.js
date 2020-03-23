Vue.component('button-red-green', {
  data: function () {
    return {
      count: 0
    }
  },
  template: `<div>
                <div class="button--contact mr-4 mt-4">
                    <red-button class="mr-2"></red-button>
                    <green-button/>
                </div>
            </div>`
});