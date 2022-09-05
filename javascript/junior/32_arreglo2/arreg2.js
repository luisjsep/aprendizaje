
// El largo de los arrays es ilimitado

//Declarar array de forma antigua e ingresar un elemento
let frutas= new Array();
frutas[0]="Sandia";

document.write(frutas);



//Podemos especificar el largo del array, pero este largo no es determinante
//quiere decir que se pueden ingresar más elementos

document.write("<br><br>")
let numero = new Array(5);
numero[0]=5;
numero[1]=4;
numero[2]=6;
numero[3]=8;
numero[4]=9;

document.write(numero);
document.write ("<br>Largo: "+numero.length);
document.write("<br><br>")

//Agregando un elemento automaticamente 
//se modifica el largo del array
numero[30]=10;
document.write(numero);
document.write ("<br>Largo: "+numero.length);