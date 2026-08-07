$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);
    var selectedVal = selector.val();

    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");
        window.location.replace(currentUrl);
    }
});

$('.volume-option').change(function() {
    var selectedPrice = $(this).data('price');
    $('#displayPrice').text('£' + parseFloat(selectedPrice).toFixed(2));
});

function handleEnableDisable(itemId, volume) {
    var inputElement = $(`.id_qty_${itemId}`);
    var currentValue = parseInt(inputElement.val()) || 1;
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

var allQtyInputs = $('.qty_input');
for (var i = 0; i < allQtyInputs.length; i++) {
    var itemId = $(allQtyInputs[i]).data('item_id');
    var currentVolume = $('input[name="product_volume"]:checked').val();
    handleEnableDisable(itemId, currentVolume);
}

$('.qty_input').on('change input', function() {
    var itemId = $(this).data('item_id');
    var currentVolume = $('input[name="product_volume"]:checked').val();
    var val = parseInt($(this).val());
    if (isNaN(val) || val < 1) {
        $(this).val(1);
    } else if (val > 99) {
        $(this).val(99);
    }
    handleEnableDisable(itemId, currentVolume);
});

$('.increment-qty').click(function(e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var volume = $('input[name="product_volume"]:checked').val();
    var inputField = $(this).closest('.input-group').find('.qty_input');
    var currentValue = parseInt(inputField.val()) || 1;
    if (currentValue < 99) {
        inputField.val(currentValue + 1);
    }
    handleEnableDisable(itemId, volume);
});

$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var volume = $('input[name="product_volume"]:checked').val();
    var inputField = $(this).closest('.input-group').find('.qty_input');
    var currentValue = parseInt(inputField.val()) || 1;
    if (currentValue > 1) {
        inputField.val(currentValue - 1);
    }
    handleEnableDisable(itemId, volume);
});