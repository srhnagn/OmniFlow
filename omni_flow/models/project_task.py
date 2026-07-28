# -*- coding: utf-8 -*-
from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    # We are inheriting to ensure we can customize behavior later.
    # Odoo's native 'description' is already an HTML field, which works perfectly for our Notion-style rich text.
    # We can add custom fields for Trello-like cover images or agile points.
    
    omniflow_cover_image = fields.Image("Cover Image", max_width=1024, max_height=1024)
    omniflow_story_points = fields.Integer("Story Points", default=0, help="Agile story points for the task")
