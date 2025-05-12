document.addEventListener('DOMContentLoaded', function () {
  const regionSelect = document.getElementById('region');
  const comunaSelect = document.getElementById('comuna');

  // Al cambiar la región, obtener las comunas desde el backend
  regionSelect.addEventListener('change', function () {
    const regionId = this.value;

    if (!regionId) {
      comunaSelect.innerHTML = '<option value="">Selecciona una comuna</option>';
      return;
    }

    fetch(`/login/ajax/cargar-comunas/?region_id=${regionId}`)
      .then(response => response.json())
      .then(data => {
        comunaSelect.innerHTML = '<option value="">Selecciona una comuna</option>';
        data.forEach(comuna => {
          const option = document.createElement('option');
          option.value = comuna.id;
          option.textContent = comuna.nombre;
          comunaSelect.appendChild(option);
        });
      })
      .catch(error => {
        console.error('Error al cargar comunas:', error);
      });
  });

  // Disparar una carga inicial si ya hay una región seleccionada (opcional)
  if (regionSelect.value) {
    regionSelect.dispatchEvent(new Event('change'));
  }
});
