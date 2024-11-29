const form = document.querySelector('#form');
//console.log(form)  es para verificar si se capturo el formulario

form.addEventListener('submit', (event)=> {
    event.preventDefault();
    let curso = document.querySelector('#curso').value;
    let duracion = document.querySelector('#duracion').value;  
    console.log(curso, duracion);
})
