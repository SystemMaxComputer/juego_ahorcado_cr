CREATE TABLE dificultad
(
    id     SERIAL PRIMARY KEY,
    nombre varchar(20)
);


CREATE TABLE categoria
(
    id     SERIAL PRIMARY KEY,
    nombre varchar(20)
);

CREATE TABLE palabra
(
    id            SERIAL PRIMARY KEY,
    contenido     varchar(20) UNIQUE,
    categoria_id  INTEGER,
    dificultad_id INTEGER,
    CONSTRAINT dificultad_foreign_key FOREIGN KEY (dificultad_id)
        REFERENCES dificultad (id) MATCH SIMPLE,
    CONSTRAINT categoria_foreign_key FOREIGN KEY (categoria_id)
        REFERENCES categoria (id) MATCH SIMPLE
);

-- Insertar categorías
INSERT INTO categoria (nombre)
VALUES ('Frutas'),
       ('Animales'),
       ('Colores'),
       ('Deportes'),
       ('Profesiones');

-- Insertar dificultades
INSERT INTO dificultad (nombre)
VALUES ('Fácil'),
       ('Media'),
       ('Difícil');

-- Insertar palabras (50 palabras distribuidas en categorías y dificultades)
INSERT INTO palabra (contenido, categoria_id, dificultad_id)
VALUES
-- Frutas
('Manzana', 1, 1),
('Banano', 1, 1),
('Uva', 1, 2),
('Naranja', 1, 2),
('Fresa', 1, 3),
('Pera', 1, 3),

-- Animales
('Perro', 2, 1),
('Gato', 2, 1),
('Elefante', 2, 2),
('León', 2, 2),
('Cebra', 2, 3),
('Jirafa', 2, 3),

-- Colores
('Rojo', 3, 1),
('Azul', 3, 1),
('Verde', 3, 2),
('Amarillo', 3, 2),
('Naranjado', 3, 3),
('Morado', 3, 3),

-- Deportes
('Fútbol', 4, 1),
('Baloncesto', 4, 1),
('Tenis', 4, 2),
('Voleibol', 4, 2),
('Rugby', 4, 3),
('Golf', 4, 3),

-- Profesiones
('Ingeniero', 5, 1),
('Médico', 5, 1),
('Profesor', 5, 2),
('Abogado', 5, 2),
('Arquitecto', 5, 3),
('Científico', 5, 3);
