from odoo import models, fields, api

class saleorder(models.Model):
    _inherit = 'sale.order'

    delivery_charge = fields.Float(string='Delivery Charge', compute='_compute_delivery_charge', store=True)


    @api.depends('order_line', 'amount_total')
    def _compute_delivery_charge(self):
        for order in self:
            delivery_charge = sum(line.price_subtotal for line in order.order_line) * 0.10
            order.delivery_charge = delivery_charge
            # order.amount_total = order.amount_untaxed + delivery_charge + order.amount_tax




    # @api.depends('amount_total')
    # def _compute_delivery_charge(self):
    #     for order in self:
    #         order.delivery_charge = order.amount_total * 0.10




# class invoiceOrder(models.Model):
#     _inherit = 'account.move'
#
#     delivery_charge = fields.Float(string='Delivery Charge', compute='_compute_delivery_charge', store=True)
#
#     @api.depends('amount_total')
#     def _compute_delivery_charge(self):
#         for order in self:
#             order.delivery_charge = order.amount_total * 0.10


class invoiceorder(models.Model):
    _inherit = 'account.move'

    @api.depends('invoice_line_ids')
    def _compute_delivery_charge(self):
        for invoice in self:
            delivery_charge = sum(line.price_subtotal for line in invoice.invoice_line_ids) * 0.10
            invoice.delivery_charge = delivery_charge
            # invoice.amount_total = invoice.amount_untaxed + delivery_charge + invoice.amount_tax



    delivery_charge = fields.Float(string='Delivery Charge', compute='_compute_delivery_charge', store=True)





