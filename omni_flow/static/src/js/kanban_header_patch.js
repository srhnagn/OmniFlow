/** @odoo-module **/

import { Group } from "@web/model/relational_model/group";
import { patch } from "@web/core/utils/patch";

patch(Group.prototype, {
    async toggle() {
        const resModel = this.resModel || (this.config && this.config.resModel) || (this.model && this.model.resModel);
        const isOmniFlow = resModel === "project.task" && this.groupByField && this.groupByField.name === "personal_stage_type_id";
        
        // Native toggle
        const result = await super.toggle(...arguments);
        
        if (isOmniFlow && this.value) {
            // value could be an array [id, label] or just id
            const stageId = Array.isArray(this.value) ? this.value[0] : this.value;
            
            if (stageId && this.model && this.model.orm) {
                // Force save the fold state to the database for the user's personal stage
                const isFolded = this.config ? this.config.isFolded : this.isFolded;
                await this.model.orm.write("project.task.type", [stageId], {
                    fold: isFolded,
                });
            }
        }
        
        return result;
    }
});
