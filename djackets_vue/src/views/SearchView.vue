<template >
  <div class="page-search">
    <div class="columns is-multitline">
      <div class="column is-12">
        <h1 class="title">Search</h1>
        <h2 class="is-size-5 has-text-grey">Search term : "{{ query }}"</h2>
        <ProductCard
        v-for="product in products"
        :key="product.id"
        :product="product"
      >
      </ProductCard>
      </div>
      <!-- <ProductCard
        v-for="product in products"
        :key="product.id"
        :product="product"
      >
      </ProductCard> -->
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductCard from "@/components/ProductCard.vue";

export default {
  name: "Search",
  components: {
    ProductCard,
  },
  data() {
    return {
      products: [],
      query: "",
    };
  },
  mounted() {
    document.title = "Search" + " | Djackets";

    // getting information from the uri

    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);

    if (params.get("query")) {
      this.query = params.get("query");

      this.SearchedProducts();
    }
  },
  methods: {
    async SearchedProducts() {
      // loading bar
      this.$store.commit("setIsLoading", true);

      // use .post as the query is posted back to the server

      await axios
        .post("/api/v1/products/search/", {
          query: this.query,
        })
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>