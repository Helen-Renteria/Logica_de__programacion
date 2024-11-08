function Npar(x) {
    if (x % 2 == 0) {
        return "Es un número par"; 
    } else {
        return "Es un número impar";
    }
}

do {
    let x = prompt("Ingrese el número que desea verificar:");
    let rest = Npar(parseInt(x)); // Convertimos la entrada a número
    alert(rest);

    var contn = prompt("Si desea intentarlo de nuevo ingrese '1', de lo contrario ingrese otro número");
} while (contn == "1");
