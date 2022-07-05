

def report():
    def wrapper():
        pass
    return wrapper

def mode(iterable):
    elements = set()
    for _ in iterable:   
        elements.add(_)
    dic_frequencies = {}
    for e in elements:
        frequency = 0
        for _ in iterable:
            if e == _:
                frequency += 1
        dic_frequencies[e] = frequency
    return dic_frequencies

def check_claims(data_base):
    #Who are the claimers? In which city/state/region there more claims? Here we check it.
    #On id_claim.txt are all orders_id that were returned by a claim.
    order_id = []
    claimers, city = [], []
    state, region = [], []
    with open("./../files/id_claim.txt", "r", encoding="utf-8") as f:
        for i in f:
            order_id.append(i.strip("\n"))
    for dict in data_base:
        for _ in order_id:
            if dict["id"] == _:
                claimers.append(dict["name"]), city.append(dict["city"])
                state.append(dict["state"]), region.append(dict["region"])
    return mode(claimers), mode(city), mode(state), mode(region)    

def structure(data_wo_structure):  #wo = without
    #We save all data in a dictionary (database), but first you need to remove ",".
    #Then you save the customer's feature depending the field.
    fields = [
        "id","name", "city",
        "state", "region"
    ]
    data_base = []
    value = []
    for element in data_wo_structure: 
        counter = 0
        dic = {}
        for character in element:
            if character != ",":
                 value.append(character)
            else:
                dic[fields[counter]] = "".join(value)
                counter += 1
                value.clear()
        data_base.append(dic)
    return data_base

def cleaning(data):
    #There are many empty spaces in the data. So you need to remove them.
    for element in data:
        if element == "":
            data.remove(element)
    return data

def extraction():
    #Extract unstructured data of the customers's features.
    #Such as: name, id, city, region, state, region.
    with open("./../files/customers.txt", "r", encoding="utf-8") as f:
        data = [d.strip("\n") for d in f]
    return data

def run():
    #Build a data base for your respective analysis.
    data_base = structure(cleaning(extraction()))
    results = check_claims(data_base)
    print(results)

if __name__=="__main__":
    run()