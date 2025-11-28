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

## 5. Definir Vistas y Menús

En el archivo: addons/dc_bebidas/views/bebidas_views.xml

```bash
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="zzz_bebidas_view_tree" model="ir.ui.view">
        <field name="name">dc_bebidas.zzz_bebidas.list</field>
        <field name="model">dc_bebidas.zzz_bebidas</field>
        <field name="arch" type="xml">
            <list string="Recomendación de Bebidas">
                <field name="alumno"/>
                <field name="nivel_suenio"/>
                <field name="bebida_recomendado"/>
            </list>
        </field>
    </record>

    <record id="zzz_bebidas_view_form" model="ir.ui.view">
        <field name="name">dc_bebidas.zzz_bebidas.form</field>
        <field name="model">dc_bebidas.zzz_bebidas</field>
        <field name="arch" type="xml">
            <form string="Nivel de Sueño y Bebida">
                <sheet>
                    <group>
                        <field name="alumno"/>
                        <field name="nivel_suenio" widget="integer"/>
                    </group>
                    <group>
                        <field name="bebida_recomendado"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <record id="zzz_bebidas_action" model="ir.actions.act_window">
        <field name="name">Recomendador de Bebidas</field>
        <field name="res_model">dc_bebidas.zzz_bebidas</field>
        <field name="view_mode">list,form</field> <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                Crea un nuevo registro para recomendar una bebida.
            </p>
        </field>
    </record>

    <menuitem
        id="menu_dc_bebidas_root"
        name="Daniel Castelao"
        sequence="100"/>

    <menuitem
        id="menu_bebidas_recomendadas"
        name="Bebidas por Sueño"
        parent="menu_dc_bebidas_root"
        action="zzz_bebidas_action"
        sequence="10"/>

</odoo>
```
## 6. Instalación y Prueba

#### Lo primero que hacemos es reiniciar el contenedor con el siguiente comando:

```bash
docker compose restart web
```

<img width="809" height="123" alt="image" src="https://github.com/user-attachments/assets/8e725bda-e96d-42db-8b0a-1b7a76b3a608" />

### A continuación activo el modo desarrollador

<img width="1301" height="342" alt="image" src="https://github.com/user-attachments/assets/54ffcd05-80ba-4018-8d2a-76438f33fbe0" />

### Actualización de los modulos

<img width="1300" height="470" alt="image" src="https://github.com/user-attachments/assets/20b4cedb-e305-48b0-804f-efc39ffe105c" />

### Busqueda e instalación del modulo creado:
`Bebidas para Alumnos Daniel Castelao`

<img width="1300" height="304" alt="image" src="https://github.com/user-attachments/assets/44df760d-11f2-479a-8c0c-fc010e39968f" />

### Interfaz al introducir nuevos alumnos:

<img width="1301" height="323" alt="image" src="https://github.com/user-attachments/assets/81bd9fdd-2d5b-40f5-b3af-ec40a0e777f4" />


### Resultado al insertar dos alumnos:

<img width="1301" height="275" alt="image" src="https://github.com/user-attachments/assets/03683b05-0d09-4c02-a4a6-667b59e17572" />
