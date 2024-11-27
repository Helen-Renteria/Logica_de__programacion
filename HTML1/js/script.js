function mostrarDetalles(libro) {
    const detalles = {
      arte: "Autor: Donald Knuth. Año: 1968. Descripción: Obra maestra sobre algoritmos.",
      universo: "Autor: Carl Sagan. Año: 1980. Descripción: Misterios y maravillas del universo.",
      soledad: "Autor: Gabriel García Márquez. Año: 1967. Descripción: Realismo mágico.",
      ciberseguridad: "Autor: Helen Farina Rentería. Año: 2024. Descripción: Tu guía inicial."
    };

    alert(detalles[libro] || "Detalles no disponibles.");
}
let index = 0;

function moverCarousel(direction) {
    const images = document.querySelectorAll('.carousel img');
    images[index].classList.remove('active');
    index = (index + direction + images.length) % images.length;
    images[index].classList.add('active');
}