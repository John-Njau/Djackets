import { createStore } from "vuex";

export default createStore({
  // setting opp to vuex/state
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    token: "",
    isLoading: false,
  },
  getters: {},
  mutations: {
    // adding functionality to add to cart object vuex
    initializeStore(state) {
      if (localStorage.getItem("cart")) {
        state.cart = JSON.parse(localStorage.getItem("cart"));
      } else {
        localStorage.setItem("cart", JSON.stringify(state.cart));
      }
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(
        (i) => i.product.id === item.product.id
      );

      if (exists.length > 0) {
        exists[0].quantity =
          parseInt(exists[0].quantity) + parseInt(item.quantity);
      } else {
        state.cart.items.push(item);
      }

      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
    // setting a loading bar
    setIsLoading(state, status) {
      state.isLoading = status;
    },
  },
  actions: {},
  modules: {},
});
