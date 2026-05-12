from odoo import models
from odoo.http import request

from ..hooks import sync_fake_time_from_db


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _dispatch(cls, endpoint):
        sync_fake_time_from_db(request.env, source='HTTP request')
        return super()._dispatch(endpoint)
