// // Добавляем тени к заголовку при прокрутке
// window.addEventListener('scroll', () => {
//     const header = document.querySelector('.header');
//     if (window.scrollY > 50) {
//         header.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.3)';
//         header.style.background = 'rgba(0, 0, 0, 0.8)';
//     } else {
//         header.style.boxShadow = 'none';
//         header.style.background = 'rgba(0, 0, 0, 0.5)';
//     }
// });
//
// // Устанавливаем активный класс для текущей страницы в навигации
// document.addEventListener('DOMContentLoaded', function() {
//     const currentPage = window.location.pathname.split('/').pop();
//     const navLinks = document.querySelectorAll('.nav__link');
//     
//     navLinks.forEach(link => {
//         if (link.getAttribute('href') === currentPage || 
//             (currentPage === '' && link.getAttribute('href') === 'index.html')) {
//             link.classList.add('nav__link--active');
//         } else {
//             link.classList.remove('nav__link--active');
//         }
//     });
// });
