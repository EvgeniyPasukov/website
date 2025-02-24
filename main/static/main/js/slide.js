document.addEventListener('DOMContentLoaded', function () {
    const slider = document.querySelector('.itc-slider');
    const items = slider.querySelector('.itc-slider-items');
    const slides = slider.querySelectorAll('.itc-slider-item');
    const prevBtn = slider.querySelector('.itc-slider-btn-prev');
    const nextBtn = slider.querySelector('.itc-slider-btn-next');
    const indicators = slider.querySelectorAll('.itc-slider-indicator');

    let currentIndex = 0;
    let autoSlideInterval;

    // Функция для показа текущего слайда
    function showSlide(index) {
        const offset = -index * 100;
        items.style.transform = `translateX(${offset}%)`;
        updateIndicators(index);
    }

    // Функция для обновления индикаторов
    function updateIndicators(index) {
        indicators.forEach((indicator, i) => {
            indicator.classList.toggle('itc-slider-indicator-active', i === index);
        });
    }

    // Функция для переключения на следующий слайд
    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    // Функция для переключения на предыдущий слайд
    function prevSlide() {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(currentIndex);
    }

    // Запуск автоматического переключения слайдов
    function startAutoSlide() {
        autoSlideInterval = setInterval(nextSlide, 4000); // 4 секунды
    }

    // Остановка автоматического переключения слайдов
    function stopAutoSlide() {
        clearInterval(autoSlideInterval);
    }

    // Обработчики для кнопок "Назад" и "Вперед"
    prevBtn.addEventListener('click', () => {
        stopAutoSlide();
        prevSlide();
        startAutoSlide();
    });

    nextBtn.addEventListener('click', () => {
        stopAutoSlide();
        nextSlide();
        startAutoSlide();
    });

    // Обработчики для индикаторов
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            stopAutoSlide();
            currentIndex = index;
            showSlide(currentIndex);
            startAutoSlide();
        });
    });

    // Остановка автоматического переключения при наведении на слайдер
    slider.addEventListener('mouseenter', stopAutoSlide);

    // Возобновление автоматического переключения при уходе курсора
    slider.addEventListener('mouseleave', startAutoSlide);

    // Запуск автоматического переключения при загрузке страницы
    startAutoSlide();
});