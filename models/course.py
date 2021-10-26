from odoo import models, fields

class AcademyCourse(models.Model):
    _name = "academy.course"

    name = fields.Char()
    description = fields.Char(string="Description")
