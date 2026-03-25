# Taller evaluativo #1 🍽️

envio:https://forms.gle/ka7653WATu4fkcWT9

## Contexto
Un restaurante necesita un prototipo en Python para gestionar pedidos, clientes y ventas básicas del día.  
El objetivo del taller es practicar **listas**, **diccionarios**, **métodos de listas** y **funciones (`def`)**, junto con un flujo simple de **registro/login con intentos limitados**.

---

## Objetivo de aprendizaje
Al finalizar, el estudiante será capaz de:
- Construir soluciones usando **funciones** y estructuras de control.
- Gestionar **listas** con métodos como: `append`, `insert`, `remove`, `pop`, `sort`.
- Trabajar con una **lista de diccionarios** (mínimo 10 registros).
- Implementar un sistema básico de **registro/login** con control de intentos.
- Generar y procesar un volumen de datos relacionado con ventas de un restaurante.

---

## Requisitos del ejercicio

### 1) Registro y Login (con 4 intentos)
Implementa un sistema que permita:

**Registro**
- Permitir crear un usuario con:
  - `correo`
  - `password`
- Guardar el usuario registrado en una estructura simple (diccionario o lista de diccionarios).

**Login**
- Pedir correo y contraseña.
- Permitir **máximo 4 intentos**.
- En cada intento fallido debe mostrar:
  - `"Credenciales incorrectas. Intentos restantes: X"`
- Si inicia sesión correctamente, mostrar:
  - `"Login exitoso"` y permitir continuar con el menú.
- Si se agotan los intentos:
  - `"Cuenta bloqueada temporalmente"` y finalizar el programa.

---

### 2) Registro de N diccionarios (lista de diccionarios)
Crear una lista llamada `ventas_restaurante` que contenga **10 diccionarios**, cada uno con esta estructura mínima:

- `idVenta` (int)
- `nombreCliente` (str)
- `numeroMesa` (int)
- `platoPrincipal` (str)
- `valorConsumo` (float o int)
- `metodoPago` (str: "EFECTIVO", "TARJETA", "TRANSFERENCIA")
- `estadoPedido` (str: "ENTREGADO" o "PENDIENTE")

Debe existir un menú para:
- Mostrar todas las ventas registradas
- Ordenar las ventas por `valorConsumo` de menor a mayor
- Buscar una venta por `idVenta`
- Eliminar una venta
- Agregar una nueva venta

---

## Funciones obligatorias
Tu solución debe estar organizada usando funciones `def`.

Se espera como mínimo la construcción de módulos o funciones para:
- Registro de usuario
- Inicio de sesión
- Crear ventas
- Mostrar ventas
- Ordenar ventas
- Buscar ventas
- Eliminar ventas


---

## Menú sugerido (después del login)
1. Gestionar ventas del restaurante
2. Salir

---

## Criterios de evaluación (guía)
- (30%) Diseño de los módulos o funciones a programar
- (30%) Implementación correcta de las funciones
- (10%) Unificación de todo en un menú funcional
- (30%) Correcto uso de Git y GitHub

---

## Recomendaciones
- Usa nombres de variables claros y coherentes.
- Aplica correctamente listas, diccionarios y funciones.
- Organiza el código de forma legible.
- Realiza commits claros en GitHub que evidencien tu proceso.

---

Éxitos. La idea es que el ejercicio sea sencillo, funcional, completo y bien organizado.

