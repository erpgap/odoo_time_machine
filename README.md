# Time Machine

Time Machine is an Odoo 19 module that shifts Odoo's perceived current date and time by a whole-number month offset.

It is meant to be simple: move Odoo backward or forward by `N` months, and let time continue progressing normally from that shifted point.

## Features

- Shift Odoo into the past or future
- Use a single month offset value
- Configure from **Settings > General Settings > Time Machine**
- Configure from `ODOO_FAKE_TIME_MONTHS` at startup
- Applies the shift immediately in the current process when settings are saved
- Shifted time continues to progress normally

## How it works

The module uses the Python package `time_machine` to override the perceived current time inside the running Odoo process.

The shifted current datetime is computed as:

- `real current datetime + month offset`

Examples:

- `-1` moves Odoo one month into the past
- `+2` moves Odoo two months into the future
- `0` applies no shift

## Configuration from Odoo Settings

After installing the module, go to:

- **Settings > General Settings > Time Machine**

Available options:

- **Enable fake time**: turn the shift on or off
- **Month offset**: negative for the past, positive for the future

## Configuration from environment variables

You can configure the shift when starting Odoo with:

- `ODOO_FAKE_TIME_MONTHS`

Example:

```bash
export ODOO_FAKE_TIME_MONTHS=-1
```

Notes:

- If `ODOO_FAKE_TIME_MONTHS` is not set, the module does nothing at startup
- `0` is valid and means no shift
- The environment variable acts as an implicit enable flag

## Dependencies

Python packages:

```bash
pip install time-machine python-dateutil
```

## Important behavior notes

- Saving settings applies the shift immediately in the current Odoo process
- A full Odoo restart is still recommended after configuration changes
- In multi-worker setups, restart all workers so they all share the same shifted clock
- This module is best suited for demos, development, testing, and troubleshooting

## Typical use cases

- Move Odoo to the previous month for accounting demos
- Move Odoo forward a few months to preview renewals or expirations
- Reproduce bugs that only happen around month boundaries
- Validate scheduled activities and date-based business flows

## Technical note

The module initializes environment-based shifting in the module `post_load` hook and reapplies the shift when settings are saved through `res.config.settings`.
