
document.addEventListener("DOMContentLoaded", function() {
    const tabs = document.querySelectorAll('.option');
    const tabContentOption1 = document.getElementById('tabContentOption1');
  
    // Mostrar por defecto el contenido de tabContentOption1 y resaltar la opción correspondiente
    tabContentOption1.classList.add('content-active');
    document.getElementById('option1').classList.add('option-active');
  
    // Ocultar los otros tabContentOptions
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(content => {
      if (content.id !== 'tabContentOption1') {
        content.style.display = 'none';
      }
    });
  
    tabs.forEach(tab => {
      tab.addEventListener('click', function() {
        const tabContentId = this.id.replace('option', 'tabContentOption');
  
        // Ocultar todos los contenidos de tab
        tabContents.forEach(content => {
          content.classList.remove('content-active');
        });
  
        // Mostrar el contenido del tab seleccionado
        document.getElementById(tabContentId).classList.add('content-active');
  
        // Ocultar los tabContentOptions que no correspondan a la opción seleccionada
        tabContents.forEach(content => {
          if (content.id !== tabContentId) {
            content.style.display = 'none';
          } else {
            content.style.display = 'block';
          }
        });
  
        // Resaltar el tab activo y desactivar los demás
        tabs.forEach(tab => {
          tab.classList.remove('option-active');
        });
        this.classList.add('option-active');
      });
    });
  });


// Función para abrir la barra lateral solo cuando se presiona la opción de reservar
function abrirBarraLateral() {
  var barraLateral = document.querySelector('.barra-lateral');
  barraLateral.style.display = 'block';
  localStorage.setItem('barraLateral', 'visible');
}

// Función para cerrar la barra lateral
function cerrarBarraLateral() {
  var barraLateral = document.querySelector('.barra-lateral');
  barraLateral.style.display = 'none';
  localStorage.setItem('barraLateral', 'oculta');
}

// Función para abrir y cerrar la barra lateral
function toggleBarraLateral() {
  var estadoBarraLateral = localStorage.getItem('barraLateral');

  if (estadoBarraLateral === 'visible') {
    cerrarBarraLateral();
  } else {
    abrirBarraLateral();
  }
}

// Verificar el estado de la barra lateral al cargar la página
window.onload = function() {
  var estadoBarraLateral = localStorage.getItem('barraLateral');
  var barraLateral = document.querySelector('.barra-lateral');

  if (!estadoBarraLateral || estadoBarraLateral === 'oculta') {
    // Si no hay un estado almacenado o está oculta, no hacemos nada
    barraLateral.style.display = 'none';
  } else {
    // Si el estado es visible, mostramos la barra lateral
    barraLateral.style.display = 'block';
  }
};

// Evento para abrir la barra lateral cuando se presiona la opción de reservar
var botonReservar = document.getElementById('boton-reservar');
botonReservar.addEventListener('click', abrirBarraLateral);







  
  
  
  
  