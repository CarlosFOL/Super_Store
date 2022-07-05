
def report(func):
    """Put my results in a report"""
    def wrapper(*args):
        print("""
-------------------
COMPLAINT REPORT
-------------------""")
        for elements in func(*args):
            for key, value in elements.items():
                print(f"""

FIELD: {key}

More complaints => {value[0]}, Q: {value[1]} complaint(s)

Less complaints => {value[2]}, Q: {value[3]} complaint(s)
""")
    return wrapper

def max_min(dictionary, letter):
    """Calculate the max frequency and the min frequency to find 
    the one who claims the most and the one who does the least."""
    field = {
        "c": "CLAIMERS", 
        "i": "CITY",
        "s": "STATE", 
        "r": "REGION"
    }
    results = {}
    max_value = max([v for v in dictionary.values()])
    min_value = min([v for v in dictionary.values()])
    max_field, min_field = [], []
    for key, value in dictionary.items():
        if value == max_value:
            max_field.append(key)
        elif value == min_value:
            min_field.append(key)
    for k, v in field.items():
        if letter == k:
            results[v] = [max_field, max_value, min_field, min_value]
    return results

@report
def results(data):
    """Here are the final results of my analysis"""
    claimers, city = max_min(data[0], "c"), max_min(data[1], "i")
    state, region = max_min(data[2], "s"), max_min(data[3], "r")
    return claimers, city, state, region 
    
def mode(iterable):
    """Calculate the frequency of the items in the list"""
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

def check_complaints(data_base):
    """Who are the claimers? In which city/state/region there more complaints? Here we check it.
    On id_claim.txt are all orders_id that were returned by a claim."""
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
    """We save all data in a dictionary (database), but first you need to remove ",".
    Then you save the customer's feature depending the field"""
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
    """There are many empty spaces in the data. So you need to remove them."""
    for element in data:
        if element == "":
            data.remove(element)
    return data

def extraction():
    """Extract unstructured data of the customers's features.
    Such as: name, id, city, region, state, region."""
    with open("./../files/customers.txt", "r", encoding="utf-8") as f:
        data = [d.strip("\n") for d in f]
    return data

def run():
    """Build a data base for your respective analysis."""
    data_base = structure(cleaning(extraction()))
    results(check_complaints(data_base))

if __name__=="__main__":
    run()