$(function(){
    $("#mis-datos").validate({
        rules:{
            nombre:{
                required:true
            },
            apellidos:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            telefono:{
                required:true,
                number:true
            },
            pass1:{
                required:true
            },
            pass2:{
                required:true,
                equalTo:'#pass1'
            },
        },
        messages:{
            nombre:{
                required:'Ingresar nombre',
                minlength:'Caracteres insuficientes'
            },
            apellidos:{
                required:'Ingresar apellidos',
                minlength:'Caracteres insuficientes'
            },
            correo:{
                required:'Ingresar correo válido',
                email:'Formato de correo inválido'
            },
            telefono:{
                required:'Ingresar número de teléfono',
                minlength:'Dígitos insuficientes',
                number:'Sólo ingresar números'
            },
            pass1:{
                required:'Ingresar contraseña',
                minlength:'Mínimo 8 caracteres'
            },
            pass2:{
                required:'Repetir contraseña',
                minlength:'Mínimo 8 caracteres',
                equalTo:'Contraseñas no coinciden'
            },
        },
     })
});