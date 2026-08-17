/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { browser } from "@web/core/browser/browser";

const STORAGE_KEY = "omniflow_theme";
const LIGHT_CLASS = "omniflow-light";

// ─── Apply theme before first render (flash önleme) ──────────────────────────
// Bu kod modül yüklenirken (bileşen mount edilmeden önce) çalışır.
(function applyThemeEarly() {
    const stored = browser.localStorage.getItem(STORAGE_KEY);
    // Varsayılan: light. Eğer "dark" kaydedilmişse light class'ı ekleme.
    if (stored !== "dark") {
        document.body.classList.add(LIGHT_CLASS);
    } else {
        document.body.classList.remove(LIGHT_CLASS);
    }
})();

// ─── Systray Component ────────────────────────────────────────────────────────
export class ThemeToggle extends Component {
    setup() {
        const stored = browser.localStorage.getItem(STORAGE_KEY);
        this.state = useState({
            isLight: stored !== "dark",
        });
    }

    toggle() {
        this.state.isLight = !this.state.isLight;
        if (this.state.isLight) {
            document.body.classList.add(LIGHT_CLASS);
            browser.localStorage.setItem(STORAGE_KEY, "light");
        } else {
            document.body.classList.remove(LIGHT_CLASS);
            browser.localStorage.setItem(STORAGE_KEY, "dark");
        }
    }
}

ThemeToggle.template = "omni_flow.ThemeToggle";
ThemeToggle.props = {};

// sequence: 25 → kullanıcı avatarının hemen solunda görünür
registry.category("systray").add("omni_flow.theme_toggle", {
    Component: ThemeToggle,
}, { sequence: 25 });
