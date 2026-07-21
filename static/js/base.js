document.addEventListener('DOMContentLoaded', function() {

    // Hero Video Play/Pause Toggle
    const video = document.getElementById('hero-video');
    const button = document.getElementById('video-toggle-btn');
    const icon = document.getElementById('toggle-icon');

    button.addEventListener('click', function() {
        if (video.paused) {
            video.play();
            icon.classList.remove('fa-circle-play');
            icon.classList.add('fa-circle-pause');
            button.setAttribute('aria-label', 'Pause Video');
        } else {
            video.pause();
            icon.classList.remove('fa-circle-pause');
            icon.classList.add('fa-circle-play');
            button.setAttribute('aria-label', 'Play Video');
        }
    });

    // Sticky Navigation Bar on Scroll | Credit to https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollY
    const navbarSticky = document.querySelector('.homepage-sticky-nav');

    if (navbarSticky && video) {
        window.addEventListener('scroll', function() {
            const scrollTriggerPoint = video.offsetHeight / 2;

            if (window.scrollY > scrollTriggerPoint) {
                navbarSticky.classList.add('scrolled');
            } else {
                navbarSticky.classList.remove('scrolled');
            }
        });
    }

    // Remove focus from toggler when collapsed
    const toggler = document.querySelector('.navbar-toggler');

    if (toggler) {
        toggler.addEventListener('click', function() {
            setTimeout(function() {
                toggler.blur();
            }, 150);
        });
    }

    // Navbar products menu transition
    const navbar = document.querySelector('.navbar-bg');
    const productsToggle = document.getElementById('navbarDropdownProducts');
    const dropdownMenu = productsToggle.nextElementSibling;

    if (productsToggle && navbar) {

        // Opening
        productsToggle.addEventListener('show.bs.dropdown', function() {
            navbar.classList.add('navbar-products-open');

            if (dropdownMenu) {
                dropdownMenu.style.display = 'block';

                requestAnimationFrame(() => { /* https://www.w3schools.com/jsref/met_win_requestanimationframe.asp */
                    requestAnimationFrame(() => {
                        dropdownMenu.classList.add('show')
                    })
                })
            }
        });

        // Closing
        productsToggle.addEventListener('hide.bs.dropdown', function(e) {
            productsToggle.blur();
            navbar.classList.remove('navbar-products-open');

            if (dropdownMenu && !dropdownMenu.classList.contains('is-collapsing')) {
                e.preventDefault() // https://getbootstrap.com/docs/4.0/getting-started/javascript/#:~:text=All%20infinitive%20events%20provide%20preventDefault,also%20automatically%20call%20preventDefault()%20
                
                dropdownMenu.classList.remove('show');
                productsToggle.classList.remove('show');
                productsToggle.setAttribute('aria-expanded', 'false');

                dropdownMenu.classList.add('is-collapsing');

                setTimeout(() => {
                    dropdownMenu.classList.remove('is-collapsing');
                    dropdownMenu.style.display = '';

                    const bsDropdown = bootstrap.Dropdown.getInstance(productsToggle);
                    if (bsDropdown) {
                        dropdownMenu.classList.remove('show');
                        productsToggle.classList.remove('show');
                    }
                }, 600);
            }
        });
    }

    // Close Django messages after set period of time
    setTimeout(function() {
        let messages = document.getElementById("msg");
        if (messages) {
            let alert = new bootstrap.Alert(messages);
            alert.close();
        }
    }, 8000);
});