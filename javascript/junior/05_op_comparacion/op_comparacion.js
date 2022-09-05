
/** OPERADORES DE COMPARACIÓN
 * Los operadores de compración comparnan 
 * dos expresiones y duevelven un valor boolean que
 * represnta la relación de sus valores 
 * 
 * Devuelven true o false
 */

let numero1=23;
let numero2=13;
let texto1= "23";
let texto2= "texto 2";

//compara igualdad o desigualdad
document.write('¿23 es igual a "23"? ');
document.write (numero1 == texto1);
document.write ("<br>");

document.write('¿23 es distinto de "23"? ');
document.write (numero1 != texto1);
document.write ("<br>");

//compara igualdad desigualdad de valor y tipo de datos
document.write ('¿"23"  es estrictamente igual a 23? ');
document.write (texto1 === numero1);

//estrictamente distinto
document.write ("<br>");
document.write('¿"23" es estrictamente distinto a 23? ');
document.write (texto1 !== numero1);

