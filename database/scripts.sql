-- Crear tabla Usuarios
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    correo TEXT(50) NOT NULL,
    password TEXT NOT NULL,
    nombres TEXT(100) NOT NULL,
    apellidos TEXT(100) NOT NULL,
    edad INTEGER NOT NULL,
    idGenero INTEGER REFERENCES Generos(id) NOT NULL,
    idCargo INTEGER REFERENCES Cargos(id) NOT NULL,
    fechaIngreso TEXT(20) NOT NULL,
    idTipoContrato INTEGER REFERENCES TiposContratos(id) NOT NULL,
    fechaTerminoContrato TEXT(20) NOT NULL,
    idDependencia INTEGER REFERENCES Dependencias(id) NOT NULL,
    salario REAL NOT NULL,
    idRol INTEGER REFERENCES Roles(id) NOT NULL,
    puntaje INTEGER,
    comentarios TEXT
)

-- Eliminar tabla usuarios
DROP TABLE USUARIOS

-- Insertar un registro en la tabla usuarios
INSERT INTO usuarios (correo, password, nombres, apellidos, edad, idGenero, idCargo, fechaIngreso, idTipoContrato, fechaTerminoContrato, idDependencia, salario, idRol)
VALUES (
    'asd',
    '123',
    'nomasd',
    'asdzxcc',
    18,
    24,
    56,
    '2010-10-20',
    7,
    '2010-10-22',
    5,
    1500000,
    2
)

-- Consulta toda la información de los usuarios
SELECT u.id, u.correo, u.nombres, u.apellidos, u.edad, u.idGenero, g.descripcion as genero, u.idCargo, c.descripcion as cargo,
u.fechaIngreso, u.idTipoContrato, tc.descripcion as tipoContrato, u.fechaTerminoContrato, u.idDependencia, d.descripcion as dependencia,
u.salario, u.idRol, r.descripcion as rol FROM usuarios as u
INNER JOIN cargos as c
on c.id = u.idCargo
INNER JOIN dependencias as d
on d.id = u.idDependencia
INNER JOIN generos as g
on g.id = u.idGenero
INNER JOIN tiposContratos as tc
on tc.id = u.idTipoContrato
INNER JOIN roles as r
on r.id = u.idRol


-- Consulta para el login
SELECT u.id, u.correo, u.password, u.nombres, u.apellidos, u.idRol, r.descripcion as rol FROM usuarios as u
INNER JOIN roles as r
on r.id = u.idRol

-- Consulta la información para retroalimentación
SELECT u.id, u.correo, u.password, u.nombres, u.apellidos, u.puntaje, u.comentarios FROM usuarios as u

-- Consultar la información de la tabla usuarios
SELECT * FROM usuarios

DELETE FROM usuarios WHERE id = 8

------------------------------------------
------------------------------------------

-- Crear tabla géneros
CREATE TABLE generos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT(10) NOT NULL
)
-- Operaciones para la tabla generos
SELECT * FROM generos
DELETE FROM generos

------------------------------------------
------------------------------------------

-- Crear tabla cargos
CREATE TABLE cargos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT(100) NOT NULL
)

-- Operaciones para la tabla cargos
SELECT * FROM cargos
DELETE FROM cargos WHERE id = 55

------------------------------------------
------------------------------------------

-- Crear tabla tiposContratos
CREATE TABLE tiposContratos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
descripcion TEXT(100) NOT NULL
)

-- Operaciones para la tabla tiposContratos
SELECT * FROM tiposContratos
DELETE FROM tiposContratos

------------------------------------------
------------------------------------------

-- Crear tabla dependencias
CREATE TABLE dependencias (
id INTEGER PRIMARY KEY AUTOINCREMENT,
descripcion TEXT(100) NOT NULL
)

-- Operaciones para la tabla dependencias
SELECT * FROM dependencias
DELETE FROM dependencias

------------------------------------------
------------------------------------------

-- Crear tabla roles
CREATE TABLE roles (
id INTEGER PRIMARY KEY AUTOINCREMENT,
descripcion TEXT(100) NOT NULL
)

-- Operaciones para la tabla roles
INSERT INTO roles (descripcion) VALUES ('Usuario final')
INSERT INTO roles (descripcion) VALUES ('Administrador')
INSERT INTO roles (descripcion) VALUES ('SuperAdministrador')
SELECT * FROM roles
DELETE FROM ROLES

-- Consultas para dashboard
SELECT count(id) as cantidad from usuarios
SELECT max(puntaje) as maxpuntaje from usuarios
SELECT min(puntaje) as maxpuntaje from usuarios


------------------------------------------
------------------------------------------

-- Crear tabla opciones del menú
CREATE TABLE opcionesMenu (
id INTEGER PRIMARY KEY AUTOINCREMENT,
descripcion TEXT(100) NOT NULL,
url TEXT(100) NOT NULL,
icono TEXT(100) NOT NULL,
idRol INTEGER REFERENCES Roles(id) NOT NULL
)

-- Operaciones para la tabla opcionesMenu
--
-- File generated with SQLiteStudio v3.3.3 on mié. oct. 20 21:26:02 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: opcionesMenu para el rol de superadministrador

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Dashboard', '/', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Dashboard', '/dashboard', '<i class="far fa-circle nav-icon"></i>', 3, 1);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Perfil de usuario', '/usuarios/perfil', '<i class="far fa-circle nav-icon"></i>', 3, 1);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios', '<i class="far fa-circle nav-icon"></i>', 3, 1);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Cargos', '/cargos', '<i class="far fa-circle nav-icon"></i>', 3, 1);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Cargos', '/cargos/listar', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Cargos', '/cargos/obtener', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Cargos', '/cargos/crear', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Cargos', '/cargos/editar', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Cargos', '/cargos/eliminar', '', 3, 0);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Dependencias', '/dependencias', '<i class="far fa-circle nav-icon"></i>', 3, 1);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Dependencias', '/dependencias/listar', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Dependencias', '/dependencias/obtener', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Dependencias', '/dependencias/crear', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Dependencias', '/dependencias/editar', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Dependencias', '/dependencias/eliminar', '', 3, 0);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Géneros', '/generos', '<i class="far fa-circle nav-icon"></i>', 3, 1);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Géneros', '/generos/listar', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Géneros', '/generos/obtener', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Géneros', '/generos/crear', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Géneros', '/generos/editar', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Géneros', '/generos/eliminar', '', 3, 0);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Tipos de contratos', '/tiposcontratos', '<i class="far fa-circle nav-icon"></i>', 3, 1);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Tipos de contratos', '/tiposcontratos/listar', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Tipos de contratos', '/tiposcontratos/obtener', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Tipos de contratos', '/tiposcontratos/crear', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Tipos de contratos', '/tiposcontratos/editar', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Tipos de contratos', '/tiposcontratos/eliminar', '', 3, 0);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/listar', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/obtener', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/ver', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/crear', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/editar', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/eliminar', '', 3, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/retroalimentacion', '', 3, 0);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Cerrar sesión', '/logout', '<i class="nav-icon far fa-circle text-danger"></i>', 3, 1);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Menú', '/menu', '', 3, 0);


-- Table: opcionesMenu para el rol de administrador

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Dashboard', '/', '', 2, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Dashboard', '/dashboard', '<i class="far fa-circle nav-icon"></i>', 2, 1);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Perfil de usuario', '/usuarios/perfil', '<i class="far fa-circle nav-icon"></i>', 2, 1);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios', '<i class="far fa-circle nav-icon"></i>', 2, 1);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/listar', '', 2, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/obtener', '', 2, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/ver', '', 2, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/crear', '', 2, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/editar', '', 2, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/eliminar', '', 2, 0);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Usuarios', '/usuarios/retroalimentacion', '', 2, 0);

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Cerrar sesión', '/logout', '<i class="nav-icon far fa-circle text-danger"></i>', 2, 1);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Menú', '/menu', '', 2, 0);

-- Table: opcionesMenu para el rol de usuario

INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Perfil de usuario', '/usuarios/perfil', '<i class="far fa-circle nav-icon"></i>', 1, 1);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Cerrar sesión', '/logout', '<i class="nav-icon far fa-circle text-danger"></i>', 1, 1);
INSERT INTO opcionesMenu (descripcion, url, icono, idRol, mostrarMenu) VALUES ('Menú', '/menu', '', 1, 0);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;


SELECT * FROM opcionesMenu

SELECT om.descripcion, om.url, om.icono, om.mostrarMenu FROM opcionesMenu as om
INNER JOIN roles as r
ON om.idRol = r.id
WHERE r.id = 3


DELETE FROM opcionesMenu where id = 58

DELETE FROM opcionesMenu where idRol = 1



-- Activar la validación de llaves foráneas
PRAGMA foreign_keys = ON;

PRAGMA foreign_keys;





