# INV-001 - Inventario de Elementos de Configuración de PetCare

## Información del elemento de configuración

- Código del CI: INV-001
- Nombre: Inventario de Elementos de Configuración
- Categoría: Gestión de Configuración
- Proyecto: PetCare
- Versión: 1.0
- Estado: Aprobado para línea base inicial
- Fecha: 04/10/2026
- Responsable: Equipo PetCare
- Ubicación: 01_Documentacion/03_Trazabilidad/INV-001_Inventario_CI.md

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 04/10/2026 | Creación inicial del inventario de elementos de configuración | Equipo PetCare |

## 1. Objetivo

Identificar y mantener bajo control los principales elementos de configuración que forman parte de la versión inicial del producto PetCare.

El inventario permite conocer la identificación, versión, estado, responsable, ubicación y línea base de cada elemento de configuración, facilitando el control de cambios y la trazabilidad del producto.

## 2. Elementos de configuración

| Código | Nombre | Categoría | Versión | Estado | Responsable | Ubicación | Línea base |
|--------|--------|-----------|---------|--------|-------------|-----------|------------|
| REQ-001 | Especificación de requisitos | Especificación | 1.0 | Aprobado | Equipo PetCare | 01_Documentacion/01_Requisitos/REQ-001_Especificacion_Requisitos.md | BL-001 |
| DIS-001 | Diseño del Sistema | Diseño | 1.0 | Aprobado | Equipo PetCare | 01_Documentacion/02_Diseno/DIS-001_Diseno_Sistema.md | BL-001 |
| SRC-001 | Gestión de Propietarios, Mascotas y Consultas | Implementación | 1.0 | Aprobado | Equipo PetCare | 02_Codigo_Fuente/SRC-001_PetCare.py | BL-001 |
| TST-001 | Plan y Casos de Prueba | Pruebas | 1.0 | Aprobado | Equipo PetCare | 03_Pruebas/TST-001_Plan_Casos_Prueba.md | BL-001 |
| DOC-001 | Documentación de PetCare | Documentación | 1.0 | Aprobado | Equipo PetCare | 01_Documentacion/05_Documentacion/DOC-001_README_PetCare.md | BL-001 |
| TRA-001 | Matriz de Trazabilidad | Gestión de Configuración | 1.0 | Aprobado | Equipo PetCare | 01_Documentacion/03_Trazabilidad/TRA-001_Matriz_Trazabilidad.md | BL-001 |
| INV-001 | Inventario de Elementos de Configuración | Gestión de Configuración | 1.0 | Aprobado | Equipo PetCare | 01_Documentacion/03_Trazabilidad/INV-001_Inventario_CI.md | BL-001 |

## 3. Criterios de identificación de los CI

Se consideran elementos de configuración aquellos artefactos cuya modificación puede afectar la integridad, comportamiento, verificación o trazabilidad del producto.

Para la línea base inicial se seleccionaron los siguientes tipos de elementos:

- Especificación de requisitos.
- Diseño del sistema.
- Código fuente.
- Pruebas.
- Matriz de trazabilidad.
- Inventario de elementos de configuración.
- Documentación del producto. 

No se registran como CI independientes archivos auxiliares o archivos de trabajo cuya modificación no represente por sí misma un cambio relevante para la configuración del producto.

## 4. Estados de los elementos de configuración

Los estados utilizados en el inventario son:

| Estado | Descripción |
|--------|-------------|
| Borrador | El elemento se encuentra en elaboración y aún no ha sido aprobado. |
| En revisión | El elemento está siendo revisado antes de su aprobación. |
| Aprobado | El elemento fue revisado y puede formar parte de una línea base. |
| En modificación | El elemento está siendo modificado como consecuencia de un cambio autorizado. |
| Obsoleto | El elemento dejó de pertenecer a la configuración vigente. |

## 5. Control de versiones

Cada elemento de configuración posee una versión identificable. Las modificaciones posteriores a la línea base deberán realizarse mediante una solicitud de cambio aprobada y deberán generar una nueva versión del elemento afectado cuando corresponda.

La versión 1.0 corresponde a la configuración inicial de PetCare.

## 6. Relación con la línea base

Los elementos registrados como versión 1.0 forman parte de la línea base inicial BL-001.

La línea base identifica las versiones exactas de los elementos que constituyen la configuración aprobada del producto en su estado inicial.

## 7. Control de cambios

Cualquier modificación de un elemento incluido en la línea base deberá estar relacionada con una solicitud de cambio.

El cambio deberá permitir identificar:

- Solicitud de cambio asociada.
- Elementos afectados.
- Nueva versión de los elementos modificados.
- Evidencia de implementación.
- Evidencia de pruebas.
- Revisión y aprobación.
- Línea base en la que se incorpora el cambio.

## 8. Observaciones

Este documento constituye el Elemento de Configuración INV-001.

El inventario deberá actualizarse cuando se incorporen, modifiquen o retiren elementos de configuración como resultado de cambios aprobados.

Las solicitudes de cambio rechazadas deberán conservar su registro y decisión, pero no producirán modificaciones en los elementos de configuración ni en la línea base.

La línea base BL-001 se encuentra documentada en `01_Documentacion/04_Lineas_Base/BL-001_Linea_Base_1.0.md`.