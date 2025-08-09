import { ref } from 'vue'

const selectedCard = ref(null)

export function getSelectedCard(){
    return selectedCard 
}