import json

Liste = """
{
    "Name": "Schmalo",
    "Next": "Dev",
    "Land": "NRW, Berlin, Land,",
    "Telefon": {
        "Handy": "12345",
        "Festnetz": "678910"
    }
}
"""

Um = json.loads(Liste)

Liste = [Um["Name"], Um["Next"], Um["Land"], Um["Telefon"]]

with open("Liste.json", "w") as Json_data:
    json.dump(Liste, Json_data, indent=4)
