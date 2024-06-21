# Copyright 2024 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import SavepointCase


class TestEstimatedHours(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.milestone = cls.env["project.milestone"].create(
            {"name": "My Milestone", "estimated_hours": 10}
        )
        cls.milestone_copy = cls.milestone.copy()

    def test_estimated_hours_copy(self):
        assert (
            self.milestone.estimated_hours == self.milestone_copy.estimated_hours == 10
        )
