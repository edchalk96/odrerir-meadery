var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);

var appearance = {
    theme: 'stripe',
    variables: {
        colorPrimary: '#000000',
        colorBackground: '#ffffff',
        colorText: '#000000',
        colorDanger: '#dc3545',
        fontFamily: 'Helvetica Neue, Helvetica, sans-serif',
        borderRadius: '4px',
    }
};

var elements = stripe.elements({
    clientSecret: clientSecret,
    appearance: appearance
});


var paymentElementOptions = {
    layout: {
        type: 'tabs',
        defaultCollapsed: false,
    },
};

var paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');

paymentElement.on('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        function getValue(element) {
            return element && element.value ? element.value.trim() : '';
        }

        stripe.confirmPayment({
            elements: elements,
            confirmParams: {
                return_url: window.location.origin + '/checkout/checkout_success/',
                payment_method_data: {
                    billing_details: {
                        name: getValue(form.full_name),
                        phone: getValue(form.phone_number),
                        email: getValue(form.email),
                        address: {
                            line1: getValue(form.street_address1),
                            line2: getValue(form.street_address2),
                            city: getValue(form.town_or_city),
                            country: getValue(form.country),
                            state: getValue(form.county),
                        }
                    }
                },
                shipping: {
                    name: getValue(form.full_name),
                    phone: getValue(form.phone_number),
                    address: {
                        line1: getValue(form.street_address1),
                        line2: getValue(form.street_address2),
                        city: getValue(form.town_or_city),
                        country: getValue(form.country),
                        postal_code: getValue(form.postcode),
                        state: getValue(form.county),
                    }
                }
            },
            redirect: 'if_required'
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent && result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    })
});