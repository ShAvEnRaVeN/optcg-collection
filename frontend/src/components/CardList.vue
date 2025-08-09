<template>
    <h2>{{ currentSet }}</h2>

    <div class="container p-2">
        <div class="row">
            <div v-for="card in cards" :key="card.id" class="card col-6 col-sm-3 col-md-2 col-lg-2 mb-2">
                <img :src="`${flaskURL}/${card.image_dir}`" class="card-img-top" alt="...">
                <div class="card-body d-flex justify-content-between">
                    <h5 class="card-title">{{ card.name }}</h5>
                    <h5 class="card-text">{{ card.num }}</h5>
                </div>
                <a href="#" @click.prevent="selectedCard = card">Details</a>
            </div>
        </div>
    </div>
    <div>
        <CardModal v-if="selectedCard != null" :card="selectedCard" @close="selectedCard = null" />
    </div>

</template>

<script setup>
import CardModal from './CardModal.vue'
import { useCurrentSet } from '../composables/useCurrentSet'
import { getcards } from '../composables/getCards'
import { getSelectedCard } from '@/composables/selectedCard'


const { currentSet } = useCurrentSet()
const { cards } = getcards()
const selectedCard = getSelectedCard()

// base url for requests
const flaskURL = "http://127.0.0.1:5000/"


</script>