<template>
    <div class="container">
        <h2>{{ currentSet }}</h2>
        <ul>
            <li class="d-flex" v-for="card in cards" :key="card.num">
                <p class="col-3">{{ card.num }}</p>
                <a href="#" class="col-6" @click.prevent=""> {{ card.name }}</a>
            </li>
        </ul>
    </div>

</template>

<script setup>
import { useCurrentSet } from '../composables/useCurrentSet'
import { getcards } from '../composables/getCards'

const { currentSet } = useCurrentSet()
const { cards } = getcards()


</script>