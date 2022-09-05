/**script que solicite la calificación y cantidad 
 * de asistencias a un curso. Si la calificación es mayor 
 * o igual que 60 y la asistencias son mayor que 20
 * entonces ha indicar que ha aprobado el curso
 */

document.write('Aprobar<br>');
document.write('Califaciones >= 60<br>');
document.write('Asistencia >= 20')


calificacion= parseFloat(prompt('Ingrese calificación: '));
asistencias= parseFloat(prompt('Ingrese asistencia: '));

if (calificacion >= 60 && asistencias >=20)
{
    document.write('<h2>Felicidades aprobaste el curso</h2>');
    if (calificacion >= 95)
      document.write('<h2>Estudiante sobresaliente. Pídele un beca a Boric...</h2>');
}else{
    document.write('<h2>Lo siento. Debes esforzarte más..</h2>');
}