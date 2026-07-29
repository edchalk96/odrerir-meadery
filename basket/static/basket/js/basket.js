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

$('.update-link').click(function(e) {
        var form = $(this).closest('.col-12').find('.update-form');
        form.submit();
    })

$('.remove-item').click(function(e) {
    e.preventDefault();

    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var itemId = $(this).attr('id').split('remove_')[1];
    var volume = $(this).data('product_volume');
    var url = `/basket/remove/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken, 'product_volume': volume};
    $.post(url, data)
     .done(function() {
         location.reload();
     });
})