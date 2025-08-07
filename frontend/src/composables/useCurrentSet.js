import { ref } from 'vue'

const currentSet = ref('none')

export function useCurrentSet(){
    return { currentSet }
}