const addToShopCarBtn = document.querySelectorAll("#addcar");

addToShopCarBtn.forEach((addToCarBtn) => {
    addToCarBtn.addEventListener("click", addToCarClick);
});
    
const shopCarPordCont=document.querySelector('.shopCarRow');
const compBtn =document.querySelector("#");
compBtn.addEventListener('click',compBtnClk)


function addToCarClick(e){
    const btn = e.target;
    const   prod = btn.closest('.comentarios');
    
    const   pordNon  = prod.querySelector('.titulo').textContent;
    const   prodPrice = prod.querySelector('.precio').textContent;
    const   prodDes= prod.querySelector('.descripcion').textContent;

    addProdShopCar(pordNon, prodPrice, prodDes );
}

function addProdShopCar(pordNon, prodPrice, prodDes ){

    const elemTtl = shopCarPordCont.getElementsByClassName(".shopCarElmTitle")
for ( let i=0; i< elemTtl.length ; i++ ){
    if(elemTtl(i).innerText == pordNon ){
        let elemQaun = elemTtl[i].parentElement.parentElement.querySelector("#")
    }
    elemQaun.value++
    return
}

    const shopCarRow=document.createElement('div');
    const shopCarCont = `
                <div class="container">
                <div class="row">
                <div class="col-9"><B>${pordNon}</B></div>
                <div class="col-4"><img src="img/cafe_helado.jpg" class="img-thumbnail"><br>${prodPrice}</div>
                <div class="col-4">${prodDes}</div>
                <div class="col-2">
                    <select class="form-select"  aria-label=".bg-success">
                        <option selected>cantidad</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                    </select>  
                    </div>
                <a href="#" class="col-2"><img src="img/basura.png"alt="" width="20" height="20"> </a>
                </div>
                `

                // shopCarRow.innerHTML = shopCarCont;
                // shopCarPordCont.append(shopCarRow);
            
                // shopCarRow
                // .querySelector('btnDel')
                // .addEventListener('click',remShopCarProd);

                // shopCarRow
                // .querySelector('shopCarProdCuantit')
                // .addEventListener('change',(quantitChange);
                
                // updateShopCarTotal();
}


// function  updateShopCarTotal(){
//     let total= 0;

//     const shopcartotal= documet.querySelector('#');
//     const shopCarProd =documetn.querySelectorAll("shopCarProd");
    
//     shopCarProd.forEach((shopCarPord)=>{
//         const shopCarPriceElem = shopCarPord.querySelector(".shopCarPordPrice");
    
//         const shopCarPrice = number(shopCarPriceElem.textContent.replace('$',""));
//         const shoppingcarpordCuantityelement=shopCarProd.queryselector('#');
//         const shoppingcarpordCuantit= number(shoppingcarpordCuantityelement.value);
//         total = total + shopCarPrice * shoppingcarpordCuantit;
//     });
    
//     shopcartotal.innerHTML = ${total};
// }


// function remShopCarProd (e){
//     const btnClk = e.target;
//     btnClk.closest('.shopCarPord').remove();
//     updateShopCarTotal();
// }
// function quantitChange(e){
    
//     const input = e.target;

//     if input.value <= 0 ? (input.value = 1) : null;
//     updateShopCarTotal();

// }

// function compBtnClk(){

//     shopCarPordCont.innerHTML="";
//     updateShopCarTotal();
// }
