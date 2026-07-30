function handleEnableDisable(element) {
    var container = $(element).closest('.update-form');
    var inputElement = container.find('.qty_input');
    var currentValue = parseInt(inputElement.val()) || 1;

    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;

    container.find('.decrement-qty').prop('disabled', minusDisabled);
    container.find('.increment-qty').prop('disabled', plusDisabled);
}

$('.qty_input').each(function() {
    handleEnableDisable(this);
});

$('.qty_input').on('change input', function() {
    var val = parseInt($(this).val());

    if (isNaN(val) || val < 1) {
        $(this).val(1);
    } else if (val > 99) {
        $(this).val(99);
    }
    handleEnableDisable(this);
});

$('.increment-qty').click(function(e) {
    e.preventDefault();

    var inputField = $(this).closest('.input-group').find('.qty_input');
    var currentValue = parseInt(inputField.val()) || 1;
    if (currentValue < 99) {
        inputField.val(currentValue + 1);
    }
    handleEnableDisable(this);
});

$('.decrement-qty').click(function(e) {
    e.preventDefault();

    var inputField = $(this).closest('.input-group').find('.qty_input');
    var currentValue = parseInt(inputField.val()) || 1;
    if (currentValue > 1) {
        inputField.val(currentValue - 1);
    }
    handleEnableDisable(this);
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