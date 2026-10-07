# TST-001: Plan y Registro de Ejecución de Pruebas - PetCare

- **Código CI:** TST-001
- **Nombre:** Plan y Casos de Prueba del Sistema PetCare
- **Responsable de Pruebas:** Juan Pablo Jiménez
- **Categoría:** Pruebas
- **Estado:** En Revisión (CR-001)

---

## 1. Cobertura de Pruebas por Línea Base

### 1.1. Línea Base 1.0 (Producto Mínimo Inicial)
| ID Prueba | Descripción | Criterio de Aceptación | Estado | Evidencia |
| :--- | :--- | :--- | :--- | :--- |
| **PRU-01** | Registrar propietario y mascota | Se crea el registro del propietario vinculado a la mascota. | **PASÓ** | Consola ejecutada sin errores |
| **PRU-02** | Registrar y consultar citas clínicas | Muestra las consultas 'C-01' y 'C-02' asociadas a 'M-01'. | **PASÓ** | Consola ejecutada (C-01 / C-02) |

### 1.2. Línea Base 1.1 (CR-001: Seguimiento de Peso)
| ID Prueba | Descripción | Criterio de Aceptación | Estado | Evidencia |
| :--- | :--- | :--- | :--- | :--- |
| **PRU-03** | Registro de peso válido | La función `programar_consulta` registra el parámetro `peso_kg` correctamente (ej. 12.5 kg). | **PASÓ** | Verificado en `SRC-001_PetCare.py` |
| **PRU-04** | Historial con peso | El historial clínico despliega la evolución cronológica del peso. | **PASÓ** | Consulta e historial en consola |
| **PRU-05** | Registro de peso igual a cero | Al ingresar `peso_kg = 0`, el sistema invalida o rechaza la captura por valor no clínico. | **RECHAZADO / FALLÓ** | Validación de frontera ejecutada |
| **PRU-06** | Registro de peso negativo | Al ingresar `peso_kg < 0` (ej. -5 kg), el sistema rechaza el valor inconsistente. | **RECHAZADO / FALLÓ** | Validación de frontera ejecutada |

---

## 2. Dictamen Técnico de Pruebas - CR-001
- **Ejecutado por:** Juan Pablo Jiménez Izquierdo
- **Resultado de Verificación:** Las pruebas PRU-03 y PRU-04 confirman la integración del peso en consultas normales. Las pruebas PRU-05 y PRU-06 identifican la necesidad de validación de rangos numéricos.