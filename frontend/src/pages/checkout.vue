<template>
  <div class="checkout-container">
    <h3 class="top-title">Checkout</h3>

    <h5>Mimi Hair Salon</h5>

    <div class="shop-service">
      <v-icon icon="mdi-store" color="black" />
      Shop Service
    </div>

    <div class="date-time-container">
      <div class="left-content">
        <v-icon icon="mdi-calendar" color="black" />
        Select Date & Time
      </div>
      <div class="right-content">
        <v-icon icon="mdi-chevron-right" color="rgba(100, 64, 254, 1)" />
      </div>
    </div>

    <PriceCounter :products="cartItems" />
  </div>

  <hr />

  <div class="offers-container">
    <div class="offers-left-content">
      <img src="@/assets/icons/product/discount-percentage-outline.svg" alt="Discount Image" />
      <h6>Offers & Promo Code</h6>
    </div>
    <p>
      View offers <span><v-icon icon="mdi-chevron-right" color="rgba(100, 64, 254, 1)" /></span>
    </p>
  </div>

  <hr />
</template>

<script lang="ts">
import '@/styles/checkout.scss';

export default {
  data() {
    return {
      cartItems: [
        { name: 'Haircut', price: 40, quantity: 3 },
        { name: 'Shave', price: 25, quantity: 2 },
        { name: 'Beard Trim', price: 15, quantity: 2 },
      ],
    };
  },
};
</script>
