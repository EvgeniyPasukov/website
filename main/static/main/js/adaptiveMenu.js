const button_menu = document.querySelector('.button_menu')
const menu_navigation = document.querySelector('.menu_navigation')
const button_close = document.querySelector('.button_close')

button_menu.addEventListener('click',OpenButtonMenu)
button_close.addEventListener('click',ButtonCloseMenu)

function OpenButtonMenu() {
    button_menu.classList.add('show')
    menu_navigation.classList.add('navigation_active')

}

function ButtonCloseMenu() {
console.log('hel')
    menu_navigation.classList.remove('navigation_active')
    button_menu.classList.remove('show')
}
