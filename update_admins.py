import sys
sys.path.append('/Users/serhanagan/Developer/Odoo Core')
import odoo
from odoo import api, SUPERUSER_ID

odoo.tools.config.parse_config(['-c', '/Users/serhanagan/Developer/OmniFlow/odoo.conf'])

databases = ['kaleseramik_test_db', 'omniasset_db', 'omniflow_db']

for db_name in databases:
    try:
        print(f"Connecting to {db_name}...")
        registry = odoo.registry(db_name)
        with registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            
            admin_user = env.ref('base.user_admin', raise_if_not_found=False)
            if admin_user:
                admin_user.write({
                    'login': 'admin',
                    'password': 'admin'
                })
                env.cr.commit()
                print(f"[{db_name}] Successfully updated admin login and password.")
            else:
                print(f"[{db_name}] Could not find base.user_admin")
    except Exception as e:
        print(f"[{db_name}] Error: {e}")
