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
