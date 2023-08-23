from odoo import models, fields, api ,  exceptions

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_cost = fields.Float(string='Minimum Cost' , required=True)
    brand_name = fields.Char(string='Brand Name', required=True)




class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    brand_name = fields.Char(related='product_id.brand_name', string='Brand Name', store=True, readonly=True,required=True)

    @api.onchange('product_id', 'price_unit')
    def _onchange_product_price_unit(self):
        if self.product_id and self.price_unit < self.product_id.minimum_cost:
            self.price_unit = self.product_id.minimum_cost
            return {
                'warning': {
                    'title': "Price Adjustment",
                    'message': f"The unit price cannot be less than the minimum cost of {self.product_id.minimum_cost}."
                }
            }