

/**
 * script en python que calcula el área de un triángulo.
 * El usuario deberá ingresar tanto el valor
 * de la base como el de la altura y el programa
 * mostrará el valor del área
 */


alert('VAMOS A CALCULAR EL ÁREA DE UN TRIÁNGULO');
base= parseFloat(prompt("Ingrese base: "));
altura=parseFloat(prompt("Ingrese altura: "));

area= (base * altura) / 2;

document.write("<h2>El área del triángulo es: "+area+ "</h2>");


