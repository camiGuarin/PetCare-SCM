# TST-001 - Plan y Casos de Prueba de PetCare

## Información del elemento de configuración

- Código del CI: TST-001
- Nombre: Plan y Casos de Prueba
- Categoría: Pruebas
- Proyecto: PetCare
- Versión: 1.0
- Estado: Aprobado para línea base inicial
- Fecha: 04/10/2026
- Responsable: Equipo PetCare
- Ubicación: 04_Pruebas/TST-001_Plan_Casos_Prueba.md

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 04/10/2026 | Creación inicial del plan y casos de prueba | Equipo PetCare|

## 1. Objetivo

Validar que las funcionalidades principales de PetCare cumplan con los requisitos definidos en REQ-001 versión 1.0.

## 2. Alcance de las pruebas

Las pruebas iniciales cubren:

- Registro de propietarios.
- Registro de mascotas.
- Programación de consultas.
- Consulta del historial de una mascota.
- Conservación íntegra del historial.

## 3. Casos de prueba

### CP-01 - Registrar propietario correctamente

- Requisito asociado: RF-01
- Diseño asociado: DIS-001 - Entidad Propietario
- Código asociado: SRC-001 - registrar_propietario
- Precondición: El propietario no debe existir previamente.

Datos de entrada:

- Identificación: 1001
- Nombre completo: Carlos Ramírez
- Teléfono: 3001234567

Resultado esperado:

El sistema crea correctamente el propietario y almacena identificación, nombre completo y teléfono.

### CP-02 - Registrar mascota con propietario existente

- Requisito asociado: RF-02
- Diseño asociado: DIS-001 - Entidad Mascota
- Código asociado: SRC-001 - registrar_mascota
- Precondición: El propietario 1001 debe estar registrado.

Datos de entrada:

- Código: M-01
- Nombre: Luna
- Especie: Perro
- Raza: Labrador
- Identificación del propietario: 1001

Resultado esperado:

La mascota queda registrada y asociada al propietario. 

Si el propietario no existe, el sistema rechaza el registro con un mensaje de error.

### CP-03 - Programar consulta

- Requisito asociado: RF-03
- Diseño asociado: DIS-001 - Entidad Consulta
- Código asociado: SRC-001 - programar_consulta
- Precondición: La mascota M-01 debe estar registrada.

Datos de entrada:

- Código de consulta: C-01
- Mascota: M-01
- Fecha: 2026-10-01
- Veterinario: Dra. Gómez
- Motivo: Control general
- Observaciones: Sin novedades

Resultado esperado:

La consulta queda almacenada y asociada a la mascota. 

Si la mascota no existe o la fecha es inválida, el sistema rechaza el registro.

### CP-04 - Consultar historial de una mascota

- Requisito asociado: RF-04
- Diseño asociado: DIS-001 - Entidades Mascota y Consulta
- Código asociado: SRC-001 - consultar_historial
- Precondición: La mascota M-01 tiene al menos dos consultas registradas.

Resultado esperado:

El sistema muestra todas las consultas de la mascota ordenadas por fecha. 

Si la mascota no existe, devuelve un mensaje de error.

### CP-05 - Historial conserva las consultas sin alteraciones

- Requisito asociado: RNF-01
- Diseño asociado: DIS-001 - Decisión D-01
- Código asociado: SRC-001 - consultar_historial
- Precondición: Existe una consulta registrada.

Resultado esperado:

Al consultar el historial varias veces, los datos de la consulta registrada permanecen idénticos y el sistema no ofrece una operación para editar o eliminar consultas.

## 4. Trazabilidad de pruebas

| Caso de prueba | Requisito | Diseño | Código |
|----------------|-----------|--------|--------|
| CP-01 | RF-01 | DIS-001 | SRC-001 |
| CP-02 | RF-02 | DIS-001 | SRC-001 |
| CP-03 | RF-03 | DIS-001 | SRC-001 |
| CP-04 | RF-04 | DIS-001 | SRC-001 |
| CP-05 | RNF-01 | DIS-001 (D-01) | SRC-001 |

## 5. Registro de resultados de ejecución

Las pruebas fueron ejecutadas sobre la versión 1.0 del sistema antes de establecer la línea base inicial.

| Caso de prueba | Versión probada | Fecha de ejecución | Ejecutado por | Resultado |
|----------------|-----------------|--------------------|---------------|-----------|
| CP-01 | 1.0 | 04/10/2026 | Equipo PetCare | Exitoso |
| CP-02 | 1.0 | 04/10/2026 | Equipo PetCare | Exitoso |
| CP-03 | 1.0 | 04/10/2026 | Equipo PetCare | Exitoso |
| CP-04 | 1.0 | 04/10/2026 | Equipo PetCare | Exitoso |
| CP-05 | 1.0 | 04/10/2026 | Equipo PetCare | Exitoso |

### Evidencia de ejecución 

- **CP-01:** Se registró correctamente un propietario con identificación, nombre completo y teléfono. 
- **CP-02:** Se registró correctamente una mascota y se asoció al propietario existente.
- **CP-03:** Se registró correctamente una consulta asociada a la mascota.
- **CP-04:** El historial de la mascota se consultó correctamente y las consultas aparecieron ordenadas por fecha.
- **CP-05:** Se realizaron dos consultas consecutivas del historial y los datos permanecieron iguales. La comparación entre ambos resultados retornó `True`.

## 6. Observaciones de configuración

Este documento constituye el Elemento de Configuración TST-001.

Los casos de prueba deberán actualizarse cuando una solicitud de cambio aprobada modifique los requisitos, el diseño o el código relacionado.

Las pruebas asociadas a cambios aprobados deberán conservar la trazabilidad con la solicitud de cambio correspondiente. 

Los resultados registrados corresponden a las pruebas realizadas sobre la versión 1.0 del producto antes de establecer la línea base inicial. 