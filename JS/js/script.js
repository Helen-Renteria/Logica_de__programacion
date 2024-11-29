/*let temperatura = 30; 
if(temperatura>=30){
    console.log("hace mucho calor.");

}else if(temperatura>=20){
    console.log("el clima esta agradable."); 
}else{
    console.log("hace frio. "); 
} */
/*
const mascota = "perro";
switch(mascota){
    case "lagarto":
        console.log("tengo un lagarto");
        break; 
    case "leon":
        console.log("tengo un lagarto");
        break; 
    case "perro":
        console.log("tengo un lagarto");
        break; 
    default: 
    console.log("no tengo mascota");
    
}
*/
// ternario 
// condicion? valorsiesvedadero: calorsiesfalso
/*let edad=20;
let resultado= (edad>=18)?"mayor de edad": "menor de edad";
console.log(resultado);
*/
/*
let numero= 7; 
let tipo= (numero % 2===0)? "par": "impar"; 
console.log(tipo);
*//*
const array = [1,2,3,4,5]; 
for (let i=0; i < array.length; i++){
    console.log(array[i]); 
}*/

const mi_parrafo =document.getElementById("mi_parrafo"); 
const  boton_cambiar_texto= document.querySelector
("#boton_cambiar_texto");
const boton_agregar_texto=document.getElementById
("boton_agregar_texto");
const contenedor = document.getElementById("contenedor");

boton_cambiar_texto.addEventListener("click", ()=>{
    mi_parrafo.textContent="hola amigos";
}); 

boton_agregar_texto.addEventListener("click",()=>{
    const nuevo_parrafo= document.createElement("p");
    nuevo_parrafo.textContent="este parrafo no exixtia";
    contenedor.appendChild(nuevo_parrafo);
});

// confirmar de que color esta el texto
// si esta de un color cambiarlo al otro
// variable para guardar el color a comparar
boton_cambiar_color.addEventListener("click", ()=>{
    let colr = "red";

    if(mi_parrafo.style.color == colr){
        mi_parrafo.style.color = "black";

    } else{
        mi_parrafo.style.color = "red";
    }

}); 

