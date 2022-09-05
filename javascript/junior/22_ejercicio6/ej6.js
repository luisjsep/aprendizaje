

/**script que pregunte al usuario cuánto indica el
 * termómetro y si ese valor se encuentra entre 18 y 27 
 * que le indique que la temperatura es 
 * agradable
 */

temperatura= parseInt(prompt('¿Cuánto indica el termómetro: ?'))

if (18<= temperatura && temperatura <=27)
{
    document.write('<h1>El clima es agradable</h1>');
}else if (temperatura < 18){
    document.write ('<h1>El clima es frío </h1>');
}else{
    document.write('<h1>El clima es caluroso </h1>');
}