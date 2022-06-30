from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class Mantenimiento(models.Model):
    _name = 'garaje.mantenimiento'
    _description = ''
    _order = 'fecha'

    fecha = fields.Date('Fecha', required=True, default = fields.date.today())
    tipo = fields.Selection(
        string = 'Tipo', 
        selection = [
            ('l','Lavar'), ('r','Revision'), ('m','Mecanica'), ('p','Pintura')
            ], 
        default = 'l')
    coste = fields.Float(
        string = 'Coste', 
        help = 'Coste total del mantenimiento.')

    #relaciones entre tablas
    coche_ids = fields.Many2many(
        'garaje.coche', 
        string = "Lista de Coches")

    def name_get(self):
        resultado = []
        for mantenimiento in self:
            description = f'{len(mantenimiento.coche_ids)} coches - {mantenimiento.coste} $'
            resultado.append((mantenimiento.id, description))
        return resultado