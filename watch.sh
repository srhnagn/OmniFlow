#!/bin/bash
# watch.sh for OmniFlow

MODULE_NAME="omni_flow"
VENV="/Users/serhanagan/Developer/Odoo Core/venv/bin/python"
ODOO_BIN="/Users/serhanagan/Developer/Odoo Core/odoo-bin"
CONF="/Users/serhanagan/Developer/OmniFlow/odoo.conf"

echo "Starting OmniFlow watcher (using Odoo native dev mode)..."
"$VENV" "$ODOO_BIN" -c "$CONF" -u "$MODULE_NAME" --dev=all
