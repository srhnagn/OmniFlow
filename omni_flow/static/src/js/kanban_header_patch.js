/** @odoo-module **/

import { Group } from "@web/model/relational_model/group";
import { patch } from "@web/core/utils/patch";
import { browser } from "@web/core/browser/browser";

patch(Group.prototype, {
    setup(config, data) {
        super.setup(...arguments);
        const resModel = this.resModel || (this.config && this.config.resModel) || (this.model && this.model.resModel);
        
        if (resModel === "project.task" && this.groupByField && (this.groupByField.name === "omni_state" || this.groupByField.name === "personal_stage_type_id") && this.value) {
            const stateVal = Array.isArray(this.value) ? this.value[0] : this.value;
            if (stateVal) {
                const storageKey = `omniflow_fold_${this.groupByField.name}_${stateVal}`;
                const savedState = browser.localStorage.getItem(storageKey);
                if (savedState === "true") {
                    this.config.isFolded = true;
                } else if (savedState === "false") {
                    this.config.isFolded = false;
                }
            }
        }
    },

    async toggle() {
        const resModel = this.resModel || (this.config && this.config.resModel) || (this.model && this.model.resModel);
        
        // Native toggle
        const result = await super.toggle(...arguments);
        
        // Handle localStorage persistence for omni_state and personal_stage_type_id
        if (resModel === "project.task" && this.groupByField && (this.groupByField.name === "omni_state" || this.groupByField.name === "personal_stage_type_id") && this.value) {
            const stateVal = Array.isArray(this.value) ? this.value[0] : this.value;
            if (stateVal) {
                const isFolded = this.config ? this.config.isFolded : this.isFolded;
                const storageKey = `omniflow_fold_${this.groupByField.name}_${stateVal}`;
                browser.localStorage.setItem(storageKey, isFolded ? "true" : "false");
            }
        }
        
        return result;
    }
});
