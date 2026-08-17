/** @odoo-module **/

import { Component, useState, onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { browser } from "@web/core/browser/browser";

const STORAGE_KEY = "omniflow_theme";
const LIGHT_CLASS = "omniflow-light";

/**
 * Reads the saved theme from localStorage and applies it to <body>.
 * Called immediately on module load so there's no flash of dark mode.
 */
function applyStoredTheme() {
    const saved = browser.localStorage.getItem(STORAGE_KEY);
    // Default is light mode — only go dark if explicitly saved as "dark"
    if (saved === "dark") {
        document.body.classList.remove(LIGHT_CLASS);
    } else {
        document.body.classList.add(LIGHT_CLASS);
    }
}

// Apply immediately (before any component mounts) to prevent flash
applyStoredTheme();

class ThemeToggle extends Component {
    static template = "omni_flow.ThemeToggle";
    static props = {};

    setup() {
        const saved = browser.localStorage.getItem(STORAGE_KEY);
        this.state = useState({
            isLight: saved !== "dark",  // default: light
        });

        onMounted(() => {
            this._applyTheme(this.state.isLight);
        });
    }

    _applyTheme(isLight) {
        if (isLight) {
            document.body.classList.add(LIGHT_CLASS);
        } else {
            document.body.classList.remove(LIGHT_CLASS);
        }
        browser.localStorage.setItem(STORAGE_KEY, isLight ? "light" : "dark");
    }

    toggle() {
        this.state.isLight = !this.state.isLight;
        this._applyTheme(this.state.isLight);
    }
}

registry.category("systray").add("omniflow.theme_toggle", {
    Component: ThemeToggle,
    sequence: 5,  // sağda, kullanıcı avatarının yanına yerleş
});
