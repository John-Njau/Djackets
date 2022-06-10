<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome to S/W Jackets</p>
        <p class="subtitle">The best jacket store online</p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
      <ProductCard
      
        v-for="product in latestProducts"
        :key="product.id"
        :product="product"
      >
      </ProductCard>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import axios from "axios";
import ProductCard from "@/components/ProductCard.vue";

export default {
  name: "HomeView",
  components: {
    ProductCard,
  },
  data() {
    return {
      latestProducts: [],
    };
  },
  mounted() {
    this.getLatestProducts();
    // page title
    document.title = "Home " + " | Djackets";
  },
  methods: {
    async getLatestProducts() {
      // loading bar
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/v1/latest-products")
        .then((response) => {
          this.latestProducts = response.data;
          // page title
          // document.title = 'Homepage ' + ' | Djackets'
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
