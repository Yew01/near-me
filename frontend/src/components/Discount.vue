<template>
  <div class="discount-container">
    <div v-for="discount in discounts" :key="discount.id" class="discount-card">
      <div class="top-discount-card">
        <img src="@/assets/icons/product/discount-percentage.svg" alt="Discount Image" />
        <p>{{ discount.percentageOff }}</p>
      </div>
      <div class="bottom-discount-card">
        <p>{{ discount.code }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
interface Discount {
  id: number;
  percentageOff: string;
  code: string;
}

export default {
  name: 'Discount',
  props: {
    discounts: {
      type: Array as () => Discount[],
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.discount-container {
  width: 100%;
  display: flex;
  gap: 8px;

  overflow-x: auto;
  overflow-y: hidden;
  -ms-overflow-style: none;
  scrollbar-width: none;
  &::-webkit-scrollbar {
    display: none;
  }

  .discount-card {
    border: 1px solid rgba(242, 242, 245, 1);
    border-radius: 8px;
    padding: 8px 16px;

    display: flex;
    flex-direction: column;
    gap: 2px;

    min-width: min-content;
    width: 100%;

    .top-discount-card {
      display: flex;
      gap: 8px;
      align-items: center;

      font-weight: 700;
      font-size: 1rem;
      width: 100%;
      white-space: nowrap;
    }

    .bottom-discount-card {
      font-weight: 400;
      font-size: 0.8rem;
      white-space: nowrap;
    }
  }
}
</style>
