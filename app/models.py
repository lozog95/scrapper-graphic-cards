"""
Definition of models.
"""

from django.db import models
import json
import os
import app.utils as utils

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

def output_lists(model):
    #output_me = json_reader(utils.lookup_file(model=model, shop="me"))
    #output_euro = json_reader(utils.lookup_file(model=model, shop="euro"))
    output_mm = json_reader(utils.lookup_file(model=model, shop="mm"))
    output = []
    # if output_me:
    #     output= output + output_me
    # if output_euro:
    #     output= output + output_euro
    if output_mm:
        output=output+output_mm
    #output.sort(key=lambda x: int(x['price']), reverse=False)
    return utils.parse_json(output)
