<template>
  <div id="app">
    <div class="d-flex align-items-baseline">
      <h1 class="p-3">Needs a title</h1>
      <h3 class="ms-auto p-3">Maybe a search feature</h3>
    </div>
    <SetButtons />
    <div class="d-flex">
      <CardPreview />
      <CardList />
    </div>
  </div>
</template>

<script setup>
import SetButtons from './components/SetButtons.vue'
import CardPreview from './components/CardPreview.vue'
import CardList from './components/CardList.vue'


</script>

<style></style>
