# OmniFlow - Business Workflow & Internal Communication Platform

OmniFlow is an Odoo 17-based centralized platform designed for comprehensive team task tracking, internal communication, and project management. It transforms scattered, disorganized communication across emails and messaging apps into a structured, manager-approved workflow environment.

## ✨ Key Features

* **Manager-Approved Task Workflow:** Unlike standard task managers where anyone can move cards freely, OmniFlow enforces a strict approval mechanism. Tasks transitioning between "Waiting", "In Progress", and "Done" states must pass through a Project Manager's approval, ensuring complete managerial control over project progression.
* **Custom Kanban Boards:** Highly visual, custom Kanban card designs optimized for quick status reading. Features quick-action buttons (Red X for Cancel, Green Tick for Done) directly on the cards for one-click stage transitions.
* **State Persistence & Core Overrides:** Native Odoo JavaScript OWL behaviors were patched to provide true "Fold Memory Persistence", meaning collapsed columns are saved directly to the database. Core system stages ('Done', 'Cancelled') are protected at the Python ORM level to prevent accidental deletion.
* **Rich Text Task Documents:** Moving away from classic, rigid ERP form layouts to a wide, clean, Notion-style document structure that focuses on Rich Text editing for extensive task descriptions and collaborative notes. Includes a custom onboarding placeholder ("Welcome to Task Details").
* **Centralized Internal Communication:** Customized Odoo Discuss framework integrations that provide a Slack/Teams-like structure directly embedded within task records, allowing teams to collaborate in context without leaving the platform.
* **Dark Theme Optimized:** Deep UI/UX overrides with carefully crafted CSS/SCSS ensuring the entire task management experience is easy on the eyes and professionally styled.

## 🛠 Tech Stack

* **Backend:** Python 3.10+, Odoo 17 Framework, PostgreSQL 17
* **Frontend:** Odoo Web Library (OWL) JS, QWeb (XML), SCSS, Bootstrap
* **Architecture:** Custom Models, UI/UX Overrides, Workflow State Machines

## 🚀 Installation Guide

1. Clone or download the repository into your Odoo `addons/` directory.
2. Ensure the path is properly defined in your `odoo.conf` file under `addons_path`.
3. Enable **Developer Mode** in the Odoo web interface.
4. Go to the **Apps** menu and click **Update Apps List**.
5. Search for the **OmniFlow** module and click **Activate**.

## 🤝 Workflow Logic (Business Rules)

The core philosophy of OmniFlow revolves around **Controlled Progress**. 
If a team member finishes a task and marks it as "Done", it does not officially close until a Manager reviews the outcome. If rejected, the manager can revert the task back to the "Waiting" or "In Progress" state with feedback. This rigorous approval mechanism forms the backbone of the OmniFlow task management system, guaranteeing high-quality deliverables.

---

**Proprietary License**
All copyrights of this software belong to its developer. The source codes cannot be copied, reproduced, distributed without permission, modified, or sold commercially under a different brand/name. Any commercial use, installation, and corporate integration of the software are strictly subject to the developer's exclusive permission and license agreements.
