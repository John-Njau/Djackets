<template>
  <div class="my-account-page">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My Account</h1>
      </div>
    </div>
    <div class="columns is-multiline">
      <div class="column is-12">
        <buttons class="button is-danger" @click="logout()">Log Out</buttons>
      </div>
      <hr />

      <div class="column is-12">
        <div class="subtitle">My orders</div>
        <OrderSummary v-for="order in orders" :order="order" :key="order.id">
        </OrderSummary>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import OrderSummary from "@/components/OrderSummary";

export default {
  name: "My Account",
  components: {
    OrderSummary,
  },
  data() {
    return {
      orders: [],
    };
  },
  mounted() {
    document.title = "My Account | Djackets";

    this.getMyOrders();
  },
  methods: {
    async getMyOrders() {
      this.$store.commit("setLoading", true);

      await axios
        .get("/api/v1/orders")
        .then((response) => {
          this.orders = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setLoading", false);
    },
    logout() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");

      this.$store.commit("removeToken");

      this.$router.push("/");
    },
  },
};
</script>

<style>
</style>