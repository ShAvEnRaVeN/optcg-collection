<template>

    <div class="d-flex flex-wrap justify-content-center p-3">
            <button v-for="set in sets" :key="set" class="btn btn-primary m-1" @click="selectSet(set)">{{set}}</button>
    </div>


</template>

<script setup>
    import { ref, onMounted } from 'vue'
    import { useCurrentSet } from '../composables/useCurrentSet'
    import { getcards } from '@/composables/getCards'

    const { currentSet } = useCurrentSet()
    const { cards } = getcards()
    

    const sets = ref([])

    onMounted(async () => {
        const res = await fetch('http://127.0.0.1:5000/api/sets')
        sets.value = await res.json()
    })

    async function selectSet(set){
        currentSet.value = set
        const res = await fetch(`http://127.0.0.1:5000/api/${set}`)
        cards.value = await res.json()
    }
    

</script>