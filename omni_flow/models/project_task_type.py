# -*- coding: utf-8 -*-
from odoo import models, api, _
from odoo.exceptions import UserError

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    def unlink(self):
        for stage in self:
            if stage.name in ['Done', 'Cancelled'] and stage.user_id:
                raise UserError(_("The '%s' stage is critical for OmniFlow and cannot be deleted. If you don't want to use it, you can fold it.", stage.name))
        return super(ProjectTaskType, self).unlink()

    @api.model
    def action_load_default_stages(self):
        # Only load for the current user
        user_id = self.env.uid
        default_stages = ['Unscheduled', 'Today', 'This Week', 'This Month', 'Later', 'Done', 'Cancelled']
        
        existing_stages = self.search([('user_id', '=', user_id)])
        existing_names = existing_stages.mapped('name')
        
        sequence = 10
        for stage_name in default_stages:
            should_fold = stage_name in ['Done', 'Cancelled']
            
            if stage_name not in existing_names:
                self.create({
                    'name': stage_name,
                    'user_id': user_id,
                    'sequence': sequence,
                    'fold': should_fold
                })
            else:
                # Update existing stage to ensure correct sequence and fold state
                stage = existing_stages.filtered(lambda s: s.name == stage_name)
                stage.write({
                    'sequence': sequence,
                    'fold': should_fold
                })
            sequence += 10
            
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
