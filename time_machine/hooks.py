import logging
import os
from datetime import datetime

import time_machine
from dateutil.relativedelta import relativedelta

_logger = logging.getLogger(__name__)
_traveler = None
_state = None

def _to_int(value, default=0):
    if value in (None, ''):
        return default
    return int(value)


def _compute_fake_now(months=0):
    return datetime.now() + relativedelta(months=_to_int(months))


def stop_fake_time():
    global _traveler, _state
    if _traveler:
        _traveler.stop()
        _traveler = None
    _state = None
    _logger.warning('Fake time disabled; Odoo is back to real time.')



def apply_fake_time(*, enabled=True, months=0, source='runtime'):
    global _traveler, _state

    months = _to_int(months)
    desired_state = (bool(enabled), months)
    if _state == desired_state:
        return False

    stop_fake_time()
    if not enabled:
        return False

    fake_now = _compute_fake_now(months=months)
    _traveler = time_machine.travel(fake_now, tick=True)
    _traveler.start()
    _state = desired_state
    _logger.warning(
        'Fake time enabled from %s: fake_now=%s months=%s',
        source,
        fake_now,
        months,
    )
    return True



def apply_fake_time_from_env():
    months = os.getenv('ODOO_FAKE_TIME_MONTHS')
    if months is None:
        return False

    return apply_fake_time(months=months, source='environment variables')


def sync_fake_time_from_db(env, source='database'):
    params = env['ir.config_parameter'].sudo()
    enabled = params.get_param('time_machine.enabled', 'False') == 'True'
    months = params.get_param('time_machine.months', '0')
    return apply_fake_time(enabled=enabled, months=months, source=source)



def post_load():
    try:
        apply_fake_time_from_env()
    except Exception:
        _logger.exception('Could not initialize fake time during module post_load.')
