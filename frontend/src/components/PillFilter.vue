<template>
  <div class="pill-filter-container">
    <div class="pill-filter-wrapper">
      <div class="pill-filter" v-for="filter in filters" :key="filter">
        {{ filter }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      filters: ['All', 'Food', 'Drinks', 'Shopping', 'Services', 'More'],
    };
  },
};
</script>

<style lang="scss" scoped>
.pill-filter-container {
  width: 100%;
  overflow-x: auto;
  -ms-overflow-style: none; 
  scrollbar-width: none;
  &::-webkit-scrollbar {
    display: none;
  }
}

.pill-filter-wrapper {
  display: inline-flex; 
  gap: 8px; 
}

.pill-filter {
  padding: 8px 16px;
  border-radius: 20px;
  background-color: #f0f0f0; 
  color: #333;
  font-size: 14px;
  cursor: pointer;

  &:hover {
    background-color: #e0e0e0;
  }
}
</style>
