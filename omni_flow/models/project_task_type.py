from odoo import models, api

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        res = super().search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)
        # Force all personal stages (To-Do stages) to remain open (unfolded) in the UI
        if fields and 'fold' in fields:
            for r in res:
                if r.get('user_id'):
                    r['fold'] = False
        return res
