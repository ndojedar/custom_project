# -*- coding: utf-8 -*-

from odoo import models, fields, _ 


class CustomProject(models.Model):
     _inherit = "project.project"

     ref_cliente = fields.Char(
          comodel_name='sale.order',  
          related='sale_order_id.client_order_ref', 
          string='Referencia del Cliente',
          readonly=True, 
          store=True
          )

    