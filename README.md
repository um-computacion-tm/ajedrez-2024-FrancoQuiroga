Ajedrez
========================
- Proyecto creado por Franco Enzo Quiroga Abraham

## Como instalar y jugar:
IMPORTANTE: Se requiere de una conexión a internet para descargar el repositorio y para construir la imagen de docker. Una vez construida, la conexión a internet no es obligatoria. Este tutorial funciona para 
1) Instalar Docker (Preferiblemente usar Linux):  https://docs.docker.com/get-started/get-docker/

2) Usando Git descargar el repositorio y cambiar el directorio de tu consola al de git:
```bash 
 git clone https://github.com/um-computacion-tm/ajedrez-2024-FrancoQuiroga.git
 
 cd ajedrez-2024-FrancoQuiroga
 
```
3) Usando docker crear y ejecutar la imagen:
```bash
sudo docker build --no-cache -t ajedrez . && sudo docker run -it ajedrez
```
Para jugar una vez construida la imagen:
```bash
sudo docker run -it ajedrez
```
Si no quieres escribir tu contraseña de usuario cada vez que quieras jugar:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Reiniciar la computadora después de esos 2 comandos  
(IMPORTANTE: Agregar tu usuario al grupo de Docker puede ser un riesgo
de seguridad para tu sistema, usa el comando con )  
Para sacar a tu usuario del grupo de Docker:
```bash
sudo gpasswd -d $USER docker
```

4) Jugar al ajedrez.

## Reglas para jugar este Ajedrez:

- Si no sabes jugar al ajedrez este es un buen recurso para aprender:  
https://www.chess.com/es/como-jugar-ajedrez  

- IMPORTANTE: Este programa no puede ejecutar los siguientes movimientos:
    - Enroque
    - En passant
    - Jaque Mate (El juego termina cuando cualquiera de los reyes es capturado, o cuando se capturan todas las otras piezas)

## Estado de Main(CircleCi):
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-FrancoQuiroga/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-FrancoQuiroga/tree/main)

##  Calidad del Código (CodeClimate):
[![Maintainability](https://api.codeclimate.com/v1/badges/e72781e346f2cde9dfcd/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-FrancoQuiroga/maintainability)

## Cobertura de los Tests (CodeClimate):
[![Test Coverage](https://api.codeclimate.com/v1/badges/e72781e346f2cde9dfcd/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-FrancoQuiroga/test_coverage)

