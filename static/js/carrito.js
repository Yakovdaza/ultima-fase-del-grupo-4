const addToShopCarBtn = document.querySelectorAll("#addcar")

addToShopCarBtn.forEach((addToCarBtn) => {
    addToCarBtn.addEventListener("click", addToCarClick)
})
    
const shopCarPordCont=document.querySelector('.shopCarRow')
const compBtn =document.querySelector(".btn-success")
compBtn.addEventListener('click',compBtnClk)


function addToCarClick(e){
    const btn = e.target;
    const   prod = btn.closest('.producto')
    
    const   pordNon  = prod.querySelector('.titulo').textContent
    const   prodPrice = prod.querySelector('.precio').textContent
    const   prodDes= prod.querySelector('.descripcion').textContent

    addProdShopCar(pordNon, prodPrice, prodDes)
}

function addProdShopCar(pordNon, prodPrice, prodDes){
    const elemTtl = shopCarPordCont.getElementsByClassName("shopCarElmTitle")
    for( let i=0; i< elemTtl.length ; i++ ){
        if(elemTtl[i].innerText === pordNon ){

            let elemQaun = elemTtl[i].parentElement.parentElement.querySelector(".form-select")
            elemQaun.value++
            return
        }
    }

    const shopCarRow=document.createElement('div')
    const shopCarCont = `
                <div class="contacto">
                <div class="lalal shopCarElmTitle">${pordNon}</div>
                <div class="lalal"><img src="img/cafe_helado.jpg" class="img-thumbnail"><p class="shopCarPordPrice">${prodPrice}</p<</div>
                <div class="lalal">${prodDes}</div>
                <div class="lalal">
                    <select class="form-select lalal"  aria-label=".bg-success">
                        <option value="1" selected >1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                    </select>  
                </div>
                    <button class="btnDel entrar">eliminar</button>
                </div>`;

    shopCarRow.innerHTML = shopCarCont
    shopCarPordCont.append(shopCarRow)

    shopCarRow
    .querySelector('.btnDel')
    .addEventListener('click',remShopCarProd)

    // shopCarRow
    // .querySelector('form-select')
    // .addEventListener('change', quantitChange)
    
    updateShopCarTotal()

}

function  updateShopCarTotal(){
    let total= 0;

    const shopcartotal= documet.querySelector('.total-car')
    console.log(shopcartotal)
    const shopCarProd =documetn.querySelectorAll(".contacto")

    
    shopCarProd.forEach((shopCarPord)=>{
        const shopCarPriceElem = shopCarPord.querySelector(".shopCarPordPrice")
        
        const shopCarPrice = number(shopCarPriceElem.textContent.replace('$',""))
        const shoppingcarpordCuantityelement=shopCarProd.queryselector('form-select')
        const shoppingcarpordCuantit= number(shoppingcarpordCuantityelement.value)
        total = total + shopCarPrice * shoppingcarpordCuantit
    })
    
    shopcartotal.innerHTML = `${total}`
}


function remShopCarProd (e){
    const btnClk = e.target;
    btnClk.closest('.shopCarPord').remove()
    updateShopCarTotal();
}
function quantitChange(e){
    const input = e.target
    if (input.value <= 0){
        input = 1
    }
    updateShopCarTotal()

}

function compBtnClk(){

    shopCarPordCont.innerHTML=""
    updateShopCarTotal()
}
