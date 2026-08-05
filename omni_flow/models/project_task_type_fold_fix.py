from odoo import models, api

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    def write(self, vals):
        # Allow users to save their fold state even if they don't have write access?
        # But wait, they DO have write access.
        return super().write(vals)
