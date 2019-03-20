# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        print('on_change ici')

        # fiscal position empty on the start
        position_id = False

        # if the partner has a fiscal position and the invoice a team
        if self.partner_id and self.partner_id.property_account_position_id and self.team_id:
            print('et là')
            # if there is a country on the fiscal position of the partner, we search the fiscal position corresponding with the correct team
            if self.partner_id.property_account_position_id.country_id:
                position_id = self.env['account.fiscal.position'].search([('country_id.id', '=', self.partner_id.property_account_position_id.country_id.id),('team_id.id', '=', self.team_id.id)], limit=1)

                # if there is no result, and a group of country on the fiscal position, we restart the search
                if position_id.__str__() == 'account.invoice()' and self.partner_id.property_account_position_id.country_group_id:
                    position_id = self.env['account.fiscal.position'].search([('country_group_id.id', '=', self.partner_id.property_account_position_id.country_group_id.id),('team_id.id', '=', self.team_id.id)], limit=1)

            # if there is no country on the fiscal position of the partner but a group of country, we search the fiscal position corresponding with the correct team
            elif self.partner_id.property_account_position_id.country_group_id:
                position_id = self.env['account.fiscal.position'].search([('country_group_id.id', '=', self.partner_id.property_account_position_id.country_group_id.id),('team_id.id', '=', self.team_id.id)], limit=1)

        # affectation
        self.fiscal_position_id = position_id

        # searching a match beetween accounts of the fiscal position and the current account of the invoice
        if self.fiscal_position_id and self.fiscal_position_id.account_ids:
            for account in self.fiscal_position_id.account_ids:
                if account.account_src_id.id == self.account_id.id:
                    self.account_id = account.account_dest_id.id
                    break


    @api.onchange('team_id')
    def onchange_team_id(self):
        print('tttttttt')
        # fiscal position empty on the start
        position_id = False

        # if the partner has a fiscal position and the invoice a team
        if self.partner_id and self.partner_id.property_account_position_id and self.team_id:
            print('tteeeeeeeeee')
            # if there is a country on the fiscal position of the partner, we search the fiscal position corresponding with the correct team
            if self.partner_id.property_account_position_id.country_id:
                position_id = self.env['account.fiscal.position'].search(
                    [('country_id.id', '=', self.partner_id.property_account_position_id.country_id.id),
                     ('team_id.id', '=', self.team_id.id)], limit=1)

                # if there is no result, and a group of country on the fiscal position, we restart the search
                if position_id.__str__() == 'account.invoice()' and self.partner_id.property_account_position_id.country_group_id:
                    position_id = self.env['account.fiscal.position'].search(
                        [('country_group_id.id', '=', self.partner_id.property_account_position_id.country_group_id.id),
                         ('team_id.id', '=', self.team_id.id)], limit=1)

            # if there is no country on the fiscal position of the partner but a group of country, we search the fiscal position corresponding with the correct team
            elif self.partner_id.property_account_position_id.country_group_id:
                position_id = self.env['account.fiscal.position'].search(
                    [('country_group_id.id', '=', self.partner_id.property_account_position_id.country_group_id.id),
                     ('team_id.id', '=', self.team_id.id)], limit=1)

        # affectation
        self.fiscal_position_id = position_id

        # searching a match beetween accounts of the fiscal position and the current account of the invoice
        if self.fiscal_position_id and self.fiscal_position_id.account_ids:
            for account in self.fiscal_position_id.account_ids:
                if account.account_src_id.id == self.account_id.id:
                    self.account_id = account.account_dest_id.id
                    break