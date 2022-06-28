from email.policy import default
from typing_extensions import Required
from odoo import models, fields, api

class Aparcamiento(models.Model):
    _name = 'garaje.aparcamiento'
    _description = 'Permite definir las caracteristicas de un aparcamiento.'

    name = fields.Char(string = 'Dirección', required = True)
    plaza = fields.Integer(string = 'Plazas', requiered = True)


class Coche(models.Model):
    _name = 'garaje.coche'
    _description = 'Permite definir las caracteristicas de un coche.'
    _order = 'name'

    name = fields.Char(string = 'Matricula', required = True, size = 7)
    modelo = fields.Char(string = 'Modelo' )
    construido = fields.Date(string = 'Fecha de construcción' )
    consumo = fields.Float(string = 'Consumo', (4, 1), default = 0.0)
    averiado = fields.Boolean(string = '')
    annos = fields.Integer(string = 'Años', compute  = '_get_annos')
    aparcamiento_id = fields.(string = '')
    mantenimiento_ids = fields.(string = '')
    description = fields.Text(string = 'Descripción')

    @api.depends('construido'):
    def _get_annos(self):
        for coche in self:
            coche.annos = 0