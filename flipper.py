print("Hello World")
import os
import pandas as pd
file_name = "parameter.xlsx"
sheetname = ["system","seeds"]
data = pd.ExcelFile(file_name)
print(data.sheet_names)
print(data.sheet_names[0])
print("new co0nten")
# text some text and ModuleNot
systemData = data.parse(sheet_name=sheetname[0],skiprows=1)
print(systemData)
print(systemData["parameter"][0])
if 