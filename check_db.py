import sys
import odoo
odoo.tools.config.parse_config(['-c', '/Users/serhanagan/Developer/OmniFlow/odoo.conf', '-d', 'omniflow_db'])
registry = odoo.registry('omniflow_db')
with registry.cursor() as cr:
    env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
    view = env['ir.ui.view'].search([('name', '=', 'omniflow.todo.task.kanban.override')])
    print('View found:', bool(view))
    if view:
        print('View active:', view.active)
        print('Inherit ID:', view.inherit_id.xml_id if view.inherit_id else None)
