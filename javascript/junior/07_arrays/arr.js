
let frutas = ["bananas", "manzana", "pera", 5, 9, "pedro"];

document.write(frutas[1]);

//array asociativo

let pc1 ={
    nombre: "LuisPC",
    procedador: "Intel core I7",
    ram: "16GB",
    espacio: "1TB"
};

document.write("<br>"+pc1["nombre"]);


let nombre = pc1 ["nombre"];
let procesador= pc1["procesador"];
let ram= pc1["ram"];
let espacio=pc1["ram"];


frase = `<br>El nombre de mi PC es: <b>${nombre}</b> <br>
        El procesador es: <b>${procesador}</b> <br>
        La memoria ram es: <b>${ram}</b> <br>
        El espacio en disco es de: <b>${espacio}</b> `

document.writeln(frase);