function correovalido(correo){
    return /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(correo)
}

$(document).ready(function(correo){

    $('#oculto-1').hide()

    if(correo === ''){
        $('#oculto-1').show()
    }else{
        $('#oculto-1').hide()
    }

})