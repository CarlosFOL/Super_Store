from typing import List, Dict

def data_base(data_wo_structure:List[str]) -> List[Dict[str:str]]:  #wo = without
    fields:List[str] = [
        "id","name", "city",
        "state", "region"
    ]
    db = []
    dic = {}
    value = []
    for element in data_wo_structure:
        counter = 0
        for character in element:
            if character != ",":
                value.append(character)
            else:
                dic[fields[counter]] = "".join(value)
                value.clear()
                counter += 1
        db.append(dic)
    return db

def cleaning(data:List[str]) -> List[str]:
    for element in data:
        if element == "":
            data.remove(element)
    return data

def extraction() -> List[str]:
    with open("./../files/customers.txt", "r", encoding="utf-8") as f:
        data:List[str] = [d.strip("\n") for d in f]
    return data

def run():
    data_base(cleaning(extraction()))
    
if __name__=="__main__":
    run()