class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []
        self.estado = "detenido"
        self.indice_actual = -1

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def eliminar_cancion(self, cancion):
        if cancion in self.canciones:
            self.canciones.remove(cancion)

    def mostrar_canciones(self):
        if self.canciones:
            print("Canciones en la playlist:")
            for i, cancion in enumerate(self.canciones):
                print(f"{i + 1}. {cancion}")
        else:
            print("La playlist está vacía.")

    def reproducir(self):
        if not self.canciones:
            print("No hay canciones en la playlist.")
            return

        if self.estado == "detenido":
            self.indice_actual = 0
        self.estado = "reproduciendo"
        print(f"Reproduciendo: {self.canciones[self.indice_actual]}")

    def seleccionar(self, indice):
        if 0 <= indice < len(self.canciones):
            self.indice_actual = indice
            self.estado = "reproduciendo"
            print(f"Reproduciendo: {self.canciones[self.indice_actual]}")
        else:
            print("Índice no válido.")

    def pausar(self):
        if self.estado == "reproduciendo":
            self.estado = "pausa"
            print("Pausado.")
        else:
            print("No reproduce ninguna canción.")

    def detener(self):
        if self.estado == "reproduciendo" or self.estado == "pausa":
            self.estado = "detenido"
            print("Detenido.")
        else:
            print("No reproduce ninguna cancion.")

    def siguiente(self):
        if not self.canciones:
            print("No hay canciones en la playlist.")
            return

        if self.indice_actual < len(self.canciones) - 1:
            self.indice_actual += 1
            self.estado = "reproduciendo"
            print(f"Reproduciendo siguiente: {self.canciones[self.indice_actual]}")
        else:
            print("No hay más canciones en la playlist.")

    def cancion_anterior(self):
        if not self.canciones:
            print("No hay canciones en la playlist.")
            return

        if self.indice_actual > 0:
            self.indice_actual -= 1
            self.estado = "reproduciendo"
            print(f"Reproduciendo anterior: {self.canciones[self.indice_actual]}")
        else:
            print("Esta es la primera canción en la playlist.")

    def ver_estado(self):
        print(f"Estado actual: {self.estado}")

    def ver_cancion_actual(self):
        if self.indice_actual >= 0 and self.indice_actual < len(self.canciones):
            print(f"Canción actual: {self.canciones[self.indice_actual]}")
        else:
            print("No se está reproduciendo ninguna canción.")


mi_playlist = Playlist("Mi Lista de Reproducción")


while True:
    print(" Menú de playlist ")
    print("1. Agregar una canción")
    print("2. Eliminar canción")
    print("3. Mostrar canciones")
    print("4. Reproducir")
    print("5. Seleccionar canción")
    print("6. Pausar")
    print("7. Detener")
    print("8. Siguiente canción")
    print("9. Canción anterior")
    print("10. Ver estado")
    print("11. Ver canción actual")
    print("12. Salir")

    opcion = input("Elija una opción del menú: ")

    if opcion == "1":
        cancion = input("Ingrese el nombre de la canción: ")
        mi_playlist.agregar_cancion(cancion)
        print(f"{cancion} ha sido agregada a la playlist.")

    elif opcion == "2":
        mi_playlist.mostrar_canciones()
        indice = int(input("Ingrese el índice de la canción a eliminar: ")) - 1
        if 0 <= indice < len(mi_playlist.canciones):
            cancion_eliminada = mi_playlist.canciones[indice]
            mi_playlist.eliminar_cancion(cancion_eliminada)
            print(f"{cancion_eliminada} ha sido eliminada de la playlist.")
        else:
            print("Índice no válido.")

    elif opcion == "3":
        mi_playlist.mostrar_canciones()

    elif opcion == "4":
        mi_playlist.reproducir()

    elif opcion == "5":
        mi_playlist.mostrar_canciones()
        indice = int(input("Ingrese el índice de la canción a seleccionar: ")) - 1
        mi_playlist.seleccionar_cancion(indice)

    elif opcion == "6":
        mi_playlist.pausar()

    elif opcion == "7":
        mi_playlist.detener()

    elif opcion == "8":
        mi_playlist.siguiente_cancion()

    elif opcion == "9":
        mi_playlist.cancion_anterior()

    elif opcion == "10":
        mi_playlist.ver_estado()

    elif opcion == "11":
        mi_playlist.ver_cancion_actual()

    elif opcion == "12":
        print("Salir del programa...")
        break

    else:
        print("Opción no válida, elija una opción válida.")


del mi_playlist
