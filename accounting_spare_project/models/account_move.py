from odoo import models, fields, api, _

class account_inherit(models.Model):
    _inherit = 'account.payment'

class account_analytic_line(models.Model):
    _inherit = 'account.analytic.line'
    ware_id = fields.Many2one('account.inventory', string="Inventory name")

    # analytic_account = fields.Many2one('account.analytic.account', string="ana")
    # ware_id = fields.Many2one(string="اسم المعرض", related='analytic_account.ware_id')


class account_move_inherit(models.Model):
    _inherit = 'account.move'
    analytic_account_id = fields.Many2one('account.analytic.account', string="Analytic Account")
    ware_id = fields.Many2one(string="Inventory name",related='analytic_account_id.ware_id')

class account_analytic_inherit(models.Model):
    _inherit = 'account.analytic.account'
    ware_id = fields.Many2one('account.inventory', string="Inventory name")


class account_low_inherit(models.Model):
    _inherit = 'hr.expense'

class account_employee_inherit(models.Model):
    _inherit = 'hr.employee'

class account_company_inherit(models.Model):
    _inherit = 'res.company'

class account_inventory(models.Model):
    _name = 'account.inventory'
    name = fields.Char(string="inventory name")
    # name = fields.Char(string="الكود")
    name_scq = fields.Char(string="inventory no", required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_scq', _('New')) == _('New'):
            vals['name_scq'] = self.env['ir.sequence'].next_by_code('account.inventory.sequence') or _('New')
        result = super(account_inventory, self).create(vals)
        return result
