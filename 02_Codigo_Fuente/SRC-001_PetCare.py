# SRC-001 - Gestión de Propietarios, Mascotas y Consultas
# Proyecto: PetCare
# Categoria: Implementación
# Versión: 1.0
# Estado: Aprobado para línea base inicial
# Fecha: 04/10/2026
# Responsable: Equipo PetCare
# Ubicación: 02_Codigo_Fuente/SRC-001_PetCare.py

from datetime import date


class Propietario:
    def __init__(self, identificacion, nombre_completo, telefono):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.telefono = telefono

    def mostrar_informacion(self):
        return {
            "identificacion": self.identificacion,
            "nombre_completo": self.nombre_completo,
            "telefono": self.telefono,
        }


class Mascota:
    def __init__(self, id_mascota, nombre, especie, raza, identificacion_propietario):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.identificacion_propietario = identificacion_propietario

    def mostrar_informacion(self):
        return {
            "id_mascota": self.id_mascota,
            "nombre": self.nombre,
            "especie": self.especie,
            "raza": self.raza,
            "identificacion_propietario": self.identificacion_propietario,
        }


class Consulta:
    def __init__(self, id_consulta, id_mascota, fecha, veterinario, motivo, observaciones):
        self.id_consulta = id_consulta
        self.id_mascota = id_mascota
        self.fecha = fecha
        self.veterinario = veterinario
        self.motivo = motivo
        self.observaciones = observaciones

    def mostrar_informacion(self):
        return {
            "id_consulta": self.id_consulta,
            "id_mascota": self.id_mascota,
            "fecha": self.fecha,
            "veterinario": self.veterinario,
            "motivo": self.motivo,
            "observaciones": self.observaciones,
        }


# Almacenamiento en memoria (versión mínima)
propietarios = {}
mascotas = {}
consultas = {}


def _validar_obligatorios(**campos):
    for nombre, valor in campos.items():
        if valor is None or str(valor).strip() == "":
            raise ValueError(f"El campo '{nombre}' es obligatorio")


def registrar_propietario(identificacion, nombre_completo, telefono):
    _validar_obligatorios(
        identificacion=identificacion,
        nombre_completo=nombre_completo,
        telefono=telefono,
    )
    if identificacion in propietarios:
        raise ValueError("Ya existe un propietario con esa identificación")
    propietario = Propietario(identificacion, nombre_completo, telefono)
    propietarios[identificacion] = propietario
    return propietario


def registrar_mascota(id_mascota, nombre, especie, raza, identificacion_propietario):
    _validar_obligatorios(
        id_mascota=id_mascota,
        nombre=nombre,
        especie=especie,
        raza=raza,
        identificacion_propietario=identificacion_propietario,
    )
    if identificacion_propietario not in propietarios:
        raise ValueError("El propietario no existe")
    if id_mascota in mascotas:
        raise ValueError("Ya existe una mascota con ese código")
    mascota = Mascota(id_mascota, nombre, especie, raza, identificacion_propietario)
    mascotas[id_mascota] = mascota
    return mascota


def programar_consulta(id_consulta, id_mascota, fecha, veterinario, motivo, observaciones):
    _validar_obligatorios(
        id_consulta=id_consulta,
        id_mascota=id_mascota,
        fecha=fecha,
        veterinario=veterinario,
        motivo=motivo,
        observaciones=observaciones,
    )
    if id_mascota not in mascotas:
        raise ValueError("La mascota no existe")
    if id_consulta in consultas:
        raise ValueError("Ya existe una consulta con ese código")
    try:
        date.fromisoformat(fecha)
    except ValueError:
        raise ValueError("La fecha debe tener formato AAAA-MM-DD")
    consulta = Consulta(id_consulta, id_mascota, fecha, veterinario, motivo, observaciones)
    consultas[id_consulta] = consulta
    return consulta


def consultar_historial(id_mascota):
    if id_mascota not in mascotas:
        raise ValueError("La mascota no existe")
    historial = [c for c in consultas.values() if c.id_mascota == id_mascota]
    historial.sort(key=lambda c: (c.fecha, c.id_consulta))
    return [c.mostrar_informacion() for c in historial]


if __name__ == "__main__":
    registrar_propietario("1001", "Carlos Ramírez", "3001234567")
    registrar_mascota("M-01", "Luna", "Perro", "Labrador", "1001")
    programar_consulta("C-02", "M-01", "2026-10-15", "Dra. Gómez", "Vacunación", "Vacuna aplicada")
    programar_consulta("C-01", "M-01", "2026-10-01", "Dra. Gómez", "Control general", "Sin novedades")
    for item in consultar_historial("M-01"):
        print(item)
