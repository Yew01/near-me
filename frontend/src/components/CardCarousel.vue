<template>
  <div class="card-carousel">
    <div class="header">
      <h2>{{cardCarouselTitle}}</h2>
      <router-link to="/explore" class="view-more">
        see all
        <v-icon icon="mdi-chevron-right" color="rgba(100, 64, 254, 1)" />
      </router-link>
    </div>

    <div class="card-row">
      <div v-for="card in cards" :key="card.id" class="card-container">
        <img :src="card.imageUrl" :alt="card.cardTitle + ' Image'" />
        <p class="filter-title">{{ card.filterTitle }}</p>

        <p class="card-title">{{ card.cardTitle }}</p>

        <p class="filters">
          {{ card.filters.join(', ') }}
          <v-icon size="large" icon="mdi-circle-small" color="rgba(196, 196, 196, 1)" />
          <v-icon size="large" icon="mdi-star-outline" color="rgba(143, 144, 166, 1)" />
          <span class="rating"> {{ card.rating }} </span>
        </p>

        <p class="filters">
          {{ card.location }}
          <v-icon size="large" icon="mdi-circle-small" color="rgba(196, 196, 196, 1)" />
          <span> {{ card.distance }} Kms </span>
          <v-icon size="large" icon="mdi-circle-small" color="rgba(196, 196, 196, 1)" />
          <span> {{ card.priceRange }} </span>
        </p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

interface Card {
  id: number;
  imageUrl: string;
  filterTitle: string;
  cardTitle: string;
  filters: string[];
  rating: number;
  location: string;
  distance: number;
  priceRange: string;
}

export default defineComponent({
  name: 'CardCarousel',
  props: {
    cardCarouselTitle: {
      type: String,
      required: true,
      default: '',
    },
    cards: {
      type: Array as PropType<Card[]>,
      required: true,
      default: () => [],
    },
  },
});
</script>

<style lang="scss" scoped>
.card-carousel {
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
    color: rgba(100, 64, 254, 1);
    text-decoration: none;
  }
}

.card-row {
  display: flex;
  gap: 32px;
  overflow-y: scroll;
  -ms-overflow-style: none;
  scrollbar-width: none;
  &::-webkit-scrollbar {
    display: none;
  }

  .card-container {
    display: flex;
    flex-direction: column;
    align-items: start;

    img {
      border-radius: 12px;
    }

    .filter-title {
      padding-top: 6px;
      color: rgba(143, 144, 166, 1);
      font-size: 0.75rem;
      font-weight: 500;
      text-transform: uppercase;
    }

    .card-title {
      font-size: 1rem;
      font-weight: 700;
      margin: 0;
    }

    .filters {
      color: rgba(143, 144, 166, 1);
      font-size: 0.75rem;
      font-weight: 300;
      text-transform: capitalize;

      .rating {
        color: rgba(143, 144, 166, 1);
        font-weight: 500;
      }
    }
  }
}
</style>
