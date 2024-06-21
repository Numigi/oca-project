# Copyright 2024 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectMilestone(models.Model):
    _inherit = "project.milestone"

    estimated_hours = fields.Float(string="Estimated Hours")
