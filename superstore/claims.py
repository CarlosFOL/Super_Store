
def check_claims(data_base):
    claimers = []
    order_id = []
    with open("./../files/id_claim.txt", "r", encoding="utf-8") as f:
        for i in f:
            order_id.append(i.strip("\n"))
    for dict in data_base:
        for _ in order_id:
            if dict["id"] == _:
                claimers.append(dict["name"])
    print(len(claimers))

def structure(data_wo_structure):  #wo = without
    fields = [
        "id","name", "city",
        "state", "region"
    ]
    data_base = []
    value = []
    for element in data_wo_structure: # element = CA-2016-152156,Claire Gute,Henderson,Kentucky,South,
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
    for element in data:
        if element == "":
            data.remove(element)
    return data

def extraction():
    with open("./../files/customers.txt", "r", encoding="utf-8") as f:
        data = [d.strip("\n") for d in f]
    return data

def run():
    data_base = structure(cleaning(extraction()))
    check_claims(data_base)

if __name__=="__main__":
    run()