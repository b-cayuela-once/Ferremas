// Menú hamburguesa
document.getElementById('menu-toggle').addEventListener('click', () => {
  document.getElementById('nav-links').classList.toggle('active');
});

// Simulación de búsqueda
function buscar() {
  const input = document.getElementById("busqueda-input").value.toLowerCase();
  const productos = document.querySelectorAll(".producto");

  productos.forEach(p => {
    if (p.textContent.toLowerCase().includes(input)) {
      p.style.display = "block";
    } else {
      p.style.display = "none";
    }
  });
}
