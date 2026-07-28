#!/bin/bash
# start.sh for OmniFlow

VENV="/Users/serhanagan/Developer/Odoo Core/venv/bin/python"
ODOO_BIN="/Users/serhanagan/Developer/Odoo Core/odoo-bin"
CONF="/Users/serhanagan/Developer/OmniFlow/odoo.conf"

echo "Starting Odoo 17 for OmniFlow..."
"$VENV" "$ODOO_BIN" -c "$CONF" "$@"
