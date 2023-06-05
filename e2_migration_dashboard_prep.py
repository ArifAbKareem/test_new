# Databricks notebook source
pip install gspread

# COMMAND ----------

import gspread

gc = gspread.service_account(filename='/Workspace/Repos/arif.kareem@databricks.com/e2migration_dashboard/fe-dev-sandbox-c5c53185865b.json')

# COMMAND ----------

sh = gc.open("Example spreadsheet")
