document.getElementById('region').addEventListener('change', function() {
  var regionId = this.value;
  if (regionId) {
    fetch(`/cargar_comunas/?region_id=${regionId}`)
      .then(response => response.json())
      .then(data => {
        var comunaSelect = document.getElementById('comuna');
        comunaSelect.innerHTML = '<option value="">Selecciona una comuna</option>';  // Resetear las opciones
        data.forEach(function(comuna) {
          var option = document.createElement('option');
          option.value = comuna.id;
          option.textContent = comuna.nombre;
          comunaSelect.appendChild(option);
        });
      });
  } else {
    // Si no se selecciona región, limpiar las comunas
    document.getElementById('comuna').innerHTML = '<option value="">Selecciona una comuna</option>';
  }
});