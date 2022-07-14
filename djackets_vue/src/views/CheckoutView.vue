<template>
  <div class="checkout-page">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Checkout page</h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="cartTotalLength">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th></th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="item in cart.items" :key="item.product.id">
              <td>
                {{ item.product.name }}
              </td>
              <td>${{ item.product.price }}</td>
              <td>
                {{ item.quantity }}
              </td>
              <td>${{ getItemTotal(item).toFixed(2) }}</td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td colspan="2">Total</td>
              <td>{{ cartTotalLength }}</td>
              <td>${{ cartTotalPrice.toFixed(2) }}</td>
            </tr>
          </tfoot>
        </table>
        <p v-else>Nothing items to checkout. Add items to cart</p>
      </div>
      <div class="column is-12">
        <h1 class="subtitle">Shipping Details</h1>
        <small class="has-text-grey mb-4">* All fields are required</small>

        <div class="columns is-multiline">
          <div class="column is-6">
            <div class="field">
              <label class="label">First Name</label>
              <div class="control">
                <input class="input" type="text" v-model="first_name" />
              </div>
            </div>
            <div class="field">
              <label class="label">Last Name</label>
              <div class="control">
                <input class="input" type="text" v-model="last_name" />
              </div>
            </div>
            <div class="field">
              <label class="label">Email</label>
              <div class="control">
                <input class="input" type="email" v-model="email" />
              </div>
            </div>
            <div class="field">
              <label class="label">Phone no.</label>
              <div class="control">
                <input class="input" type="number" v-model="phone" />
              </div>
            </div>
          </div>
          <div class="column is-6">
            <div class="field">
              <label class="label">Address</label>
              <div class="control">
                <input class="input" type="text" v-model="address" />
              </div>
            </div>
            <div class="field">
              <label class="label">City</label>
              <div class="control">
                <input class="input" type="text" v-model="city" />
              </div>
            </div>
            <div class="field">
              <label class="label">Zipcode</label>
              <div class="control">
                <input class="input" type="text" v-model="zipcode" />
              </div>
            </div>
            <div class="field">
              <label class="label">State</label>
              <div class="control">
                <input class="input" type="text" v-model="state" />
              </div>
            </div>
          </div>
        </div>
        <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" :key="error">{{ error }}</p>
        </div>
        <hr />
        <div id="card-element" class="mb-5">
          <!-- A Stripe Element will be inserted here. -->
        </div>
        <template v-if="cartTotalLength" class="field">
          <hr />
          <div class="control">
            <button class="button is-dark" @click="submitForm">
              Pay with Stripe
            </button>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Checkout",
  data() {
    return {
      cart: {
        items: [],
      },
      stripe: {},
      card: {},
      first_name: "",
      last_name: "",
      email: "",
      phone: "",
      address: "",
      city: "",
      zipcode: "",
      state: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Checkout" + " | Djackets";

    this.cart = this.$store.state.cart;

    if (this.cartTotalLength > 0) {
      this.stripe = Stripe(
        "pk_test_51L9CbWCPyKFs9GTqeIi112xCv0VMMO6zZDgwgG2b24bpyPKnzB7BOkeJuwkOLTVEU1umftGorM91cXTpzwCOHvmG00HMytukm8"
      );
      const elements = this.stripe.elements();

      this.card = elements.create("card", { hidePostalCode: true });

      this.card.mount("#card-element");
    }
  },

  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    submitForm() {
      this.errors = [];

      if (this.first_name === "") {
        this.errors.push("The first name is missing");
      }

      if (this.last_name === "") {
        this.errors.push("The last name is missing");
      }

      if (this.email === "") {
        this.errors.push("Email is missing");
      }
      if (this.phone === "") {
        this.errors.push("Phone number is missing");
      }
      if (this.address === "") {
        this.errors.push("Address is missing");
      }
      if (this.city === "") {
        this.errors.push("City is missing");
      }
      if (this.zipcode === "") {
        this.errors.push("Zipcode is missing");
      }
      if (this.state === "") {
        this.errors.push("State is missing");
      }

      if (!this.errors.length) {
        this.$store.commit("setIsLoading", true);

        this.stripe.createToken(this.card).then((result) => {
          if (result.error) {
            this.$store.commit("setIsLoading", false);

            this.errors.push(
              "Something went wrong with stripe. Please try again."
            );

            console.log(result.error.message);
          } else {
            this.stripeTokenHandler(result.token);
          }
        });
      }
    },
    async stripeTokenHandler(token) {
      const items = [];

      for (let i = 0; i < this.cart.items.length; i++) {
        const item = this.cart.items[i];
        const obj = {
          product: item.product.id,
          quantity: item.quantity,
          price: item.product.price * item.quantity,
        };

        items.push(obj);
      }

      const data = {
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        address: this.address,
        zipcode: this.zipcode,
        city: this.city,
        state: this.state,
        phone: this.phone,
        items: items,
        stripe_token: token.id,
      };

      await axios
        .post("/api/v1/checkout", data)
        .then((response) => {
          this.$store.commit("clearCart");

          this.$router.push("/cart/success");
        })
        .catch((error) => {
          this.errors.push("Something went wrong. Please try again.");

          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },

    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.product.price * curVal.quantity);
      }, 0);
    },
  },
};
</script>

<style>
</style>