# prueba-axede
Prueba de ingreso
# Esquema de Base de Datos

Este proyecto utiliza una base de datos relacional diseñada para gestionar la información de una cadena hotelera. A continuación se describe el esquema, sus tablas y relaciones.

## Descripción de las Tablas
### 1. HOTEL
id: Identificador único del hotel (clave primaria).
nombre: Nombre del hotel (por ejemplo, "Hotel Barranquilla").
ciudad: Ciudad en la que se encuentra el hotel.
direccion: Dirección física (opcional).
telefono: Número de contacto (opcional).
creado_en / actualizado_en: Marcas de tiempo para el registro de creación y última actualización.
Relación: Un hotel puede tener múltiples habitaciones asociadas.

### 2. HABITACION
##### id: Identificador único de la habitación (clave primaria).
##### hotel_id: Referencia al hotel al que pertenece (clave foránea).
##### tipo: Tipo de habitación (por ejemplo, "standard", "premium", "vip").
##### capacidad: Número máximo de personas que puede alojar la habitación.
##### precio: Tarifa base de la habitación (opcional).
##### creado_en / actualizado_en: Marcas de tiempo para el registro de creación y última actualización.
Relación: Cada habitación pertenece a un solo hotel, pero un hotel puede contener varias habitaciones.

### 3. USUARIO
##### id: Identificador único del usuario (clave primaria).
##### nombre: Nombre completo del usuario.
##### email: Correo electrónico (único para cada usuario).
##### telefono: Número de contacto (opcional).
##### creado_en / actualizado_en: Marcas de tiempo para el registro de creación y última actualización.
##### Relación: Un usuario puede realizar múltiples reservas.

### 4. RESERVACION
##### id: Identificador único de la reserva (clave primaria).
##### usuario_id: Referencia al usuario que realiza la reserva (clave foránea).
##### habitacion_id: Referencia a la habitación reservada (clave foránea).
##### fecha_checkin: Fecha y hora de inicio de la reserva.
##### fecha_checkout: Fecha y hora de fin de la reserva.
##### estado: Estado de la reserva (por ejemplo, "confirmada", "cancelada").
##### creado_en / actualizado_en: Marcas de tiempo para el registro de creación y última actualización.
Relación:
Una reserva pertenece a un único usuario.
Una reserva se asocia a una única habitación.
Una habitación puede tener múltiples reservas a lo largo del tiempo (controlando el solapamiento de fechas).

## Diagrama Entidad-Relación

```mermaid
erDiagram
    HOTEL ||--|{ HABITACION : "contiene"
    HABITACION ||--|{ RESERVACION : "tiene"
    USUARIO ||--|{ RESERVACION : "realiza"

    HOTEL {
        int id PK
        string nombre
        string ciudad
        string direccion
        string telefono
        datetime creado_en
        datetime actualizado_en
    }

    HABITACION {
        int id PK
        int hotel_id FK
        string tipo
        int capacidad
        decimal precio
        datetime creado_en
        datetime actualizado_en
    }

    USUARIO {
        int id PK
        string nombre
        string email
        string telefono
        datetime creado_en
        datetime actualizado_en
    }

    RESERVACION {
        int id PK
        int usuario_id FK
        int habitacion_id FK
        datetime fecha_checkin
        datetime fecha_checkout
        string estado
        datetime creado_en
        datetime actualizado_en
    }
