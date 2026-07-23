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

    // Responsive popular items carousel
    const container = document.querySelector('#popularProductsCarousel .carousel-inner');
    if (!container) return;

    const rawCards = Array.from(container.querySelectorAll('.js-product-card'));
    if (rawCards.length === 0) return;

    function responsiveCarousel() {
        let itemsPerSlide = 4;
        let colClass = "col-lg-3";

        if (window.innerWidth < 576) {
            itemsPerSlide = 1;
            colClass = "col-12";
        } else if (window.innerWidth < 768) {
            itemsPerSlide = 2;
            colClass = "col-6";
        } else if (window.innerWidth < 992) {
            itemsPerSlide = 3;
            colClass = "col-4";
        }
        
        container.innerHTML = '';

        for (let i = 0; i < rawCards.length; i += itemsPerSlide) {
            const chunk = rawCards.slice(i, i + itemsPerSlide);

            const slide = document.createElement('div');
            slide.className = `carousel-item ${i === 0 ? 'active' : ''}`;

            const row = document.createElement('div');
            row.className = 'row g-3 justify-content-center py-3 px-3 px-md-0';

            chunk.forEach(cardWrapper => {
                const col = document.createElement('div');
                col.className = colClass;
                col.appendChild(cardWrapper.cloneNode(true));
                row.appendChild(col);
            });

            slide.appendChild(row);
            container.appendChild(slide);
        }
    }

    responsiveCarousel();

    //Code adapted from https://developer.mozilla.org/en-US/docs/Web/API/Window/resize_event + https://www.freecodecamp.org/news/javascript-debounce-example/

    let resizeTimer;

    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer)
        resizeTimer = setTimeout(responsiveCarousel, 150);
    });
});
