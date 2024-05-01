$(document).ready(function() 
{

    alert("Hola");
insertar_registro();


}
)
function insertar_registro()
{
$(document).on('click', '#btn_register', function() 

{
var user = $('#nombre').val();
var email= $('#email').val();
var apellido= $('#apellido').val();
var dni= $('#dni').val()
var fechadenacimiento= $('#fechadenacimiento').val();
var contrasena= $('#Contrasena').val();
var repetir= $('#Repetir').val ();

if(nombre == "" || email == "")
{
    $('#Mensaje').html ("Llenar los campos en blanco");
}
else
{

    $.ajax(
        {
            URL: 'insertar.php',
            method: 'post',
            data: {Uname:user, UEmail:email, Uapellido:apellido, Udni:dni, Ufechadenacimiento:fechadenacimiento, Ucontrasena:contrasena, Urepetir:repetir},
            success: function (data)
        {
            $('#Mensaje').html (data);
           //$('#Mensaje').html ('Se Inserto Bien');

           // $('#Registration').modal ('show');
           // $('form').trigger ('reset')
           // Mostrar_registro();

           alert("Entro a la funcion");
           alert(data);

        } 



        }
    )
}
})
}
