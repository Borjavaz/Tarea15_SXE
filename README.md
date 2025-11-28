# Tarea15_SXE

## 1. Levantar contenedores

```bash
docker compose up
```

## 2. Crear la Estructura Base

### Para acceder a este contenedor de Odoo (web) utilizo este comando

```bash
docker exec -it odoo18_app /bin/bash
```

<img width="806" height="72" alt="image" src="https://github.com/user-attachments/assets/b83c9c43-4667-4011-b750-edf0a191e2a1" />

### El siguiete paso es crear la carpeta `dc_bebidas` en la carpeta local `addons`

```bash
odoo scaffold dc_bebidas /mnt/extra-addons/
```

<img width="664" height="61" alt="image" src="https://github.com/user-attachments/assets/4710a6a4-41be-4723-99c6-c2c2140d2572" />

### Salgo del contenedor con el comando:

```bash
exit
```
### Esta es la estructura del proyecto:

<img width="463" height="406" alt="image" src="https://github.com/user-attachments/assets/3ab4b994-1fd6-49d5-ba61-690675d2cbb2" />

Renombro el archivo models/models.py a models/zzz_bebidas.py

<img width="591" height="272" alt="image" src="https://github.com/user-attachments/assets/882ccf44-31d8-4823-bcc6-491731c00b78" />
