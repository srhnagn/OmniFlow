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
2.  **Task Detail Form:** Moved away from the classic ERP form layout to a Notion-style, wide, clean, and Rich Text-focused document structure. A custom HTML/CSS placeholder ("Welcome to Task Details") was injected to guide users to use the space like a collaborative document workspace.
3.  **Manager Approval Workflow:** Just like inventory movements in KS Envanter require management approval before taking effect, project tasks must also go through a Project Manager's approval to transition between "Ideas", "In Progress", and "Done" states. A task can only begin processing or be moved to "Done" after this approval. Furthermore, if a task is marked as "Done" but the manager rejects the outcome, the manager can revert the task back to the "Ideas" state. This rigorous approval mechanism will form the core of the task management system.


## 📖 Internship Logbook Strategy: The Genesis of KS Akış
*   **Intellectual Property (IP) Shield & Odoo Transformation (The VSCode & Antigravity Analogy):** When the company management requested a project management module to strengthen interdepartmental communication, finding Trello and Notion inadequate in my daily life, I put the **"OmniFlow"** core, which I had previously coded entirely for my own personal use (free and secure), on the table. OmniFlow was originally a web application that I had written for my own ambitions. However, because the manager's request was specifically directed towards Odoo, we will first transform it into an Odoo module. After this OmniFlow module is finished, in the remaining internship days, just like how the open-source VSCode core was customized and transformed into the Antigravity IDE, I built the **'KS Akış'** application by modifying my own OmniFlow core according to the company's corporate departmental structure and manager approval mechanisms.
*   **Vibe Coding and the Manager's Philosophy:** Our manager's visionary comment regarding my rapid and flawless delivery of the project became the fundamental philosophy of my internship: *"Leave the grunt work (manual coding) to Artificial Intelligence (Agents), and dedicate all your mental focus to designing a flawless Software Architecture and User Experience (UX). Learning to achieve maximum efficiency in minimum time with vibe coding will be your greatest professional experience."* By this means, without bothering to write code, I devoted all my energy to constructing a tremendous corporate architecture.

---

## 🏗️ Architectural Decisions & Guidelines (Agreed upon on 31.07.2026)

1. **Design Language (Strategic & Minimalist):** Unlike the operational/neon focus of KS IT Envanter, OmniFlow targets a strategic/documentary environment (akin to Notion or Asana). The dark mode will be clean, minimalist, and use a grayscale palette to maximize reading comfort for long rich-text descriptions. Neon colors will only be used for strict status indicators (badges) to maintain high contrast without overwhelming the interface.

2. **Kanban Columns & Language Policy:** The entire OmniFlow module will be developed **100% in English** (both code and UI/XML). Odoo's default Stage mechanics will be entirely bypassed. Instead, Kanban columns will be strictly bound to a custom `omni_state` field consisting of 6 fixed steps: `Ideas`, `Pending Start Approval`, `In Progress`, `Pending Finish Approval`, `Done`, and `Cancelled`. To prevent system breakage, core stages like 'Done' and 'Cancelled' are protected at the ORM level (via `unlink` overrides) and cannot be deleted by users. A "Load Default Stages" utility is provided to restore any missing columns. To ensure all tasks follow this correct lifecycle, the global Odoo "New" button is hidden via CSS, strictly forcing users to initiate new tasks using only the Quick Create `+` button inside the `Ideas` column.

3. **Core OWL Overrides & Persistence:** To provide a flawless user experience, Odoo's native virtual DOM mechanics were patched using JavaScript (`Group.prototype.toggle`). This ensures that Kanban column folding states are written directly to the database in real-time, providing true "Fold Memory Persistence". Quick-action UI buttons (like a Red X for Cancel and Green Tick for Done) were strategically injected into the Kanban cards using XML XPATHs.

4. **Manager Role & Scalability:** To ensure the system remains fully scalable from small IT departments (Manager + Staff) to large corporate structures, a dedicated Odoo security group named `group_omniflow_manager` will be created. Critical approval buttons (Approve/Reject) will only be visible and accessible to members of this group, ensuring the system remains completely dynamic and not hardcoded to a specific user.

5. **Omni App Ecosystem Integration:** Once the core OmniFlow module is complete, all Omni applications will be unified under a single, overarching 'Omni' Waffle Menu to solidify the software suite's branding.

6. **Strict Kanban vs. Free Editor (Trello-Notion Duality):** To preserve the structural integrity of the Kanban board, strict CSS rules ("Armored CSS") enforce maximum font sizes on cards (Headers: 21px, Body: 15px). Conversely, inside the task detail Modal, users are given total "Notion-style" freedom to format rich text (colors, sizes, styles) without breaking the outer board layout.