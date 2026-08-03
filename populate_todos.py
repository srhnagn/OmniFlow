admin_user = env['res.users'].search([('login', '=', 'admin')], limit=1)

todo_items = [
    'Staj defteri doldurulacak',
    'Bulgar oturum',
    'Longines pil',
    'Bitirme projesi',
    'Spora uyelik',
    'Arac kamerasi',
    'Araba cizik',
    'Gunes gozlugu',
    "Mac'e monitör",
    'Parfum',
    'Saat kutusu'
]

for item in todo_items:
    env['project.task'].create({
        'name': item,
        'user_ids': [(4, admin_user.id)] if admin_user else [],
        'project_id': False,
        'omni_state': 'waiting'
    })

env.cr.commit()
print('To-Do list populated successfully!')
