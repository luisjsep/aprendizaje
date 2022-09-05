

let animales = ["gato", "perro", "tiranosaurio rex"];
animales.tamano="grande";
document.write("<h3>For in <br>");

for (animal in animales){
    document.write(animal + "<br>");
}

document.write("<br></br>");
document.write("For of <br>")
for (animal of animales){
    document.write(animal + "<br>");
}

document.write("<h3>Visualizar contenido con For in <br>");

for (animal in animales){
    document.write(animales[animal] + "<br>");
}