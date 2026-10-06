# REQ-001 - Especificación de requisitos de PetCare

## Información del elemento de configuración

* Código del CI: REQ-001
* Nombre: Especificación de requisitos
* Categoría: Especificación
* Proyecto: PetCare
* Versión: 1.1
* Estado: Aprobado para línea base inicial
* Fecha: 06/10/2026
* Responsable: Equipo PetCare
* Ubicación: 01_Documentacion/01_Requisitos/REQ-001_Especificacion_Requisitos.md

## Historial de versiones

| Versión | Fecha      | Descripción del cambio                              | Responsable    |
| ------- | ---------- | --------------------------------------------------- | -------------- |
| 1.0     | 03/10/2026 | Creación inicial de la especificación de requisitos | Equipo PetCare |
| 1.1     | 06/10/2026 | CR-001: se agrega el registro del peso en la consulta y su visualización en el historial | Juan David     |

## 1. Propósito

PetCare es un sistema de atención veterinaria destinado a administrar propietarios, mascotas y consultas veterinarias, conservando el historial clínico de cada mascota.

## 2. Alcance

El sistema permitirá registrar propietarios, registrar mascotas asociadas a un propietario, programar consultas con observaciones clínicas básicas y consultar el historial de consultas de una mascota.

No hacen parte de esta versión la facturación, el inventario de insumos ni la gestión de usuarios del sistema.

## 3. Requisitos funcionales

### RF-01 - Registrar propietario

El sistema deberá permitir registrar un propietario con los siguientes datos:

* Número de identificación
* Nombre completo
* Teléfono

Criterio de aceptación:

El sistema debe almacenar correctamente la información del propietario cuando todos los datos obligatorios hayan sido suministrados y no exista otro propietario con la misma identificación.

### RF-02 - Registrar mascota

El sistema deberá permitir registrar una mascota con los siguientes datos:

* Código de la mascota
* Nombre
* Especie
* Raza
* Identificación del propietario

Criterio de aceptación:

La mascota debe quedar registrada y asociada a su propietario cuando el propietario exista.

### RF-03 - Programar consulta

El sistema deberá permitir programar una consulta veterinaria para una mascota registrada, indicando:

* Código de la consulta
* Código de la mascota
* Fecha (formato AAAA-MM-DD)
* Veterinario
* Motivo de consulta
* Observaciones clínicas básicas
* Peso de la mascota en kilogramos

Criterio de aceptación:

La consulta debe quedar almacenada y asociada a la mascota cuando la mascota exista.

El peso es obligatorio y debe ser un número mayor que cero.

### RF-04 - Consultar historial de una mascota

El sistema deberá permitir consultar el historial de consultas de una mascota utilizando su código.

Criterio de aceptación:

Cuando exista la mascota, el sistema deberá mostrar todas sus consultas registradas, ordenadas por fecha e incluyendo el peso registrado en cada una, de modo que pueda observarse la evolución del peso.

## 4. Requisitos no funcionales

### RNF-01 - Integridad del historial

El historial clínico de una mascota deberá conservarse íntegro. Las consultas registradas no deberán modificarse ni eliminarse sin conservar evidencia verificable del cambio.

### RNF-02 - Usabilidad

El sistema deberá permitir que las operaciones principales puedan realizarse de manera sencilla para el personal veterinario y administrativo.

## 5. Observaciones de configuración

Este documento constituye un Elemento de Configuración de Software identificado como REQ-001.

Cualquier modificación posterior a la aprobación de la línea base deberá estar asociada a una solicitud de cambio formal.