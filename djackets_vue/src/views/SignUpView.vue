<template>
  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign Up</h1>
        <form action="" @submit.prevent="SubmitForm">
          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input
                class="input"
                type="email"
                placeholder="Email"
                v-model="email"
                
              />
            </div>
          </div>
          <div class="field">
            <label class="label">username</label>
            <div class="control">
              <input
                class="input"
                type="username"
                placeholder="Username"
                v-model="username"
                
              />
            </div>
          </div> 
          <div class="field">
            <label class="label">Password</label>
            <div class="control">
              <input
                class="input"
                type="password"
                placeholder="Password"
                v-model="password1"
                
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Confirm password</label>
            <div class="control">
              <input
                class="input"
                type="password"
                placeholder="Confirm Password"
                v-model="password2"
                
              />
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-dark">Sign Up</button>
            </div>
          </div>
          <hr />

         Already have an account?
          <router-link to="/login" class="button is-success"
            >Sign in</router-link
          >
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      email: "",
      password1: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    SubmitForm() {
      this.errors = [];

      if (this.username === "") {
        this.errors.push("Please enter a username");
      }

      if (this.password1 === "") {
        this.errors.push("The password is too short");
      }

      if (this.password1 !== this.password2) {
        this.errors.push("Passwords don\'t match");
        return;
      }

      if (!this.errors.length){
        const formData ={
          username: this.username,
          email: this.email,
          password: this.password1,
        
        }
        axios
        .post("/api/v1/users/", formData)
        .then(response =>{
          toast({
            message: "Account created successfully",
            type: "is-success",
            duration: 2000,
            dismissible: true,
            position: "bottom-right",
            pauseOnHover: true,
          })
          this.$router.push("/login");
        })
        .catch(error =>{
          if (error.response){
            for (const property in error.response.data){
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }

            console.log(JSON.stringify(error.response.data));
          }
          else if (error.message){
            this.errors.push('Something went wrong. Please try.');

            console.log(JSON.stringify(error));
          }
        })
      }
    },
  },
};
</script>
