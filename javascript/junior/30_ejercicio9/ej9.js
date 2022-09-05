
//_crear un mini-sistema que nos permita registrar
//los alumnos que estan presentes (P) y ausentes (A) en clase.
//_Pasados los 30 días mostrar la situación final de todos los alumnos (presentes y asusentes).
//_Se puede tener un maximo de 10% de ausencias por semestre, se se tienes más estas reprobado.


//[Nombre_alumnos] [Asistencias]

let cantidad = prompt ("¿Cuantos alumnos son?");
//se declara el array
let alumnosTotales=[];
//elegir la cantidad de alumnos
for (i=0; i<cantidad; i++)
{
alumnosTotales[i]= [prompt("Nombre del alumno " + (i +1)),0];
}

const tomarAsistencia= (nombre, p)=>{
    let presencia = prompt('Dia '+(i+1)+'-----'+' Escribe "P" para dejar presente a '+nombre);
    if (presencia == "p" || presencia == "P")
        {   //se suma 1 si esta presente.
        alumnosTotales[p][1]++;
        }  
}

//30 son los días del mes
for (i=0; i<30; i++){   
    for(alumno in alumnosTotales){
        tomarAsistencia(alumnosTotales[alumno][0], alumno);  
         }

}

//días ausentes, días presentes
//El ciclo se repetirá según el número de alumnos
for (alumno in alumnosTotales){
    let resultado= `${alumnosTotales[alumno][0]}: <br>
    ____Presentes: ${alumnosTotales[alumno][1]} <br>
    ____Ausencias: ${30 - alumnosTotales[alumno][1]}`;
    if (30 - alumnosTotales[alumno][1] >18){
        resultado+="<b style='color:red'>Reprobado por inasistencia</b><br><br>";
    }else{
        resultado+="<br><br>";
    }
    document.write(resultado);
}