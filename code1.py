import xmltodict
import json

json_data = """
	{"Haupt": {"Name":"Test", "age":"26"}}
"""
liste = json.loads(json_data)
xmlTrans = xmltodict.unparse(liste)
print(xmlTrans)