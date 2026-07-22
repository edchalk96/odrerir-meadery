document.addEventListener('DOMContentLoaded', function() {

    // Hero Video Play/Pause Toggle
    const video = document.getElementById('hero-video');
    const button = document.getElementById('video-toggle-btn');
    const icon = document.getElementById('toggle-icon');

    if (video && button && icon) {
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
    }

    // Sticky Navigation Bar on Scroll | Credit to https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollY
    const navbarSticky = document.querySelector('.homepage-nav');

    if (navbarSticky && video) {
        window.addEventListener('scroll', function() {
            const scrollTriggerPoint = video.offsetHeight / 4;

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
            if (window.innerWidth >= 992) {
                navbar.classList.add('navbar-products-open');
            }

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

    //Closing products menu on mobile and tablet
    const closeMobileBtn = document.getElementById('closeProductsMobile');
    if (closeMobileBtn) {
        closeMobileBtn.addEventListener('click', function() {
            const bsDropdown = bootstrap.Dropdown.getInstance(productsToggle);
            if (bsDropdown) {
                bsDropdown.hide();
            }
        });
    }

    // Read more dynamic changes
    const historyCollapse = document.getElementById('historyCollapse');
    const readMoreBtn = document.querySelector('.read-more-btn');

    if (historyCollapse && readMoreBtn) {
        const btnText = readMoreBtn.querySelector('.btn-text');
        const toggleIcon = readMoreBtn.querySelector('.toggle-icon');

        historyCollapse.addEventListener('show.bs.collapse', function () {
            btnText.textContent = 'Read Less';
                if (toggleIcon) {
                    toggleIcon.classList.remove('fa-chevron-down');
                    toggleIcon.classList.add('fa-chevron-up');
                }
        });

        historyCollapse.addEventListener('hide.bs.collapse', function () {
            btnText.textContent = 'Read More';
            if (toggleIcon) {
                toggleIcon.classList.remove('fa-chevron-up');
                toggleIcon.classList.add('fa-chevron-down');
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

    // Mead type content and button changes
    const hexItems = document.querySelectorAll('.hex-item');
    const descriptionInfo = document.getElementById('meadDescription');
    const shopBtn = document.getElementById('meadTypeShopBtn');

    const defaultDescription = descriptionInfo.textContent.trim();
    const defaultBtnText = shopBtn.innerText.trim();
    const defaultBtnUrl = shopBtn.getAttribute('href');
    
    hexItems.forEach(item => {
        item.addEventListener('click', function () {
            const isAlreadyActive = this.classList.contains('active');

            descriptionInfo.style.opacity = '0';

            setTimeout(() => {
                hexItems.forEach(hex => hex.classList.remove('active'));

                if (isAlreadyActive) {
                    descriptionInfo.innerText = defaultDescription;
                    shopBtn.innerText = defaultBtnText;
                    shopBtn.setAttribute('href', defaultBtnUrl);
                } else {
                    this.classList.add('active');

                    const typeName = this.getAttribute('data-type');
                    const description = this.getAttribute('data-description');
                    const url = this.getAttribute('data-url');

                    descriptionInfo.textContent = description;
                    shopBtn.textContent = `Shop ${typeName}`;
                    shopBtn.setAttribute('href', url);
                }

                descriptionInfo.style.opacity = '1';
            }, 150);
        });
    });
});
