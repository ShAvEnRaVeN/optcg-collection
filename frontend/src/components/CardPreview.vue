<template>
    <div class="col-4 p-3">
        <div class="card" style="width: 18rem;">
            <img class="card-img-top" src="../assets/dummy.jpg" alt="Card image cap">
            <div class="card-body">
                <div class="row">
                    <div class="col-6 text-center">
                        <label class="form-check-label me-2" for="in-folder">
                            In Folder:
                        </label>
                        <input class="form-check-input" type="checkbox" id="in-folder">
                    </div>
                    <div class="col-6">
                        <p class="card-text text-center">Bulk: <span id="bulk">-</span></p>
                    </div>
                </div>
                <h5 class="card-title text-center">Card name</h5>
                <p class="card-text">Rarity: <span id="rarity">-</span></p>

            </div>
        </div>
    </div>
</template>

<script setup>
</script>