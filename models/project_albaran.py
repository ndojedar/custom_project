# -*- coding: utf-8 -*-

from odoo import api, models, fields, _


class ProjectAlbaran(models.Model):
    _name = "project.albaran"

    name = fields.Char(
        string="Nº de albarán", 
        readonly=True
    )

    tipo_albaran = fields.Selection(
        string="Tipo de albarán",
        selection=[
                ('cierre', 'Cierre'),
                ('entrega', 'Entrega')
        ],
    )

    fecha_alb = fields.Date(string="Fecha albarán")
    
    partner_id = fields.Many2one(
        string="Cliente",
        comodel_name="res.partner",
        readonly=True
    )

    partner_id_adr = fields.Many2one(
        string="Dirección de entrega",
        comodel_name="res.partner"
    )

    project_id = fields.Many2one(
        string="Proyecto",
        comodel_name="project.project",
        readonly=True
    )

    saleorder_id = fields.Many2one(
        string="Pedido de venta",
        comodel_name="sale.order",
        readonly=True
    )

    ref_cliente = fields.Char(
        string='Referencia del Cliente',
        related='project_id.ref_cliente',  
        readonly=True
    )

    resp_project_id = fields.Char(
        string='Responsable de Proyecto',
        related='project_id.user_id.name',  
        readonly=True
    )

    bam_id = fields.Char(
        string='Business Area Manager',
        related='project_id.business_area_manager.name',
        readonly=True
    )

    comentarios = fields.Text("Comentarios")

    albaranes_lines_ids = fields.One2many(
        string="Líneas de albarán",
        comodel_name="project.albaran.lines", 
        inverse_name="project_albaran_id" 
    )


    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('albaran.secuence') or 'ALB'
        result = super(ProjectAlbaran, self).create(vals)
        return result



class ProjectAlbaranLines(models.Model):
    _name = "project.albaran.lines"

    project_albaran_id = fields.Many2one(string="Albarán", comodel_name="project.albaran")
    concepto = fields.Text("Concepto", Require=True)
    cantidad = fields.Integer("Cantidad")
    precio = fields.Float("Valor importe")
    