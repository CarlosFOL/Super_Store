from fields import Fields

def max_and_min(func):
    #f = frequency
    def wrapper(field):
        results = func(field)
        max_f = max([value for value in results.values()])
        min_f = min([value for value in results.values()])
        max_field, min_field = [], []
        for key, value in results.items():
            if max_f == value:
                max_field.append(key)
            elif min_f == value:
                min_field.append(key)
        for k in field.keys():
            print(f"""
Most requested {k.replace("_", " ")}: {max_field}, f: {max_f} order(s)
Least requested {k.replace("_", " ")}: {min_field}, f: {min_f} order(s)""")
    return wrapper

def mode(iterable):
    elements = set()
    for v in iterable.values(): 
        for _ in v:
            elements.add(_)
    dic_frequencies = {}
    for e in elements:
        frequency = 0
        for v in iterable.values():
            for _ in v:
                if e == _:
                    frequency += 1
        dic_frequencies[e] = frequency
    return dic_frequencies

@max_and_min
def analysis(data): #data = {"ship_mode": [Standard Class, Same Day,... ]}
    frequency = mode(data)
    return frequency

def extraction(file_name):
    data = {}
    with open(f"./files/{file_name}.txt", "r", encoding="utf-8") as f:
        value = [x.strip("\n") for x in f]
        data [file_name] = value
    return data

if __name__=="__main__":
    field_1 = Fields("ship_mode")
    field_2 = Fields("segment")
    field_3 = Fields("city")
    field_4 = Fields("state")
    analysis(extraction(field_1.name))
    analysis(extraction(field_2.name))
    analysis(extraction(field_3.name))
    analysis(extraction(field_4.name))