-- Permite el uso de FK
PRAGMA foreign_keys = ON;

-- Catalogo de los tipos de gastos
CREATE TABLE tipo_gasto(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NULL,

    CONSTRAINT pkTipo_gasto
    PRIMARY KEY(id)
);


-- Tabla para almacenar todos los gastos
CREATE TABLE gasto (
    fecha INTEGER NOT NULL,
    id INTEGER NOT NULL,
    tipo_gasto_id INTEGER NULL,
    descripcion TEXT NULL,
    monto INTEGER NOT NULL, -- Expresado en centavos para evitar problemas con operaciones de punto flotante

    CONSTRAINT pkGasto
    PRIMARY KEY(fecha, id),

    CONSTRAINT fkGastoTipo_gasto
    FOREIGN KEY (tipo_gasto_id)
    REFERENCES tipo_gasto(id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

-- Tabla para almacenar ingersos
CREATE TABLE ingreso(
    fecha INTEGER NOT NULL,
    id INTEGER NOT NULL,
    monto INTEGER NOT NULL, -- Expresado en centavos para evitar problemas con operaciones de punto flotante
    descripcion TEXT NULL,

    CONSTRAINT pkIngreso
    PRIMARY KEY(fecha, id)
);

-- Indices para consultas basadas en fechas
CREATE INDEX idx_gasto_fecha ON gasto(fecha);
CREATE INDEX idx_ingreso_fecha ON ingreso(fecha);

INSERT INTO tipo_gasto(id, nombre, descripcion) VALUES(1, 'Alquiler', 'Gasto mensual de alquiler');
INSERT INTO tipo_gasto(id, nombre, descripcion) VALUES(2, 'Comida', 'Gasto en comida');
INSERT INTO tipo_gasto(id, nombre, descripcion) VALUES(3, 'Transporte', 'Gasto en transporte');
INSERT INTO tipo_gasto(id, nombre, descripcion) VALUES(4, 'Salud', 'Gasto en salud');
INSERT INTO tipo_gasto(id, nombre, descripcion) VALUES(5, 'Educacion', 'Gasto en educacion');
INSERT INTO tipo_gasto(id, nombre, descripcion) VALUES(6, 'Entretenimiento', 'Gasto en entretenimiento');