$(function(){
    $("#mis-datos").validate({
        rules:{
            nombre:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            asunto:{
                required:true
            },
            consulta:{
                required:true
            },
        },
        messages:{
            nombre:{
                required:'Ingresar nombre',
                minlength:'Caracteres insuficientes'
            },
            correo:{
                required:'Ingresar correo válido',
                email:'Formato de correo inválido'
            },
            asunto:{
                required:'Ingresar asunto'
            },
            consulta:{
                required:'Ingresar consulta'
            },
        },
     })
});