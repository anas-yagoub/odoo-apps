from odoo import models, fields, api, _
from odoo import models, fields, api, exceptions

class expense_inherit(models.Model):

    _inherit = 'hr.expense'
    employee_id = fields.Many2one('hr.employee', string="Employee")
    total_wage = fields.Float('Total Wage',related='employee_id.total_wage')
    currency_ids = fields.Many2one(related='employee_id.currency_ids', string="Employee Currency")
    loan = fields.Float(string="Loan",related='employee_id.loan')
    wage = fields.Float('Wage', related='employee_id.wage')
    # unit_amount = fields.Float('hr.expense',related='employee_id.total_wage')



class account_employee_product(models.Model):
    _inherit = 'product.template'

    # @api.one
    # @api.constrains('loan')
    # def _check_unit_amount(self):
    #     if self.unit_amount or int(self.loan) == 0:
    #         if self.loan == 0.00:
    #             raise Warning(_("Please enter any number !"))

    # @api.depends('wage', 'unit_amount')
    # def _compute_total_wage(self):hr.expense.sheet
    #     for employee in self:
    #         employee.total_wage = self.wage - self.unit_amount

class expense_sheet_inherit(models.Model):

    _inherit = 'hr.expense.sheet'





