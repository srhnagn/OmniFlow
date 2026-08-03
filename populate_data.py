print("Wiping existing tasks and projects...")
env['project.task'].search([]).unlink()
if 'project.update' in env:
    env['project.update'].search([]).unlink()
env['project.project'].search([]).unlink()

# Delete non-standard users
users_to_delete = env['res.users'].search([('id', 'not in', [1, 2])])
users_to_delete.unlink()

# 1. Update Company
company = env['res.company'].search([], limit=1)
if company:
    company.write({'name': 'Çanakkale Seramik A.Ş.'})
else:
    company = env['res.company'].create({'name': 'Çanakkale Seramik A.Ş.'})

# Update main admin user name just in case
admin = env.ref('base.user_admin')
admin.write({'name': 'Admin'})

manager_group = env.ref('omni_flow.group_omniflow_manager')

# List of users from kaleseramik_test_db
ks_users = [
    ('Serhan Ağan', 'serhan.agan@kaleseramik.com', True), # Manager
    ('Emre Şahin', 'emre.sahin@kaleseramik.com', False),
    ('Murat Demir', 'murat.demir@kaleseramik.com', False),
    ('Fatma Çelik', 'fatma.celik@kaleseramik.com', False),
    ('Elif Yıldız', 'elif.yildiz@kaleseramik.com', False),
    ('Hakan Öztürk', 'hakan.ozturk@kaleseramik.com', False),
    ('Gizem Arslan', 'gizem.arslan@kaleseramik.com', False),
    ('Ahmet Koç', 'ahmet.koc@kaleseramik.com', False),
    ('Esra Bulut', 'esra.bulut@kaleseramik.com', False),
    ('Cemile Kılıç', 'cemile.kilic@kaleseramik.com', False),
    ('Burak Yılmaz', 'burak.yilmaz@kaleseramik.com', False),
    ('Zeynep Kaya', 'zeynep.kaya@kaleseramik.com', False)
]

user_records = []
for name, email, is_manager in ks_users:
    u = env['res.users'].create({
        'name': name,
        'login': email,
        'password': '123',
        'company_id': company.id,
        'company_ids': [(4, company.id)],
        'groups_id': [(4, env.ref('base.group_user').id)]
    })
    if is_manager:
        u.groups_id = [(4, manager_group.id)]
    user_records.append(u)

# Create a Project
project = env['project.project'].create({
    'name': 'ERP Dijital Dönüşüm v2',
    'description': 'Kaleseramik iç süreçlerinin dijitalleştirilmesi ve yeni ERP entegrasyonu.',
    'user_id': user_records[0].id, # Serhan Ağan
    'company_id': company.id
})

# Create Tasks filling ALL Kanban columns
tasks = [
    {'name': 'Veritabanı Analizi', 'desc': 'Eski veritabanı yapısının incelenmesi', 'state': 'waiting', 'sp': 3, 'user': user_records[1]},
    {'name': 'Banka API Yazılımı', 'desc': 'Garanti bankası API uçlarının sisteme tanıtılması', 'state': 'waiting', 'sp': 8, 'user': user_records[2]},
    {'name': 'UI Tasarım Konsepti', 'desc': 'Kullanıcı arayüzü Figma üzerinde çizilecek', 'state': 'pending_start', 'sp': 5, 'user': user_records[3]},
    {'name': 'Sunucu Altyapı Kurulumu', 'desc': 'Ubuntu server kurulumu', 'state': 'in_progress', 'sp': 13, 'user': user_records[4]},
    {'name': 'Güvenlik Testleri', 'desc': 'Sızma testleri ve yetki kontrolü', 'state': 'in_progress', 'sp': 8, 'user': user_records[5]},
    {'name': 'Proje Yönetim Modülü Entegrasyonu', 'desc': 'Odoo Discuss modülünün özelleştirilmesi', 'state': 'pending_finish', 'sp': 20, 'user': user_records[6]},
    {'name': 'Personel Eğitim Dokümanı', 'desc': 'Wiki sayfasının hazırlanması', 'state': 'pending_finish', 'sp': 2, 'user': user_records[7]},
    {'name': 'Eski Verilerin Taşınması', 'desc': 'CSV aktarımı ve temizlik', 'state': 'done', 'sp': 13, 'user': user_records[8]},
    {'name': 'Modül Test ve QA', 'desc': 'Test ekibinin modülü son kullanıcı gözüyle incelemesi', 'state': 'done', 'sp': 5, 'user': user_records[9]},
]

for t in tasks:
    env['project.task'].create({
        'name': t['name'],
        'description': f"<h1>{t['name']}</h1><p>{t['desc']}</p>",
        'project_id': project.id,
        'user_ids': [(4, t['user'].id)],
        'omni_state': t['state'],
        'omniflow_story_points': t['sp']
    })

env.cr.commit()
print("REAL DUMMY DATA POPULATED SUCCESSFULLY!")
