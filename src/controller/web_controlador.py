from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.model.juego import Juego
from src.model.diccionario_file import DiccionarioFile


class LetraInput(BaseModel):
    letra: str


class DificultadInput(BaseModel):
    dificultad: str


class WebControlador:
    def __init__(self):
        self.router = APIRouter(prefix="/api/v1")
        self.juego = Juego(DiccionarioFile())
        self.__registrar_rutas()

    def __registrar_rutas(self):
        @self.router.post("/iniciar")
        def iniciar_partida():
            return {"letras": self.juego.iniciar_partida()}

        @self.router.get("/intentos_permitidos")
        def obtener_intentos_permitidos():
            return {"intentos_permitidos": self.juego.calcular_intentos_permitidos()}

        @self.router.get("/intentos_realizados")
        def obtener_intentos_realizados():
            return {"intentos_realizados": self.juego.obtener_intentos_realizados()}

        @self.router.get("/hay_intentos")
        def verificar_si_hay_intentos():
            return {"hay_intentos": self.juego.verificar_si_hay_intentos()}

        @self.router.get("/hay_triunfo")
        def verificar_si_hay_triunfo():
            return {"hay_triunfo": self.juego.verificar_triunfo()}

        @self.router.post("/adivinar")
        def adivinar_letra(letra_input: LetraInput):
            letra = letra_input.letra.strip().upper()
            if not letra or not letra.isalpha() or len(letra) != 1:
                raise HTTPException(status_code=400, detail="Letra inválida")
            return {"posiciones_encontradas": self.juego.adivinar(letra)}

        @self.router.post("/dificultad")
        def modificar_dificultad(data: DificultadInput):
            if data.dificultad.lower() != "facil" and data.dificultad.lower() != "medio" and data.dificultad.lower() != "dificil":
                raise HTTPException(status_code=400, detail="Dificultad inválida. Use: facil, medio, dificil.")
            if data.dificultad.lower() == "facil":
                self.juego.modificar_dificultad(Juego.DIFICULTAD_BAJA)

            if data.dificultad.lower() == "medio":
                self.juego.modificar_dificultad(Juego.DIFICULTAD_MEDIA)
            if data.dificultad.lower() == "dificil":
                self.juego.modificar_dificultad(Juego.DIFICULTAD_ALTA)
            return {"mensaje": "Dificultad modificada correctamente"}
