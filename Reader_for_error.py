Error:
Odoo Server Error

Traceback (most recent call last):
  File "/usr/lib/python3.7/site-packages/odoo/addons/web/controllers/main.py", line 110, in wrap
    return f(*args, **kwargs)
  File "/usr/lib/python3.7/site-packages/odoo/addons/web/controllers/main.py", line 1907, in index
    return self.base(data, token)
  File "/usr/lib/python3.7/site-packages/odoo/addons/web/controllers/main.py", line 1860, in base
    response_data = self.from_data(columns_headers, export_data)
  File "/usr/lib/python3.7/site-packages/odoo/addons/web/controllers/main.py", line 1925, in from_data
    with ExportXlsxWriter(fields, len(rows)) as xlsx_writer:
  File "/usr/lib/python3.7/site-packages/odoo/addons/web/controllers/main.py", line 729, in __init__
    self.workbook = xlsxwriter.Workbook(self.output, {'in_memory': True})
AttributeError: 'NoneType' object has no attribute 'Workbook'