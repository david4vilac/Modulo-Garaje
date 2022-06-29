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

    name = fields.Char(
        string = 'Matricula', 
        required = True, 
        size = 7)
    modelo = fields.Char(
        string = 'Modelo', 
        required = True )
    construido = fields.Date(
        string = 'Fecha de construcción' )
    consumo = fields.Float(
        string = 'Consumo', 
        (4, 1), 
        default = 0.0,
        help = 'Consumo promedio cada 100kms')
    averiado = fields.Boolean(string = '')
    annos = fields.Integer(
        string = 'Años', 
        compute  = '_get_annos')
    description = fields.Text(
        string = 'Descripción')
    """aparcamiento_id = fields.(
        string = '')
    mantenimiento_ids = fields.(
        string = '')"""

    @api.depends('construido')
    def _get_annos(self):
        for coche in self:
            coche.annos = 0


class Mantenimiento(models.Model):
    _name = 'garaje.mantenimiento'
    _description = ''
    _order = 'fecha'

    fecha = fields.Date('Fecha', required=True, default = fields.date.today())
    tipo = fields.Selection(string = 'Tipo', selection = [
        ('l':'Lavar'),('r':'Revision'),('m':'Mecanica'),('p':'Pintura')
        ], default = 'l')
    coste = fields.Float(string = 'Coste', (8,2), help = 'Coste total del mantenimiento.')