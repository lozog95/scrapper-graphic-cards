"""
Definition of models.
"""

from django.db import models
import json
import os
import app.utils as utils
from datetime import datetime

#json reader model to read output json files
def json_reader(json_path):
    with open(f"app/{json_path}") as w:
        try:
            output = json.loads(w.read())
        except Exception as e:
            output = None
    
    return output

def clean_json_files(model):
    td=datetime.now()
    td=td.strftime("%Y%m%d")
    
    if os.path.exists(f"app/{td}_{model}.json"):
        print("Main file exists")
        os.remove(f"app/{td}_{model}.json")
    if os.path.exists(f"app/me_{td}_{model}.json"):
        print("Me file exists")
        os.remove(f"app/me_{td}_{model}.json")
    if os.path.exists(f"app/euro_{td}_{model}.json"):
        print("euro file exists")
        os.remove(f"app/euro_{td}_{model}.json")
    if os.path.exists(f"app/mm_{td}_{model}.json"):
        print("Mm file exists")
        os.remove(f"app/mm_{td}_{model}.json")

def output_lists(model):
    output_euro = json_reader(utils.lookup_file(model=model, shop="euro"))
    output_me = json_reader(utils.lookup_file(model=model, shop="me"))
    output_mm = json_reader(utils.lookup_file(model=model, shop="mm"))
    output = []
    if output_me:
        output= output + output_me
    if output_euro:
        output= output + output_euro
    if output_mm:
        output=output+output_mm
    
    output.sort(key=lambda x: int(x['price']), reverse=False)
    print(output)
    output_all = utils.parse_json(output)
    td=datetime.now()
    td=td.strftime("%Y%m%d")
    with open(f"app/{td}_{model}.json", "w") as f:
        f.write(json.dumps(output_all))
        f.close()
    
    return output_all

def advise_checker(profitability):
    advise = None
    if float(profitability) < 0.5:
        advise = "Cena jest przynajmniej połowę wyższa niż zazwyczaj, nie kupuj obecnie karty"
    elif float(profitability) < 0.7:
        advise = "Cena jest znacznie wyższa niż wcześniej, wstrzymaj się z zakupem"
    elif float(profitability) < 0.9:
        advise = "Cena jest wyższa niż wcześniej, wstrzymaj się z zakupem"
        print(advise)
    elif float(profitability) < 1:
        advise = "Cena jest nieznacznie wyższa niż wcześniej, jeśli możesz wstrzymaj się z zakupem aż spadnie"
        print(advise)
    elif float(profitability) < 1.1:
        advise = "Cena jest niższa niż zazwyczaj, to może być dobra okazja"
    elif float(profitability) < 1.2:
        advise = "Cena jest znacząco niższa niż zazwyczaj, to może być dobra okazja"
    elif float(profitability) < 1.3:
        advise = "Cena jest niska, to dobry czas na kupno karty"
    elif float(profitability) > 1.3:
        advise = "Cena jest bardzo mała, kupuj teraz"
    return advise