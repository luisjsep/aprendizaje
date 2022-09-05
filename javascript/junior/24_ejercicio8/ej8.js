

/**Script  que muestre el menú con los nombres
 * de distintos países de América y si el usuario selecciona
 * alguna de las opciones se le mostrará
 * el nombre de la capital de este país
 */

const MEXICO=1;
const URUGUAY=2;
const COLOMBIA=3;
const ARGENTINA=4;
const ECUADOR=5;
const PERU=6;

opc=parseInt(prompt(`         Capitales de América
1) México
2) Uruguay
3) Colombia
4) Argentina
5) Ecuador
6) Perú
`));

if (opc == MEXICO)
    document.write('<h1>Ciudad de México</h1>');
else if(opc == URUGUAY)
    document.write('<h1>Montevideo</h1>');
else if(opc == COLOMBIA)
    document.write('<h1>Bogota</h1>');
else if(opc == ARGENTINA)
    document.write('<h1>Buenos Aires</h1>');
else if(opc == ECUADOR)
    document.write('<h1>Quito</h1>');
else if(opc ==  PERU)
    document.write('<h1>Lima</h1>');
else{
        document.write('Opción no válida');
    }
   


document.write(opc);