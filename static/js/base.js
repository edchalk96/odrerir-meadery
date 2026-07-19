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
    const navbar = document.querySelector('.homepage-sticky-nav');

    if (navbar && video) {
        window.addEventListener('scroll', function() {
            const scrollTriggerPoint = video.offsetHeight / 2;

            if (window.scrollY > scrollTriggerPoint) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
});