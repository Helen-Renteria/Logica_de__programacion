/*Escribe una función que reciba un número y verifique si es par o impar.
Muestra el resultado en la consola.
*/

function Npar(x){

    if (x % 2 == 0) {
        resultado = "Es un numero par"; 
    }
    else{
        resultado = "Es un munero impar";
    }
    return resultado;
}
do{

    let x;
    let resultado;
    x = prompt("ingrese el numero que desea verificar");
    


let rest = Npar(x); 
alert(rest);


var contn = prompt("si desea intentarlo de nuevo ingrese el 1 si no otro numero");
}while(contn == "1"); 