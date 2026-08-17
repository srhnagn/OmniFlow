# -*- coding: utf-8 -*-
{
    'name': "OmniFlow",
    'summary': "Modern Agile Project Management Workspace",
    'description': """
        OmniFlow is a Trello/Notion-inspired agile project management workspace built on Odoo.
        It features a premium user interface, drag-and-drop Kanban boards, and rich-text documentation.
    """,
    'author': "Omni",
    'website': "https://www.omniflow.dev",
    'category': 'Project Management',
    'application': True,
    'version': '0.1',
    'depends': ['base', 'project', 'mail', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/omniflow_task_views.xml',
        'views/menu_overrides.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'omni_flow/static/src/scss/backend_overrides.scss',
            'omni_flow/static/src/scss/omniflow_kanban.scss',
            'omni_flow/static/src/js/todo_done_checkmark_patch.js',
            'omni_flow/static/src/js/kanban_header_patch.js',
            'omni_flow/static/src/js/theme_toggle.js',
            'omni_flow/static/src/xml/kanban_header_override.xml',
            'omni_flow/static/src/xml/theme_toggle.xml',
        ],
    },
    'installable': True,
}
