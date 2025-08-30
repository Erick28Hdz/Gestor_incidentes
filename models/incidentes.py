from odoo import models, fields

class SeguridadIncidente(models.Model):
    _name = 'seguridad.incidente'
    _description = 'Gestión de Incidentes de Seguridad'

    name = fields.Char(string='Nombre del Incidente', required=True)
    description = fields.Text(string='Descripción')
    fecha = fields.Date(string='Fecha de Ocurrencia', default=fields.Date.today)
    gravedad = fields.Selection([
        ('bajo', 'Bajo'),
        ('medio', 'Medio'),
        ('alto', 'Alto')
    ], string='Nivel de Gravedad', default='medio')
