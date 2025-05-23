function cambiarDificultad(dificultad) {
    fetch('http://127.0.0.1:8000/api/v1/dificultad', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({dificultad: dificultad})
    })
        .then(response => response.status)
        .then(status => {
            if (status === 200) {
                alert('Dificultad cambiada con exito');
            } else {
                alert('La dificultad no se pudo cambiar');
            }
            window.location.href = 'index.html';
        })
        .catch(error => {
            console.error('Error en la petición:', error);
        });
}
