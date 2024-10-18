<template>
  <div class="categories">
    <div class="header">
      <h2>Categories</h2>
      <button class="view-more">view more</button>
    </div>
    <div class="category-grid">
      <div class="category-row" v-for="rowIndex in 2" :key="rowIndex">
        <div class="category-column" v-for="colIndex in 4" :key="colIndex">
          <div class="category-item" v-if="(rowIndex - 1) * 4 + colIndex <= categories.length">
            <img
              :src="categories[(rowIndex - 1) * 4 + colIndex - 1].image"
              :alt="categories[(rowIndex - 1) * 4 + colIndex - 1].name"
            />
            <p>{{ categories[(rowIndex - 1) * 4 + colIndex - 1].name }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      categories: [
        {
          name: 'Beauty & Wellness',
          image: 'src/assets/images/landing/beauty.svg',
        },
        {
          name: 'Barbers & Hair Salon',
          image: 'src/assets/images/landing/barbers.svg',
        },
        {
          name: 'Automotives',
          image: 'src/assets/images/landing/automotives.svg',
        },
        {
          name: 'Cleaning',
          image: 'src/assets/images/landing/cleaning.svg',
        },
        {
          name: 'Repair',
          image: 'src/assets/images/landing/repair.svg',
        },
        {
          name: 'Pet Care',
          image: 'src/assets/images/landing/pet.svg',
        },
        {
          name: 'Child care',
          image: 'src/assets/images/landing/child.svg',
        },
        {
          name: 'Others',
          image: 'src/assets/images/landing/others.svg',
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.categories {
  width: 100%;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;

  h2 {
    font-weight: 700;
    font-size: 1rem;
    margin: 0;
  }

  .view-more {
    color: rgba(157, 86, 200, 1);
  }
}

.category-grid {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.category-row {
  display: flex;
  gap: 16px;
}

.category-column {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.category-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  img {
    width: 80px;
    height: 80px;
    border-radius: 8px;
  }

  p {
    padding-top: 8px;
    text-align: center;
    font-size: 0.8rem;
  }
}
</style>
