document.addEventListener('DOMContentLoaded', function() {

    // Age Verification
    const ageModalElement = document.getElementById("ageVerificationModal");
    if (!ageModalElement) return;

    const ageModal = new bootstrap.Modal(ageModalElement, {
        backdrop: 'static',
        keyboard: false
    });

    const isAgeVerified = localStorage.getItem("odrerir_age_verified");
    const modalQuestion = document.getElementById("ageModalQuestion");
    const modalDenied = document.getElementById("ageModalDenied");

    if (isAgeVerified !== "true") {
        modalQuestion.classList.remove("d-none");
        modalDenied.classList.add("d-none");
        ageModal.show();
    }

    document.getElementById("btnAgeConfirm").addEventListener("click", function () {
        localStorage.setItem("odrerir_age_verified", "true");
        ageModal.hide();
    });

    document.getElementById("btnAgeDeny").addEventListener("click", function () {
        modalQuestion.classList.add("d-none");
        modalDenied.classList.remove("d-none");
    });

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
                        dropdownMenu.classList.add('show');
                    });
                });
            }
        });

        // Closing
        productsToggle.addEventListener('hide.bs.dropdown', function(e) {
            productsToggle.blur();

            navbar.classList.remove('navbar-products-open');

            if (dropdownMenu && !dropdownMenu.classList.contains('is-collapsing')) {
                e.preventDefault(); // https://getbootstrap.com/docs/4.0/getting-started/javascript/#:~:text=All%20infinitive%20events%20provide%20preventDefault,also%20automatically%20call%20preventDefault()%20
                
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

    // Fade-in on scroll
    const observerOptions = {
        root: null,
        rootMargin: "0px",
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const fadeElements = document.querySelectorAll(".fade-in-element");
    fadeElements.forEach(el => observer.observe(el));

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

            for (const cardWrapper of chunk) {
                const col = document.createElement('div');
                col.className = colClass;
                col.appendChild(cardWrapper.cloneNode(true));
                row.appendChild(col);
            }

            slide.appendChild(row);
            container.appendChild(slide);
        }
    }

    responsiveCarousel();

    //Code adapted from https://developer.mozilla.org/en-US/docs/Web/API/Window/resize_event + https://www.freecodecamp.org/news/javascript-debounce-example/

    let resizeTimer;

    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(responsiveCarousel, 150);
    });
});

// Toast Functionality | Adapted from https://colorlib.com/wp/bootstrap-toasts/ | https://codepen.io/nttoan1202/pen/OJzvQQN */

function showDjangoToasts() {
    const toasts = document.querySelectorAll("#toast-container .toast");

    toasts.forEach((toast) => {
        const closeBtn = toast.querySelector(".close");
        const progress = toast.querySelector(".progress");

        let timer1, timer2;
        let remainingTime = 10000;
        let startTime;

        // Function to start or resume the dismiss timer
        const startDismissTimer = (time) => {
            startTime = Date.now();

            timer1 = setTimeout(() => {
                toast.classList.remove("active");
            }, time);

            timer2 = setTimeout(() => {
                if (progress) {
                    progress.classList.remove("active");
                }
                toast.remove();
            }, time + 500);
        };

        setTimeout(() => {
            toast.classList.add("active");
            if (progress) {
                progress.classList.add("active");
            }
            startDismissTimer(remainingTime);
        }, 100);

        toast.addEventListener("mouseenter", () => {
            clearTimeout(timer1);
            clearTimeout(timer2);
            remainingTime -= Date.now() - startTime;
        });

        toast.addEventListener("mouseleave", () => {
            if (remainingTime > 0) {
                startDismissTimer(remainingTime);
            } else {
                toast.classList.remove("active");
                setTimeout(() => toast.remove(), 500);
            }
        });

        if (closeBtn) {
            closeBtn.addEventListener("click", () => {
                toast.classList.remove("active");
                setTimeout(() => {
                    if (progress) {
                        progress.classList.remove("active");
                    }
                    toast.remove();
                }, 400);
                clearTimeout(timer1);
                clearTimeout(timer2);
            });
        }
    });
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", showDjangoToasts);
} else {
    showDjangoToasts();
}