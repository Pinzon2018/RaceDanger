DROP DATABASE IF EXISTS Carrera;

CREATE DATABASE Carrera CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;

USE Carrera;

CREATE TABLE Equipo (
	ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre_Equipo VARCHAR(45) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Personas_Equipo VARCHAR(45) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Mecanicos_Equipo VARCHAR(45) COLLATE utf8mb4_unicode_520_ci NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;

CREATE TABLE Circuito(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre_Circuito VARCHAR(45) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Cantidad_Max_Participantes VARCHAR(45) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Km_Circuito INT NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;

CREATE TABLE Aviones (
	ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre_Avion VARCHAR(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Numero_Avion VARCHAR(45) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Cantidad_Asientos VARCHAR(45) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Km_Recorridos VARCHAR(25) NOT NULL
)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;

CREATE TABLE usuario (
	ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Email VARCHAR(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Contraseña VARCHAR(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Fecha_Nacimiento DATE NOT NULL
)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;

CREATE TABLE Piloto (
	ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre_Piloto VARCHAR(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Num_Identificación VARCHAR(45) COLLATE utf8mb4_unicode_520_ci NOT NULL,
    Fecha_Nacimiento DATE NOT NULL,
    ID_Equipo INT NOT NULL,
    ID_Aviones INT NOT NULL,
    FOREIGN KEY (ID_Equipo) REFERENCES Equipo(ID),
    FOREIGN KEY (ID_Aviones) REFERENCES Aviones(ID)
)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;

CREATE TABLE Ganador_Carrera (
	ID INT PRIMARY KEY AUTO_INCREMENT,
    ID_Piloto INT NOT NULL,
    ID_Circuito INT NOT NULL,
    Fecha_Victoria DATE NOT NULL,
    FOREIGN KEY (ID_Circuito) REFERENCES Circuito(ID),
    FOREIGN KEY (ID_Piloto) REFERENCES Piloto(ID)
)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;
