"""
Definition of models.
"""

from django.db import models
import json
import os

#json reader model to read output json files
def json_reader():
    with open("app/euro_output.json") as w:
        try:
            output = json.loads(w.read())
            output.sort(key=lambda x: x['price'], reverse=False)
        except Exception as e:
            output = None
    
    return output

def clean_json_files():
    if os.path.exists("app/euro_output.json"):
        os.remove("app/euro_output.json")

