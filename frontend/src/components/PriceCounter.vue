<template>
  <div v-for="(product, index) in products" :key="index" class="price-counter-container">
    <div class="product-info">
      <p class="product-title">{{ product.name }}</p>
      <p class="single-price">RM {{ product.price }}</p>
    </div>

    <div class="counter-total">
      <div class="price-counter">
        <button @click="handleDecrement(index)" class="minus-button">
          <v-icon
            :icon="product.quantity === 1 ? 'mdi-trash-can-outline' : 'mdi-minus'"
            :color="product.quantity === 1 ? 'red' : 'rgba(100, 64, 254, 1)'"
          />
        </button>
        <p class="counter-value">{{ product.quantity }}</p>
        <button @click="increment(index)" class="plus-button">
          <v-icon icon="mdi-plus" color="rgba(100, 64, 254, 1)" />
        </button>
      </div>

      <p class="total-price">RM{{ calculateProductTotal(product) }}</p>
    </div>
  </div>
</template>

<script lang="ts">
interface Product {
  name: string;
  price: number;
  quantity: number;
}

export default {
  props: {
    products: {
      type: Array as () => Product[],
      required: true,
    },
  },
  methods: {
    increment(index: number) {
      this.products[index].quantity++;
    },
    decrement(index: number) {
      if (this.products[index].quantity > 1) {
        this.products[index].quantity--;
      }
    },
    calculateProductTotal(product: Product) {
      return product.quantity * product.price;
    },
    handleDecrement(index: number) {
      if (this.products[index].quantity === 1) {
        this.removeProduct(index);
      } else {
        this.decrement(index);
      }
    },
    removeProduct(index: number) {
      this.products.splice(index, 1);
    },
  },
};
</script>

<style lang="scss" scoped>
.price-counter-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;

  .product-info {
    text-align: left;
  }

  .product-title {
    font-size: 1rem;
    font-weight: 700;
  }

  .single-price {
    font-size: 1rem;
    color: rgba(28, 28, 40, 1);
  }

  .counter-total {
    text-align: right;
  }

  .price-counter {
    display: flex;
    gap: 0px;
    align-items: center;
    justify-content: space-between;
    border: 1px solid rgba(100, 64, 254, 1);
    border-radius: 8px;

    min-width: 100px;

    .minus-button,
    .plus-button {
      padding: 4px 8px;
      border: none;
      color: rgba(100, 64, 254, 1);
      cursor: pointer;
    }

    .counter-value {
      font-size: 1rem;
      font-weight: 500;
    }
  }

  .total-price {
    font-size: 1rem;
    color: rgba(28, 28, 40, 1);
  }
}
</style>
