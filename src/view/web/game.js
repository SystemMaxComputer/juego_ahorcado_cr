async function realizarIntento() {
    letra = document.getElementById('letra_input').value;
    if (letra.length !== 1) {
        alert("Debe ingresar una sola letra")
        return
    }

    const posiciones = await adivinarLetra(letra);

    const palabraLayout = document.querySelector(".palabra_layout")
    palabraLayout.childNodes.forEach((label, index) => {
        if (posiciones.includes(index)) {
            label.textContent = letra.toUpperCase();
        }
    })
    await actualizarDisplayIntentos()

    if (!await verificarSiHayIntentos()) {
        alert("Perdiste! No hay más intentos")
        window.location.href = "index.html"
        return
    }
    if (await verificarSiHayTriunfo()) {
        alert("Ganaste! Adivinaste la palabra")
        window.location.href = "index.html"
        return
    }

    document.getElementById('letra_input').value = "";
}

async function actualizarDisplayIntentos() {
    const response_intentos_permitidos = await fetch('http://127.0.0.1:8000/api/v1/intentos_permitidos', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    const responseBodyIntentosPermitidos = await response_intentos_permitidos.json();
    const intentos_permitidos = responseBodyIntentosPermitidos.intentos_permitidos;
    const responseIntentosRealizados = await fetch('http://127.0.0.1:8000/api/v1/intentos_realizados', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    const responseBodyIntentosRealizados = await responseIntentosRealizados.json();
    const intentos_realizados = responseBodyIntentosRealizados.intentos_realizados;
    document.getElementById("display_intentos").textContent = (intentos_permitidos - intentos_realizados) + "/" + intentos_permitidos;
}


async function verificarSiHayTriunfo() {
    try {

        const response = await fetch('http://127.0.0.1:8000/api/v1/hay_triunfo', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        const responseBody = await response.json();
        return responseBody.hay_triunfo;
    } catch (error) {
        return []
    }
}

async function verificarSiHayIntentos() {
    try {

        const response = await fetch('http://127.0.0.1:8000/api/v1/hay_intentos', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        const responseBody = await response.json();
        return responseBody.hay_intentos;
    } catch (error) {
        return false
    }
}

async function adivinarLetra(letra) {
    try {

        const response = await fetch('http://127.0.0.1:8000/api/v1/adivinar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({letra: letra})
        })
        const responseBody = await response.json();
        return responseBody.posiciones_encontradas;
    } catch (error) {
        console.log("error en la peticion", error)
        return []
    }
}

document.addEventListener("DOMContentLoaded", function () {
    actualizarDisplayIntentos()
    fetch('http://127.0.0.1:8000/api/v1/iniciar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(response => response.json())
        .then(responseBody => {
            const numeroDeLetras = responseBody.letras;
            const palabraLayout = document.querySelector(".palabra_layout")
            while (palabraLayout.firstChild) {
                palabraLayout.removeChild(palabraLayout.firstChild);
            }
            for (let i = 0; i < numeroDeLetras; i++) {
                const label = document.createElement("label");
                label.textContent = "_";
                palabraLayout.appendChild(label);
            }
        })
        .catch(error => {
            console.error('Error en la petición:', error);
        });
});
