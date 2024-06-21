# Copyright 2024 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project Milestone Estimated Hours",
    "version": "14.0.1.0.0",
    "author": "Numigi, Odoo Community Association (OCA)",
    "maintainer": "Numigi",
    "website": "https://github.com/OCA/project",
    "license": "AGPL-3",
    "category": "Project",
    "summary": "Add possibility to set estimated hours in a project milestone",
    "depends": ["project_milestone_enhanced"],  # TO DO: check the dependency
    "data": [
        "views/project_milestone.xml",
        "views/project.xml",
    ],
    "installable": True,
}
