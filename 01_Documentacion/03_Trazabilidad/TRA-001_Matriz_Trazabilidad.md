# TRA-001 - Matriz de Trazabilidad de PetCare

## Información del elemento de configuración

- Código del CI: TRA-001
- Nombre: Matriz de Trazabilidad
- Categoría: Gestión de Configuración 
- Proyecto: PetCare
- Versión: 1.1
- Estado: Aprobado para línea base 1.1
- Fecha: 07/10/2026
- Responsable: Equipo PetCare
- Ubicación: 01_Documentacion/03_Trazabilidad/TRA-001_Matriz_Trazabilidad.md

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 04/10/2026 | Creación inicial de la matriz de trazabilidad | Equipo PetCare |
| 1.1 | 07/10/2026 | Actualización de trazabilidad por CR-001: Seguimiento de peso en consultas | Camila Guarín |

## 1. Objetivo

Relacionar los requisitos definidos para PetCare con los elementos de diseño, código fuente y pruebas que los implementan o verifican.

La matriz permite identificar qué elementos de configuración deben revisarse cuando un requisito sea modificado y registrar la trazabilidad de las solicitudes de cambio.

## 2. Matriz de trazabilidad inicial

| Requisito | Descripción | Diseño relacionado | Código relacionado | Prueba relacionada | Estado |
|-----------|-------------|--------------------|--------------------|--------------------|--------|
| RF-01 | Registrar propietario | DIS-001 - Entidad Propietario | SRC-001 - registrar_propietario | TST-001 / CP-01 | Completa |
| RF-02 | Registrar mascota | DIS-001 - Entidad Mascota | SRC-001 - registrar_mascota | TST-001 / CP-02 | Completa |
| RF-03 | Programar consulta y registrar peso | DIS-001 - Entidad Consulta | SRC-001 - programar_consulta | TST-001 / CP-03, PRU-03, PRU-05, PRU-06 | Completa |
| RF-04 | Consultar historial incluyendo peso | DIS-001 - Entidades Mascota y Consulta | SRC-001 - consultar_historial | TST-001 / CP-04, PRU-04 | Completa |
TST-001 / CP-04 | Completa |
| RNF-01 | Integridad del historial | DIS-001 - Decisión D-01 | SRC-001 - (ausencia de operaciones de edición y eliminación) | TST-001 / CP-05 | Completa |

El estado de trazabilidad indica la existencia de relaciones entre los artefactos. No constituye evidencia de ejecución satisfactoria de las pruebas; los resultados se registran en TST-001.

## 3. Relación entre elementos de configuración

La configuración inicial de PetCare presenta la siguiente relación:

REQ-001 v1.1 
↓ 
DIS-001 v1.1 
↓ 
SRC-001 v1.1 
↓ 
TST-001 v1.1

La configuración 1.1 incorpora los cambios aprobados del CR-001: Seguimiento de peso en consultas.

## 4. Trazabilidad por requisito

### RF-01 - Registrar propietario

- Requisito: REQ-001
- Diseño asociado: DIS-001 - Entidad Propietario
- Código asociado: SRC-001 - registrar_propietario
- Caso de prueba asociado: TST-001 / CP-01
- Estado de trazabilidad: Completa

### RF-02 - Registrar mascota

- Requisito: REQ-001
- Diseño asociado: DIS-001 - Entidad Mascota
- Código asociado: SRC-001 - registrar_mascota
- Caso de prueba asociado: TST-001 / CP-02
- Estado de trazabilidad: Completa

### RF-03 - Programar consulta

- Requisito: REQ-001
- Diseño asociado: DIS-001 - Entidad Consulta
- Código asociado: SRC-001 - programar_consulta
- Caso de prueba asociado: TST-001 / CP-03
- Estado de trazabilidad: Completa

### RF-04 - Consultar historial

- Requisito: REQ-001
- Diseño asociado: DIS-001 - Entidades Mascota y Consulta
- Código asociado: SRC-001 - consultar_historial
- Caso de prueba asociado: TST-001 / CP-04
- Estado de trazabilidad: Completa

### RNF-01 - Integridad del historial

- Requisito: REQ-001
- Diseño asociado: DIS-001 - Decisión D-01
- Código asociado: SRC-001 (no ofrece edición ni eliminación de consultas)
- Caso de prueba asociado: TST-001 / CP-05
- Estado de trazabilidad: Completa

## 5. Trazabilidad de cambios

Cuando se apruebe una solicitud de cambio, esta matriz deberá registrar qué elementos fueron afectados.

La relación deberá seguir, cuando aplique, la siguiente estructura:

Solicitud de cambio (Issue)
↓
Requisito afectado
↓
Diseño afectado
↓
Código afectado
↓
Prueba afectada
↓
Commit o Pull Request
↓
Nueva versión de los elementos afectados
↓
Nueva línea base

## 6. Registro de cambios trazables

| Solicitud de cambio | Requisito afectado | Diseño afectado | Código afectado | Prueba afectada | Commit / PR | Estado |
|--------------------|--------------------|-----------------|-----------------|-----------------|-------------|--------|
| CR-001 | RF-03 y RF-04 | DIS-001 - Entidad Consulta | SRC-001 - programar_consulta y consultar_historial | TST-001 - PRU-03, PRU-04, PRU-05 y PRU-06 | PR #1 y PR #3 | Aprobado e integrado |

## 7. Observaciones

Este documento constituye el Elemento de Configuración TRA-001.

La versión 1.1 incorpora la trazabilidad correspondiente al CR-001 y a los elementos modificados para su implementación y verificación.

Toda modificación posterior deberá actualizar esta matriz y quedar relacionada con una solicitud de cambio aprobada. Las solicitudes rechazadas también se registran, indicando el Issue que conserva el análisis y la decisión, aunque no generen cambios en los CI.
