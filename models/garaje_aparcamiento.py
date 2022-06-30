from odoo import models, fields, api

class Aparcamiento(models.Model):
    _name = 'garaje.aparcamiento'
    _description = 'Permite definir las caracteristicas de un aparcamiento.'

    name = fields.Char(string = 'Dirección', required = True)
    plazas = fields.Integer(string = 'Plazas', requiered = True)

    #relacion entre tablas
    coche_ids = fields.One2many(
        'garaje.coche', 
        'aparcamiento_id', 
        string = 'Lista Coches')