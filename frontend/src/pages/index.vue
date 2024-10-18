<template>
  <div class="container">
    <Location />
    <SearchBar />
    <PillFilter />
  </div>

  <div class="container">
    <Category />
  </div>

  <div class="container">
    <hr />
  </div>

  <div class="container">
    <CardCarousel :cards="myCardData" :cardCarouselTitle="'Popular near you'" />
  </div>

  <div class="container">
    <CardCarousel :cards="bestOffersData" :cardCarouselTitle="'Best Offers'" />
  </div>
</template>

<script lang="ts">
import '@/styles/index.scss';

export default {
  data() {
    return {
      myCardData: [
        {
          id: 1,
          imageUrl: 'src/assets/images/landing/woodlands-hills.png',
          filterTitle: 'for men & women',
          cardTitle: 'Woodlands Hills Salon',
          filters: ['haircut', 'Spa', 'Massage'],
          rating: 4.1,
          location: 'Keira throughway',
          distance: 5.0,
          priceRange: '$$$',
        },
        {
          id: 2,
          imageUrl: 'src/assets/images/landing/woodlands-hills.png',
          filterTitle: 'for men & women',
          cardTitle: 'Woodlands Hills Salon',
          filters: ['haircut', 'Spa', 'Massage'],
          rating: 4.1,
          location: 'Keira throughway',
          distance: 5.0,
          priceRange: '$$$',
        },
        {
          id: 3,
          imageUrl: 'src/assets/images/landing/woodlands-hills.png',
          filterTitle: 'for men & women',
          cardTitle: 'Woodlands Hills Salon',
          filters: ['haircut', 'Spa', 'Massage'],
          rating: 4.1,
          location: 'Keira throughway',
          distance: 5.0,
          priceRange: '$$$',
        },
      ],
      bestOffersData: [
        {
          id: 1,
          imageUrl: 'src/assets/images/landing/mounrich-spa.png',
          filterTitle: 'for women',
          cardTitle: 'Mounrich Spa Services',
          filters: ['Spa', 'Salon'],
          rating: 4.1,
          location: 'Woodland Hills',
          distance: 5.0,
          priceRange: '$$',
        },
        {
          id: 2,
          imageUrl: 'src/assets/images/landing/mounrich-spa.png',
          filterTitle: 'for women',
          cardTitle: 'Mounrich Spa Services',
          filters: ['Spa', 'Salon'],
          rating: 4.1,
          location: 'Woodland Hills',
          distance: 5.0,
          priceRange: '$$',
        },
        {
          id: 3,
          imageUrl: 'src/assets/images/landing/mounrich-spa.png',
          filterTitle: 'for women',
          cardTitle: 'Mounrich Spa Services',
          filters: ['Spa', 'Salon'],
          rating: 4.1,
          location: 'Woodland Hills',
          distance: 5.0,
          priceRange: '$$',
        },
      ],
    };
  },
};
</script>
