/**Declaración e inicialización
 * condición
 * iteración / aumento - decremento
 */

let numero=0;
document.write("<h2>numero=0; y numero++  ");
document.write("<br>numero++ se suma luego de ejecutar la línea: <br>");
document.write(numero++);
document.write("<br> línea siguiente: ");
document.write(numero);

document.write ("<br><br>");
document.write("Ejecturar en la misma línea: ");
document.write(++numero);

document.write("<br><br><br>Ciclo for <br>");

for (let i=0; i<6; i++){
    document.write(i + "<br>")
}

document.write("<br>Otra forma<br>");
//otro forma ciclo

let i=6
for (i; i>=0; i--){
    document.write(i + "<br>")
}

