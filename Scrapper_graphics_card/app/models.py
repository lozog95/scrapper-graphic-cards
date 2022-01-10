"""
Definition of models.
"""

from django.db import models
import json
import os


#json reader model to read output json files
def json_reader(json_path):
    with open(f"app/{json_path}") as w:
        try:
            output = json.loads(w.read())
        except Exception as e:
            output = None
    
    return output

def clean_json_files():
    if os.path.exists("app/euro_output.json"):
        os.remove("app/euro_output.json")
    if os.path.exists("app/me_output.json"):
        os.remove("app/me_output.json")
    if os.path.exists("app/mm_output.json"):
        os.remove("app/mm_output.json")

def output_lists():
    output_me = json_reader('me_output.json')
    output_euro = json_reader('euro_output.json')
    output_mm = json_reader('mm_output.json')
    output = []
    if output_me:
        output= output + output_me
    if output_euro:
        output= output + output_euro
    if output_mm:
        output = output + output_mm
    output.sort(key=lambda x: int(x['price']), reverse=False)
    return output
