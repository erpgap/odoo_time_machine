# -*- coding: utf-8 -*-
{
    'name': 'Time Machine',
    'version': '19.0.1.0.0',
    'category': 'Tools',
    'summary': 'Shift Odoo backward or forward by a month offset',
    'author': 'Diogo Duarte (ERPGAP)',
    'description': '''
Time Machine makes Odoo behave as if the current date and time were shifted by
an integer number of months relative to the real system clock.

Typical use cases:
- preparing demos with past or future business dates
- reproducing month-sensitive bugs
- validating scheduled flows and date-based logic
- testing reporting, renewals, deadlines, and reminders

Configuration:
- from General Settings with an enable toggle and month offset
- from the ODOO_FAKE_TIME_MONTHS environment variable at startup

After changing the configuration, restarting Odoo is recommended so HTTP
workers, cron workers, and background processes all use the same shifted clock.
    ''',
    'depends': ['base_setup'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'external_dependencies': {
        'python': ['time_machine', 'dateutil'],
    },
    'post_load': 'post_load',
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
