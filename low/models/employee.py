from odoo import models, fields, api, _

class employee_inherit(models.Model):

    _inherit = 'hr.employee'
    employee_id = fields.Many2one('hr.employee', string="Employee")
    loan = fields.Float(string="Loans")
    loan_date = fields.Date(string="Loan Date")

    # total_wage = fields.Float(string="Total Wage",related='expense_id.total_wage')

class employee_public(models.Model):

    _inherit = 'hr.employee.public'


class account_journal(models.Model):

    _inherit = 'account.move'






