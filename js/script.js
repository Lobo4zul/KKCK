$(document).ready(function(){

    //conteo validaciones
    let mail = 0
    let ed = 0
    let pass = 0

    // validaciones

    $('#contraseña').on('input', function(){
        let contra = $('#contraseña').val().length

        if(contra >= 8){
            $('#contraseña').removeClass("is-invalid")
            $('#contraseña').addClass("is-valid")
            $('#validacion').text('')
            pass = +1
        }else{
            $('#contraseña').addClass("is-invalid")
            $('#validacion').text('Debe tener por lo menos 8 caracteres')
        }
    })

    $('#edad').on('input', function(){

        let edad = $('#edad').val()

        if(edad >= 18){
            $('#edad').removeClass("is-invalid")
            $('#edad').addClass("is-valid")
            ed = +1
        }else{
            $('#edad').addClass("is-invalid")
        }
    })

    $('#correo').on('input', function(){

        let re = /([A-Z0-9a-z_-][^@])+?@[^$#<>?]+?\.[\w]{2,4}/.test(this.value);

        if(!re){
            $('#correo').addClass("is-invalid")
            $('#validacion-1').text('Ingrese un correo valido')
        }else{
            $('#correo').removeClass("is-invalid")
            $('#correo').addClass("is-valid")
            $('#validacion-1').text('')
            mail = +1
        }
    })
    $('#registro').click(function(){

        let nombre = $('#nombre').val().length
        let apellido = $('#apellido').val().length
        let user = $('#usuario').val().length

        if(nombre == '' || apellido == '' || user == '' || mail == 0 || pass == 0 || ed == 0){
            const Toast = Swal.mixin({
                toast: true,
                position: "top-end",
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                  toast.onmouseenter = Swal.stopTimer;
                  toast.onmouseleave = Swal.resumeTimer;
                }
              });
              Toast.fire({
                icon: "error",
                title: "Verificar datos ingresados!"
              });
        }else{

            const Toast = Swal.mixin({
                toast: true,
                position: "top-end",
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                  toast.onmouseenter = Swal.stopTimer;
                  toast.onmouseleave = Swal.resumeTimer;
                }
              });
              Toast.fire({
                icon: "success",
                title: "Registro Exitoso!"
              });

              setTimeout(() => {
                window.location.reload();
            }, 3000);
        }
    })


    })