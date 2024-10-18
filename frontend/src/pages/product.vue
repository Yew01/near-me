<template>
  <div class="banner">
    <div class="top-bar">
      <v-icon icon="mdi-chevron-left" color="white" />

      <v-icon icon="mdi-magnify" color="white" />
    </div>

    <div class="banner-content">
      <div class="left-content">
        <h1>Huulk Barber</h1>
        <p>
          Kuala Lumpur <v-icon size="large" icon="mdi-circle-small" color="rgba(196, 196, 196, 1)" />5.0 Kms
          <v-icon size="large" icon="mdi-circle-small" color="rgba(196, 196, 196, 1)" /> $$
        </p>
      </div>

      <div class="right-content">
        <v-icon size="large" icon="mdi-heart-outline" color="rgba(196, 196, 196, 1)" />
        <p>Favourite</p>
      </div>
    </div>
  </div>

  <div class="top-content-container">
    <div class="product-contact">
      <div class="icons-container">
        <div class="icon-container">
          <v-icon icon="mdi-phone-outline" color="black" />
          <p>Call</p>
        </div>

        <div class="icon-container">
          <v-icon icon="mdi-map-marker-outline" color="black" />
          <p>Directions</p>
        </div>

        <div class="icon-container">
          <v-icon icon="mdi-export-variant" color="black" />
          <p>Share</p>
        </div>
      </div>

      <div class="ratings">
        <div class="stars">
          <v-icon icon="mdi-star-outline" color="rgba(0, 99, 247, 1)" />
          <p>4.5</p>
        </div>
        <p>5k+ ratings</p>
      </div>
    </div>

    <hr />

    <Discount :discounts="discounts" />
  </div>

  <hr />

  <div class="bottom-content-container">
    <CategoryFilter />
  </div>
</template>

<script lang="ts">
import '@/styles/product.scss';

export default {
  data() {
    return {
      discounts: [
        { id: 1, percentageOff: '50% Off', code: 'use code FREE50' },
        { id: 2, percentageOff: '60% Off on Debit Card', code: 'No coupon required' },
        { id: 3, percentageOff: 'RM10 Off', code: 'WELCOME10' },
      ],
    };
  },
};
</script>
