<template>
  <div class="filter-button-container">
    <div
      class="filter-button"
      v-for="category in categories"
      :key="category"
      @click="selectedCategory = category"
      :class="{ active: selectedCategory === category }"
    >
      <p>{{ category }}</p>
    </div>
  </div>

  <div class="content-container" v-for="category in categories" :key="category">
    <div v-if="selectedCategory === category || selectedCategory === 'Recommended'">
      <h5>{{ category }} ({{ productsByCategory[category]?.length || 0 }})</h5>

      <div class="content" v-for="product in productsByCategory[category] || []" :key="product.id">
        <div class="content-row">
          <img :src="product.image" :alt="`${product.name} Image`" />
          <div class="content-details">
            <div class="content-details-top">
              <h6>{{ product.name }}</h6>
              <p>{{ product.price }}</p>
            </div>
            <div class="content-details-bottom">
              <p>{{ product.duration }}</p>
            </div>
          </div>

          <button class="select-button">Select +</button>
        </div>
      </div>

      <hr v-if="!(categories.indexOf(category) === categories.length - 1)" />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedCategory: 'Recommended',
      categories: ['Recommended', 'Packages', 'Face Care', 'Barber'],
      products: [
        {
          id: 1,
          name: 'Haircut',
          price: 'RM 40',
          duration: '40 mins',
          image: 'src/assets/images/product/haircut.png',
          category: 'Recommended',
        },
        {
          id: 2,
          name: 'Body Massage',
          price: 'RM 40',
          duration: '20 mins',
          image: 'src/assets/images/product/body-massage.png',
          category: 'Recommended',
        },
        {
          id: 3,
          name: 'Active Detox Cleanup',
          price: 'RM 40',
          duration: '10 mins',
          image: 'src/assets/images/product/detox.png',
          category: 'Recommended',
        },
        {
          id: 4,
          name: 'Haircut & Shave',
          price: 'RM 40',
          duration: '40 mins',
          image: 'src/assets/images/product/shave.png',
          category: 'Packages',
        },
        {
          id: 5,
          name: 'Haircut & Beard Grooming',
          price: 'RM 40',
          duration: '40 mins',
          image: 'src/assets/images/product/beard-grooming.png',
          category: 'Packages',
        },
        {
          id: 6,
          name: 'Haircut & Anti-Pollution Cleanup',
          price: 'RM 40',
          duration: '40 mins',
          image: 'src/assets/images/product/anti-pollution.png',
          category: 'Packages',
        },
        {
          id: 7,
          name: 'Haircut & Shave',
          price: 'RM 40',
          duration: '40 mins',
          image: 'src/assets/images/product/casmara.png',
          category: 'Face Care',
        },
        {
          id: 8,
          name: 'Haircut & Beard Grooming',
          price: 'RM 40',
          duration: '40 mins',
          image: 'src/assets/images/product/casmara2.png',
          category: 'Face Care',
        },
        {
          id: 9,
          name: 'Haircut & Anti-Pollution Cleanup',
          price: 'RM 40',
          duration: '40 mins',
          image: 'src/assets/images/product/charcoal.png',
          category: 'Face Care',
        },
      ],
    };
  },
  computed: {
    productsByCategory() {
      return this.products.reduce((acc, product) => {
        if (!acc[product.category]) {
          acc[product.category] = [];
        }
        acc[product.category].push(product);
        return acc;
      }, {});
    },
  },
};
</script>

<style lang="scss" scoped>
.filter-button-container {
  display: flex;
  gap: 8px;
  overflow-x: scroll;
  overflow-y: hidden;
  -ms-overflow-style: none;
  scrollbar-width: none;
  &::-webkit-scrollbar {
    display: none;
  }

  .filter-button {
    padding: 4px 16px;
    border: 0.5px solid rgba(143, 144, 166, 1);
    border-radius: 8px;
    min-width: min-content;
    white-space: nowrap;
    color: rgba(143, 144, 166, 1);

    cursor: pointer;

    &.active {
      border-color: rgba(100, 64, 254, 1);
      color: rgba(100, 64, 254, 1);
      background-color: rgba(123, 97, 255, 0.1);
    }
  }
}

.content-container {
  margin-top: 16px;

  h5 {
    font-size: 1rem;
    font-weight: 700;
  }

  hr {
    border: 0.5px solid rgba(199, 201, 217, 1);
  }

  .content {
    margin-block: 8px;

    .content-row {
      display: flex;
      gap: 8px;
      align-items: start;

      img {
        width: 75px;
        height: 75px;
        border-radius: 8px;
      }

      .content-details {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        gap: 4px;
        height: 100%;

        .content-details-top {
          display: flex;
          flex-direction: column;
          gap: 0px;

          h6 {
            font-size: 1rem;
            font-weight: 700;
          }

          p {
            font-size: 0.8rem;
            color: rgba(143, 144, 166, 1);
          }
        }

        .content-details-bottom {
          display: flex;
          gap: 8px;

          p {
            font-size: 0.8rem;
            color: rgba(143, 144, 166, 1);
          }
        }
      }

      .select-button {
        margin-left: auto;
        min-width: fit-content;
        padding: 4px 8px;
        border: 0.5px solid rgba(100, 64, 254, 1);
        border-radius: 8px;
        color: rgba(100, 64, 254, 1);
      }
    }
  }
}
</style>
