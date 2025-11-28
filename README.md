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

Renombro el archivo models/models.py a models/zzz_bebidas.py y importo la clase.

```bash
# -*- coding: utf-8 -*-

from . import zzz_bebidas
```

<img width="591" height="272" alt="image" src="https://github.com/user-attachments/assets/882ccf44-31d8-4823-bcc6-491731c00b78" />

## 3. Creación del Modelo de Datos 

```bash
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ZzzBebidas(models.Model):
    #nombres tecnicos q usará odoo
    _name = 'dc_bebidas.zzz_bebidas'
    # descripcion del modulo
    _description = 'Asignación de Bebida por Nivel de Sueño'

    alumno = fields.Char(
        string='Alumno',
        required=True,
        help="Nombre del alumno que necesita la bebida."
    )

    nivel_suenio = fields.Integer(
        string='Nivel de Sueño (1-10)',
        required=True,
        help="Indica el nivel de sueño del alumno, de 1 a 10.",
        default=1
    )

    bebida_recomendado = fields.Char(
        string='Bebida Recomendada',
        compute='_compute_bebida_recomendado',
        store=True, #para almacen el la bd
        readonly=True
    )

    @api.depends('nivel_suenio')
    def _compute_bebida_recomendado(self):
        
        for record in self:
            nivel = record.nivel_suenio
            if 1 <= nivel <= 3:
                record.bebida_recomendado = 'Café con leche'
            elif 4 <= nivel <= 6:
                record.bebida_recomendado = 'Café solo largo'
            elif 7 <= nivel <= 9:
                record.bebida_recomendado = 'Café solo larguísimo'
            elif nivel == 10:
                record.bebida_recomendado = 'Inyección de adrenalina'
            else:
                # Caso por si el valor esta fuera de rango (1-10)
                record.bebida_recomendado = 'Nivel fuera de rango (1-10)'
```
## 4. Definición de Vistas y Permisos

Modifico el archivo: addons/dc_bebidas/__manifest__.py, relleno los campos con nombres personalizados y en el apartado `data`:

```bash
    'data': [
        # 'security/ir.model.access.csv',
        'security/ir.model.access.csv',
        'views/bebidas_views.xml',
    ],
```

<img width="320" height="138" alt="image" src="https://github.com/user-attachments/assets/31ec5b74-b099-4cfa-aba7-27da6dede0bc" />

Configuro el archivo: addons/dc_bebidas/security/ir.model.access.csv

<img width="1366" height="385" alt="image" src="https://github.com/user-attachments/assets/abd093e5-0100-435d-a374-225fc650a0a0" />

