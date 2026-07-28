# OmniFlow - Blueprint

## Internship Report Story (To Be Enhanced)

**Project:** OmniFlow - Internal Communication and Project/Task Management Platform

**Story Summary & Potential:**
"The team's task tracking and communication were scattered across different platforms (WhatsApp, Email, disorganized lists). Task statuses, approval workflows, and individual responsibilities could not be effectively tracked. To solve this issue, I designed a single centralized platform (OmniFlow) using the Odoo framework."

**Story Layers:**
*   **🔴 Problem:** Disorganized communication, inability to track tasks, and lack of managerial control over task statuses (progress, completion).
*   **🔧 Solution Process:** Customizing the Odoo Discuss module into a Slack/Teams-like structure, implementing a dark theme, custom Kanban card designs, and establishing a **Manager-Approved Task Workflow**.
*   **🟢 Result:** The entire team communicates through a single interface, and task statuses cannot change without managerial approval, ensuring complete control.
*   **📊 Technical Depth:** UI/UX overrides, Kanban XML modifications, and implementing custom models and state overrides for the approval mechanism.

---

## 📝 Internship Report Framework (Template for All Projects)

When writing each project into the internship logbook, the following structure must be followed:

1.  **Current Situation (Problem):** How company X was doing Y, and the specific problems they faced.
2.  **Analysis:** The requirements and solutions I identified.
3.  **Design:** Data models, user flows, and technical architecture.
4.  **Development:** Which technologies were chosen, why they were chosen, and the technical challenges encountered.
5.  **Conclusion:** Manager/user reactions and the actual business value delivered.

---

## 🔜 Future Developments (Pending Features)
1.  **Kanban Card Customization:** Enhancing Kanban cards with a custom, highly visual design (similar to Trello).
2.  **Task Detail Form:** Moving away from the classic ERP form layout to a Notion-style, wide, clean, and Rich Text-focused document structure.
3.  **Manager Approval Workflow:** Just like inventory movements in KS Envanter require management approval before taking effect, project tasks must also go through a Project Manager's approval to transition between "Waiting", "In Progress", and "Done" states. A task can only begin processing or be moved to "Done" after this approval. Furthermore, if a task is marked as "Done" but the manager rejects the outcome, the manager can revert the task back to the "Waiting" state. This rigorous approval mechanism will form the core of the task management system.
