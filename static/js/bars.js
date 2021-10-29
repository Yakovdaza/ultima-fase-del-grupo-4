const navToggle = document.querySelector(".toggle3")
const navCaja=document.querySelector(".caja")
const navBtnSearch = document.querySelector(".btn-search")
const navMenu = document.querySelector(".nav_menu")
const navSearch = document.querySelector(".search")
const navLogo= document.querySelector(".logo")
const navCar=document.querySelector("#carrito")
const navCar2=document.querySelector("#carrito2")
const carbar=document.querySelector(".carrito")
const foncar=document.querySelector(".fondo-car")

var query = window.matchMedia("(min-width: 412px)");

// if(query.matches){
    navToggle.addEventListener("click", () => {
        navMenu.classList.toggle("nav_menu_visible")
        
    }) 
    // navBtnSearch.addEventListener("click", function () {
    //         navSearch.classList.toggle("visible")
    //         navToggle.classList.toggle("invisible")
    //         navLogo.classList.toggle("invisible")
    //         navCaja.classList.toggle("invisible")
    //     })
    navCar.addEventListener("click",() => {
        carbar.classList.toggle("activo")
        foncar.classList.toggle("activo")
    })
    navCar2.addEventListener("click",() => {
        carbar.classList.toggle("activo")
        foncar.classList.toggle("activo")
    })
// }
// if(query.matches){
    // navSearch.classList.remove("visible")
    // navToggle.classList.remove("invisible")
    // navLogo.classList.remove("invisible")
    // navCaja.classList.remove("invisible")
// }
// 
