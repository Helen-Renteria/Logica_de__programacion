const x=document.querySelector('#x')
const y=document.querySelector('#y')
cambiar()

window.addEventListener('resize', cambiar)
function cambiar(){
    x.textContent=window.innerWidth
    y.textContent=window.innerHeight
}