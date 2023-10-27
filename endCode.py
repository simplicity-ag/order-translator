import xmltodict
import json 

liste = """
{"haupt": {"name":"marlon", "next":"dinter", "hobby":"Programmieren", "age":"26"}}"""

num = int(input("Wie moechtest du es convertiert haben 1.json 2.xml: "))

trans = json.loads(liste)

if num == 1:
    print(trans["haupt"]["name"], trans["haupt"]["next"], trans["haupt"]["hobby"], trans["haupt"]["age"])
else:
    xmlTrans = xmltodict.unparse(trans)
    print(xmlTrans)