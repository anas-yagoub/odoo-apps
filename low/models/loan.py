from odoo import models, fields, api, _

# from server.odoo.addons.ohrms_loan.models.hr_loan import HrLoan


class employee_loan(models.Model):

    _name = 'hr.loan'

    employee_id = fields.Many2one('hr.employee', string="Employee")
    loan = fields.Float(string="Loan")
    loan_date = fields.Date(string="Loan Date")
    total_wage = fields.Float(string="Total Wage", compute='_compute_total_wage')
    wage = fields.Float(string="Wage", related='employee_id.wage')
    # name_scq = fields.Char(string="loan Id", required=True, copy=False, readonly=True,
    #                        index=True, default=lambda self: _('New'))
    #
    # @api.model
    # def create(self, vals):
    #     if vals.get('name_scq', _('New')) == _('New'):
    #         vals['name_scq'] = self.env['ir.sequence'].next_by_code('hr.loan.sequence') or _('New')
    #     result = super(low, self).create(vals)
    #     return result

    @api.depends('wage','loan')
    def _compute_total_wage(self):
        for rec in self:
            rec.total_wage = self.wage - self.loan






