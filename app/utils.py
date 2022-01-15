import ast
import datetime
import os
import glob

def average(products):
    prices=[]
    for p in products:
        prices.append(float(p["price"]))
    return sum(prices)/len(prices)
    
# prod=[{"price": "4599", "card": "PNY GeForce RTX 3060 Ti 8GB XLR8 Gaming REVEL EPIC-X RGB Dual Fan (LHR) VCG3060T8LDFXPPB", "link": "https://mediamarkt.pl/komputery-i-tablety/karta-graficzna-pny-geforce-rtx-3060-ti-8gb-xlr8-gaming-revel-epic-x-rgb-dual-fan-lhr-vcg3060t8ldfxppb"},
# {"price": "4600", "card": "PNY GeForce RTX 3060 Ti 8GB XLR8 Gaming REVEL EPIC-X RGB Dual Fan (LHR) VCG3060T8LDFXPPB", "link": "https://mediamarkt.pl/komputery-i-tablety/karta-graficzna-pny-geforce-rtx-3060-ti-8gb-xlr8-gaming-revel-epic-x-rgb-dual-fan-lhr-vcg3060t8ldfxppb"}
# ]
# print(average(prod))
def parse_json(output):
    td=datetime.datetime.now()
    td=td.strftime("%d-%m-%Y")
    output_all = {"results":[], "date":td}
    output_all["results"]+=output
    output_all["average"] = average(output_all["results"])
    #print(output_all["results"])
    return output_all


def format_json(json_file):
    td=datetime.datetime.now()
    td=td.strftime("%d-%m-%Y")
    output = {"results":[], "date":td}

    with open(json_file) as f:
        products=f.readlines()
        for product in products:
            if product != "\n":
                product_j = ast.literal_eval(product)
                output["results"].append(product_j)
    output["average"] = average(output["results"])
    return output

#print(format_json("/Users/lozog/Code/scrapper-graphic-cards/cards.jl"))
def lookup_file(model, shop=None):
    
    td=datetime.datetime.now()
    td=td.strftime("%Y%m%d")
    #print(td)
    if shop:
        path=("%s_%s_%s.json" % (shop, td, model))
        print(path)
    else:
        path=("%s_%s.json" % ( td, model))
    return path
    

def get_model_history(model):
    available_files=glob.glob(f"app/????????_{model}.json")
    model_history={"model": model, "prices": []}
    for a in available_files:
        with open(a) as f:
            f_dict=ast.literal_eval(f.readlines()[0])
            model_history["prices"].append({"date":f_dict["date"], "price": f_dict["average"]})
    return model_history
#print(lookup_file(model="3050"))
