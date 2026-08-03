/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { TodoDoneCheckmark } from "@project_todo/components/todo_done_checkmark/todo_done_checkmark";

patch(TodoDoneCheckmark.prototype, {
    async onDoneToggled(ev) {
        // Execute the original toggle logic which updates the state in the backend
        await super.onDoneToggled(ev);
        
        // Force the Kanban/List view to reload immediately so that the card physically moves
        // to the "Done" stage (or back to its previous stage) without duplicating or staying behind.
        if (['kanban', 'list'].includes(this.props.viewType)) {
            if (this.props.record && this.props.record.model && this.props.record.model.root && typeof this.props.record.model.root.load === 'function') {
                await this.props.record.model.root.load();
            } else if (this.props.record && this.props.record.load) {
                await this.props.record.load();
            }
        }
    }
});
