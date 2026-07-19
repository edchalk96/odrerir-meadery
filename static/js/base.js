document.addEventListener('DOMContentLoaded', function() {
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
});