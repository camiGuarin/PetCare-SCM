# DOC-001 - Documentación de PetCare

## Información del elemento de configuración

- Código del CI: DOC-001
- Nombre: Documentación de PetCare
- Categoría: Documentación
- Proyecto: PetCare
- Versión: 1.1
- Estado: Aprobado para línea base inicial
- Fecha: 06/10/2026
- Responsable: Equipo PetCare
- Ubicación: 01_Documentacion/05_Documentacion/DOC-001_README_PetCare.md
- Línea base: BL-001

## Historial de cambios

| Versión | Fecha | Descripción |
|---|---|---|
| 1.0 | 04/10/2026 | Creación de la documentación inicial del producto. |
| 1.1 | 06/10/2026 | CR-001: se documenta el registro del peso en la consulta. |

## 1. Descripción del producto

PetCare es un producto de software orientado a la gestión básica de la atención veterinaria. Permite administrar propietarios, mascotas y consultas veterinarias, además de consultar el historial de consultas de una mascota.

La versión inicial corresponde a un producto mínimo funcional que representa las principales funciones establecidas en el caso de estudio.

## 2. Funcionalidades principales

La versión 1.0 permite:

- Registrar propietarios.
- Registrar mascotas asociadas a un propietario.
- Programar consultas veterinarias.
- Registrar observaciones clínicas básicas.
- Registrar el peso de la mascota en cada consulta y consultarlo en el historial.
- Consultar el historial de consultas de una mascota.
- Mantener el historial sin operaciones de edición o eliminación de consultas registradas.

## 3. Estructura del proyecto

La estructura inicial del proyecto se organiza de la siguiente manera:

PetCare-SCM/
├── 01_Documentacion/
│   ├── 01_Requisitos/
│   │   └── REQ-001_Especificacion_Requisitos.md
│   ├── 02_Diseno/
│   │   └── DIS-001_Diseno_Sistema.md
│   ├── 03_Trazabilidad/
│   │   ├── TRA-001_Matriz_Trazabilidad.md
│   │   └── INV-001_Inventario_CI.md
│   ├── 04_Lineas_Base/
│   │   └── BL-001_Linea_Base_1.0.md
│   └── 05_Documentacion/
│       └── DOC-001_README_PetCare.md
├── 02_Codigo_Fuente/
│   └── SRC-001_PetCare.py
└── 03_Pruebas/
    └── TST-001_Plan_Casos_Prueba.md


## 4. Método y estructura de trabajo

Para el proyecto PetCare se utiliza una estructura organizada por categorías de artefactos: especificación, diseño, implementación, pruebas y documentación.

El control de configuración se realiza mediante GitHub, utilizando versiones, ramas, commits, solicitudes de cambio, revisión, integración y etiquetas para identificar las líneas base.

Esta estructura permite mantener organizados los elementos de configuración y facilita la trazabilidad entre los requisitos, el diseño, el código, las pruebas y la documentación.

## 5. Requisitos para ejecutar el producto

Para ejecutar la versión inicial de PetCare se requiere:

- Python 3 instalado.
- Acceso al repositorio del proyecto.
- Un sistema operativo compatible con Python.

La versión inicial no requiere una base de datos externa ni servicios adicionales, debido a que la información se maneja en memoria durante la ejecución.

## 6. Ejecución del producto

Desde la carpeta raíz del proyecto se puede ejecutar el código principal mediante:


python .\02_Codigo_Fuente\SRC-001_PetCare.py


Al ejecutar el programa se muestran en consola las consultas registradas para una mascota, organizadas por fecha e incluyendo el peso registrado en cada una.

## 7. Control de cambios

La versión 1.0 corresponde al estado inicial aprobado del producto. Cualquier modificación posterior deberá gestionarse mediante una solicitud de cambio.

Los cambios aprobados deberán identificar los elementos de configuración afectados, realizar un análisis de impacto, implementarse en una rama de trabajo, ser revisados y verificarse mediante las pruebas correspondientes.

Las solicitudes rechazadas deberán conservar su registro y decisión como evidencia del proceso de Gestión de la Configuración.

## 8. Relación con otros elementos de configuración

La documentación se relaciona con los demás elementos de configuración del proyecto:

REQ-001: especificación de requisitos.

DIS-001: diseño del sistema.

SRC-001: implementación inicial.

TST-001: plan, casos y resultados de pruebas.

TRA-001: matriz de trazabilidad.

INV-001: inventario de elementos de configuración.

BL-001: línea base inicial.

## 9. Estado de la documentación

Este documento corresponde a la documentación inicial del producto y forma parte de la línea base BL-001.

Las modificaciones posteriores deberán actualizar la versión del documento cuando el cambio afecte su contenido.

## Observaciones

La documentación inicial permite comprender el propósito, estructura, ejecución y estado del producto PetCare.

Cualquier modificación de este elemento deberá realizarse mediante el proceso de Gestión de la Configuración establecido para el proyecto.