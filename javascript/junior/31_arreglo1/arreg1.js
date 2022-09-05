
/**
 * algunas personas definen los arreglos 
 * como constantes ya que este seguira siendo un
 * arreglo durante todo el programa
 */
const a=[];
const b =[1, true, "Hola", ["A", "B", "C", [1,2,3]]];
document.write(a);
document.write(b);
document.write('<br></br>');
//largo del array
document.write(b.length);

document.write('<br></br>');
document.write(b[2]);
document.write('<br></br>');
document.write(b[0]);
document.write('<br></br>');
document.write(b[3]);
document.write('<br></br>');
document.write(b[3][2]);
document.write('<br></br>');
document.write(b[3][3][0]);
document.write('<br></br>');

//accediendo al objeto Array
const c = Array.of("X", "Y", "Z", 9,8,7);
document.write(c);

document.write('<br></br>');
const d=Array(100).fill(false);
document.write(c);


/**Forma antigua */
document.write('<br></br>');
const e=new Array();
document.write(e);

/**Inicializar en forma antigua */
const f = new Array(1,2,3, true, false);
document.write(f);



const colores=["Rojo", "Verde", "Azul"];
document.write(colores);
/**Agregar un elemento */
colores.push("Negro");
document.write(colores);
//elimina un elemento al final
colores.pop();
document.write(colores);

