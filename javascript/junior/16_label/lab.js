
array1= ["maria", "josefa", "roberta"];
array2= ["pedro", "marcelo", array1, "marcela"];

for (let array in array2){
    if (array == 2){
        for (let array of array1)
        {
            document.write(array + " array1 <br>");
            break;

        }
    }else{
        document.write(array2[array] + "<br>");
    }
}


document.write("<br><br>");

document.write("Ejemplo con label: <br>");

continuar:
for (let array in array2){
    if (array == 2){
        for (let array of array1)
        {
            document.write(array + " array1 <br>");
            break continuar;

        }
    }else{
        document.write(array2[array] + "<br>");
    }
}

