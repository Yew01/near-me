<template>
  <div class="search-bar">
    <span class="search-icon">
      <v-icon icon="mdi-magnify" color="primary"></v-icon>
    </span>
    <input type="text" placeholder="Shop name or service" />
  </div>
</template>

<script lang="ts"></script>

<style lang="scss" scoped>
.search-bar {
  display: flex;
  align-items: center;
  margin-block: 16px;
  border-radius: 10px;
  max-height: 40px;
  height: 100px;
  border: none;
  box-shadow: 0px 2px 4px 0px rgba(96, 97, 112, 0.16), 0px 0px 1px 0px rgba(40, 41, 61, 0.04);

  input {
    flex: 1;

    padding: 16px 8px;
    border: none;
    border-radius: 130px;
    background-color: transparent;
    &::placeholder {
      color: #999;
    }

    &:focus {
      /* Add this block */
      outline: none;
    }
  }

  .search-icon {
    padding-right: 4px;
    padding-left: 8px;
  }
}
</style>
