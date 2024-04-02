const button_menu = document.querySelector('.button_menu')
const menu_navigation = document.querySelector('.menu_navigation')
const button_close = document.querySelector('.button_close')
const body = document.querySelector('body')
const burger_bg = document.querySelector('.burger_bg')
const contact_link = document.querySelector('.contact_link')

button_menu.addEventListener('click',OpenButtonMenu)
button_close.addEventListener('click',ButtonCloseMenu)
burger_bg.addEventListener('click',ButtonCloseMenu)
contact_link.addEventListener('click',ButtonCloseMenu)

function OpenButtonMenu() {
    burger_bg.classList.add('is-burger-bg')
    body.classList.add('scroll')
    button_menu.classList.add('show')
    menu_navigation.classList.add('navigation_active')
}

function ButtonCloseMenu() {
    burger_bg.classList.remove('is-burger-bg')
    body.classList.remove('scroll')
    menu_navigation.classList.remove('navigation_active')
    button_menu.classList.remove('show')
}
