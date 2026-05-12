from odoo import models

from ..hooks import sync_fake_time_from_db


class IrCron(models.Model):
    _inherit = 'ir.cron'

    def _callback(self, cron_name, server_action_id):
        sync_fake_time_from_db(self.env, source='cron worker')
        return super()._callback(cron_name, server_action_id)
