<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"
          ><strong>S/W Jackets</strong></router-link
        >
        <a
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/summer" class="navbar-item">Summer</router-link>
          <router-link to="/winter" class="navbar-item">Winter</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-light"
                >Login</router-link
              >
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart({{ cartTotalLength }}) </span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

  <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading' : $store.state.isLoading}" >
  <div class="lds-dual-ring"></div>
  </div>

    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-centered">Designed and Developed by John Njau <br> Copyright &copy; 2022</p>
    </footer>
  </div>
</template>

<script>
export default{
  data(){
    return {
      showMobileMenu: false,
      cart: {
        items: [],
        
      }
    }
  },
  // commit is used to call actions in mutations
  beforeCreate(){
    this.$store.commit('initializeStore')
  },
  // computed properties are used to calculate values, this add the number on the cart
  mounted(){
    this.cart = this.$store.state.cart
  },
  computed:{
    cartTotalLength(){
      let totalLength = 0;

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity;
      }

      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import "../node_modules/bulma";

.lds-dual-ring{
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after{
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #fff;
  border-color: #fff transparent #fff transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring{
  0%{
    transform: rotate(0deg);
  }
  100%{
    transform: rotate(360deg);
  }
}

.is-loading-bar{
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading{
    height: 80px;
  }
}
</style>

