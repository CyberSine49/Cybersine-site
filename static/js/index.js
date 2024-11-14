// JavaScript to toggle the mobile menu
console.log("trigged")
document.getElementById('menu-toggle').addEventListener('click', function () {
    console.log("menu toggled")
    const mobileMenu = document.getElementById('mobile-menu');
    mobileMenu.classList.toggle('hidden');
});


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            const headerOffset = 115;
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// add get in touch listener
document.querySelector('.get-started-btn').addEventListener('click', function (e) {
    e.preventDefault();
    const targetElement = document.querySelector('#contact-section');

    if (targetElement) {
        const headerOffset = 115;
        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    }
});


// js to observe scroll position and add 'visible' class
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
});

document.querySelectorAll('.section').forEach(section => {
    observer.observe(section);
});


