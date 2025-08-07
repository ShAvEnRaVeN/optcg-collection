import { ref } from 'vue'

const cards = ref([])

export function getcards(){
    return { cards }
}