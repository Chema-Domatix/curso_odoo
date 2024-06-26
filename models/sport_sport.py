from odoo import models, fields

class SportSport(models.Model):
    _name="sport.sport"
    _description="Sport Sport"
    
    
    name = fields.Char(
        string='Name',
    )
    
    description = fields.Text(
        string='Description',
    )
   
   
    team_ids = fields.One2many(
       string='Sport',
       comodel_name='sport.team',
       inverse_name='sport_id',
   )
   
    