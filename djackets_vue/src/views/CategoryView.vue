<template>
  <div class="page-category">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">{{category.name}}</h2>
        </div>
        <ProductCard
         
          v-for="product in category.products"
          :key="product.id"
          :product="product"
        >
        </ProductCard>
      </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
import ProductCard from "@/components/ProductCard.vue";

export default {
  name: "Category",
  data() {
    return {
      category: {
          products: []
      },
    };
  },
    components: {
    ProductCard,
  },
  mounted() {
    this.getCategory();
  },
  watch: {
    $route(to, from){
        if (to.name === 'Category') {
            this.getCategory();
        }
    }
  
  },
  methods:{


      async getCategory(){
          

        const categorySlug = this.$route.params.category_slug;
        this.$store.commit("setIsLoading", true);

        await axios
            .get(`/api/v1/products/${categorySlug}`)
            .then((response) => {
                this.category = response.data;
                // page title
                document.title = this.category.name + ' | Djackets'
            })
            .catch((error) => {
                console.log(error);

                toast({
                    message: "Error: " + error.response.data.message,
                    type: "is-danger",
                    duration: 2000,
                    position: "bottom-right",
                    dismissible: true,
                    animate: { in: "fadeIn", out: "fadeOut" },
                });
            });
        this.$store.commit("setIsLoading",false);

      }
  }
};
</script>