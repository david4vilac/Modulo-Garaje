from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class Coche(models.Model):
    _name = 'garaje.coche'
    _description = 'Permite definir las caracteristicas de un coche.'
    _order = 'name'

    name = fields.Char(
        string = 'Matricula', 
        required = True, 
        size = 7)
    modelo = fields.Char(
        string = 'Modelo', 
        required = True )
    construido = fields.Date(
        string = 'Fecha de construcción')
    consumo = fields.Float(
        string = 'Consumo', 
        default = 0.0,
        help = 'Consumo promedio cada 100kms')
    averiado = fields.Boolean(
        string = 'Averiado', 
        default = False)
    annos = fields.Integer(
        string = 'Años', 
        compute  = '_get_annos')
    description = fields.Text(
        string = 'Descripción')

    #relaciones entre tablas    
    aparcamiento_id = fields.Many2one(
        'garaje.aparcamiento', 
        string='Aparcamiento',
        )
    mantenimiento_ids = fields.Many2many(
        'garaje.mantenimiento',
        string = "Mantenimientos",
        required = True)


    @api.depends('construido')
    def _get_annos(self):
        for coche in self:
            today = date.today()
            coche.annos = relativedelta(today, coche.construido).years

    #restricciones con formato de la DB
    _sql_constraints = [('name_uniq', 'unique(name)', 'La matricula ya existe')]

