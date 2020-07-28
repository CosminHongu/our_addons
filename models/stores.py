from odoo import fields, models, api, tools

class store(models.Model):
    _name = 'test13.store'
    _description = 'Store'

    name = fields.Char ('Store Name:')
    id = fields.Char ('ID')
    image = fields.Binary(string="Picture", required=True)
    games_ids = fields.Many2many('test13.game', string = 'Games name:')
    movies_ids = fields.Many2many('test13.movie', string = 'Movie name:')
    image_name = fields.Char("Picture name")

    name = fields.Char(required=True, default='Click on generate!')




