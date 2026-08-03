# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProjectTask(models.Model):
    _inherit = 'project.task'

    omniflow_cover_image = fields.Image("Cover Image", max_width=1024, max_height=1024)
    omniflow_story_points = fields.Integer("Story Points", default=0, help="Agile story points for the task")
    omni_previous_stage_id = fields.Many2one('project.task.type', string='Previous Personal Stage')

    omni_state = fields.Selection([
        ('waiting', 'Waiting'),
        ('pending_start', 'Pending Start Approval'),
        ('in_progress', 'In Progress'),
        ('pending_finish', 'Pending Finish Approval'),
        ('done', 'Done')
    ], string='OmniFlow Status', default='waiting', tracking=True, required=True, group_expand='_expand_states')

    @api.model
    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).omni_state.selection]

    def write(self, vals):
        # Kaydetmeden önce eski stage'leri yakala (Done veya Cancelled'a gidenler için)
        if vals.get('state') in ['1_done', '1_canceled']:
            for task in self:
                if task.state not in ['1_done', '1_canceled'] and task.personal_stage_type_id:
                    task.omni_previous_stage_id = task.personal_stage_type_id

        res = super(ProjectTask, self).write(vals)
        
        # Odoo 17 To-Do app logic override: 
        if 'state' in vals:
            for task in self:
                if vals['state'] in ['1_done', '1_canceled']:
                    # Find the target stage for the current user
                    target_stage_name = 'Done' if vals['state'] == '1_done' else 'Cancelled'
                    target_stage = self.env['project.task.type'].search([
                        ('user_id', '=', self.env.uid),
                        ('name', '=', target_stage_name)
                    ], limit=1)
                    
                    # If the stage exists and the task is not already in it, move it.
                    if target_stage and task.personal_stage_type_id != target_stage:
                        task.personal_stage_type_id = target_stage.id
                else:
                    # Tick kaldırıldığında (örn: 01_in_progress)
                    if task.personal_stage_type_id and task.personal_stage_type_id.name in ['Done', 'Cancelled']:
                        if task.omni_previous_stage_id:
                            task.personal_stage_type_id = task.omni_previous_stage_id.id
                        else:
                            today_stage = self.env['project.task.type'].search([
                                ('user_id', '=', self.env.uid),
                                ('name', '=', 'Today')
                            ], limit=1)
                            if today_stage:
                                task.personal_stage_type_id = today_stage.id
                    
        return res

    def action_cancel_todo(self):
        # Allow toggling cancel state from a button
        for task in self:
            if task.state != '1_canceled':
                task.write({'state': '1_canceled'})
            else:
                task.write({'state': '01_in_progress'})
        return {'type': 'ir.actions.client', 'tag': 'reload'}


    # --- Worker Actions ---
    def action_request_start(self):
        for task in self:
            if task.omni_state != 'waiting':
                raise UserError(_("You can only request to start a task from the 'Waiting' state."))
            task.write({'omni_state': 'pending_start'})
            task.message_post(body=_("Requested approval to START the task."))

    def action_request_finish(self):
        for task in self:
            if task.omni_state != 'in_progress':
                raise UserError(_("You can only request to finish a task that is 'In Progress'."))
            task.write({'omni_state': 'pending_finish'})
            task.message_post(body=_("Requested approval to FINISH the task."))

    # --- Manager Actions ---
    def action_approve(self):
        for task in self:
            if task.omni_state == 'pending_start':
                task.write({'omni_state': 'in_progress'})
                task.message_post(body=_("Task START has been APPROVED by the Manager."))
            elif task.omni_state == 'pending_finish':
                task.write({'omni_state': 'done'})
                task.message_post(body=_("Task FINISH has been APPROVED by the Manager."))
            else:
                raise UserError(_("There is no pending approval for this task."))

    def action_reject(self):
        for task in self:
            if task.omni_state == 'pending_start':
                task.write({'omni_state': 'waiting'})
                task.message_post(body=_("Task START request was REJECTED. Sent back to Waiting."))
            elif task.omni_state == 'pending_finish':
                task.write({'omni_state': 'in_progress'})
                task.message_post(body=_("Task FINISH request was REJECTED. Sent back to In Progress."))
            else:
                raise UserError(_("There is no pending request to reject."))

    def action_open_modal(self):
        self.ensure_one()
        return {
            'name': _('Task Details'),
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }
