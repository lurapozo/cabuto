$("#limpiarCampos-btn").click(function() {
	limpiarCampos()
})

$("#guardar-btn").click(function() {
	if (verificarCampos()) {
	    alert("Guardado o Actualización Exitosa");
		$("#form").submit()
	}
})

function limpiarCampos() {
	var inputs = $(".input")
	//LIMPIANDO INPUTS
	inputs.each(function() {
		$(this).val("")
	})
}

function verificarCampos() {
	var verificacion = true
	var inputs = $(".input")
	//VERIFICANDO CADA CAMPO
	inputs.each(function() {if ($(this).val() == "") {verificacion = false}})

	//DISPARANDO ALERTA SI ES NECESARIA
	if (! verificacion) {alert("Por favor ingrese toda la información requerida.")}
	return verificacion
}

function abrir_agregar_producto(url){
    $('#agregar').load(url, function(){
      $(this).modal('show');
    });
}


$(document).on("click", ".btn-modal", function (e) {
    e.preventDefault();
    var $popup = $("#popup");
    var popup_url = $(this).data("popup-url");
    $(".modal-body", $popup).load(popup_url, function () {
      $popup.modal("show");
    });
  });

var modal = document.querySelector(".modal")
var btn = document.querySelector(".btn")
function toggleModal() {
        modal.classList.toggle("show-modal");
    }

function windowOnClick(event) {
        if (event.target === modal) {
            toggleModal();
        }
    }
window.addEventListener("click", windowOnClick);
