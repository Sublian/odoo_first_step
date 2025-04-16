from datetime import date
from odoo import models, fields, api

class Todo(models.Model):
    _name = "wb.todo"
    _description = "Tarea de Webinar"

    name = fields.Char("Nombre")
    status = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('no_realizado', 'No Realizado'),
        ('completada', 'Completada')
    ], string='Estado', default='pendiente')

    color = fields.Integer("Color", compute='_compute_color', store=True)
    responsable_id = fields.Many2one('res.users', string="Responsable") # 👈 Nuevo campo
    fecha_limite = fields.Date(string="Fecha Límite")  # 👈 Nuevo campo
    # fecha_creacion = fields.Date(string="Fecha de Creación", default = fields.Date.today)
    
    prioridad = fields.Selection([ # 👈 Nuevo campo
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta')
    ], string="Prioridad", default='media')

    @api.depends('status')
    def _compute_color(self):
        for record in self:
            if record.status == 'completada':
                record.color = 10  # Verde
            elif record.prioridad == 'alta':
                record.color = 1   # Rojo o Naranja
            elif record.prioridad == 'media':
                record.color = 3   # Gris
            elif record.prioridad == 'baja':
                record.color = 7   # Azul claro
            else:
                record.color = 0   # Sin color
    @api.model
    def cron_actualizar_estado(self):
        today = date.today()
        records = self.search([('status', '!=', 'completada'), ('fecha_limite', '<', today)])
        for rec in records:
            rec.status = 'no_realizado'
