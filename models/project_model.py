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

     albaranes_count = fields.Integer(
        compute='_compute_albaranes_count',
        string='Numero de Albaranes'
     )


     def _compute_albaranes_count(self):
          for rec in self:
               albaranes= self.env["project.albaran"].search([("project_id","=", rec.id)])
               rec.albaranes_count = len(albaranes)


     #acción para mostrar los albaranes relacionados
     def albaranes_project_action(self):
          action = self.env.ref('custom_project.view_tree_albaran_project').read()[0]
          return action
