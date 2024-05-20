$(document).ready(function() 
{

   // alert("Hola");
insertar_registro();


}
)
function insertar_registro()
{
$(document).on('click', '#btn_register', function() 


{
var nombre = $('#nombre').val();
var apellido= $('#apellido').val();
var calle= $('#calle').val();
var numero= $('#numero').val();
var ciudad= $('#ciudad').val();
var codearea= $('#codearea').val();
var numtelefono= $('#numtelefono').val();
var email= $('#email').val();
var edad= $('#edad').val();
var fechadenacimiento= $('#fechadenacimiento').val();
var genero= $('#genero').val();

if(nombre == "" || apellido == "" || calle == ""   || numero == ""  || ciudad == "" ||  email == ""  || edad == "" || fechadenacimiento == "" || genero == "" ) 
{
    $('#Mensaje').html ("Llenar los campos en blanco");
}
else
{

    $.ajax(
        {
            URL: 'insertar.php',
            method: 'post',
            data: {Unombre:nombre, Uapellido:apellido, Ucalle:calle, Unumero:numero, Uciudad:ciudad, Ucodearea:codearea, Unumtelefono:numtelefono, UEmail:email, Uedad:edad, Ufechadenacimiento:fechadenacimiento, Ugenero:genero},
            success: function (data)
        {
            $('#Mensaje').html (data);
           //$('#Mensaje').html ('Se Inserto Bien');

           // $('#Registration').modal ('show');
           // $('form').trigger ('reset')
           // Mostrar_registro();

           //alert("Entro a la funcion");
          // alert(data);

        } 



        }
    )
}
})
}



