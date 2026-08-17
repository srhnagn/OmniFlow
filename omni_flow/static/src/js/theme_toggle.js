/** @odoo-module **/

import { Component, useState, onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";

const STORAGE_KEY = "omniflow_theme";
const LIGHT_CLASS = "omniflow-light";

// ─── Systray Component ────────────────────────────────────────────────────────
export class ThemeToggle extends Component {
    setup() {
        // localStorage'dan oku — varsayılan: light
        const stored = window.localStorage.getItem(STORAGE_KEY);
        const isLight = stored !== "dark";

        this.state = useState({ isLight });

        // Mount olunca body class'ını doğru ayarla
        onMounted(() => {
            this._applyClass(this.state.isLight);
        });
    }

    toggle() {
        this.state.isLight = !this.state.isLight;
        this._applyClass(this.state.isLight);
        window.localStorage.setItem(STORAGE_KEY, this.state.isLight ? "light" : "dark");
    }

    _applyClass(isLight) {
        if (isLight) {
            document.body.classList.add(LIGHT_CLASS);
        } else {
            document.body.classList.remove(LIGHT_CLASS);
        }
    }
}

ThemeToggle.template = "omni_flow.ThemeToggle";
ThemeToggle.props = {};

registry.category("systray").add("omni_flow.theme_toggle", {
    Component: ThemeToggle,
}, { sequence: 25 });
