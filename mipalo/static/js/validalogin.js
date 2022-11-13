var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate(){
var username = document.getElementById("email").value;
var password = document.getElementById("pass").value;
var boton = document.getElementById("boton").value;
if ( username == "admin" && password == "admin123"){
alert ("Datos Correctos");
window.location.href = "index/"; //Redireccion.
return false;
}
else{
attempt --;// Decrementa uno 
alert("Quedan "+attempt+" intentos");
// Se bloquea los campos
if( attempt == 0){
alert("Se han superado los intentos, recargue la pagina para volver a intentar o registrese");
document.getElementById("email").disabled = true;
document.getElementById("pass").disabled = true;
document.getElementById("boton").disabled = true;
return false;
}
}
}