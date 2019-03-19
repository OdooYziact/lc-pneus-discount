# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    team_id = fields.Many2one(comodel_name="crm.team", string="Equipe de vente")