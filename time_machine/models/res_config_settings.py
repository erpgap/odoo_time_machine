from odoo import fields, models

from ..hooks import apply_fake_time


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    time_machine_enabled = fields.Boolean(
        string='Enable fake time',
        config_parameter='time_machine.enabled',
    )
    time_machine_months = fields.Integer(
        string='Month offset',
        config_parameter='time_machine.months',
        default=0,
        help='Number of months to move backward or forward from the real current time.',
    )

    def set_values(self):
        res = super().set_values()
        for settings in self:
            apply_fake_time(
                enabled=settings.time_machine_enabled,
                months=settings.time_machine_months,
                source='Settings > General Settings',
            )
        return res
