from statistics import mean, mode, multimode
#Varios analísis

def mode_func(iterable):
    elements = set(iterable)
    dic = {}
    for i in elements:
        frequency = 0
        for _ in iterable:
            if i == _:
                frequency += 1
        dic[i] = frequency
    return dic

def analysis(data):
    frequency = mode_func(data)
    print(frequency)

def extraction(file_name):
    with open(f"./files/{file_name}.txt", "r", encoding="utf-8") as f:
        data = [x.strip("\n") for x in f]
    return data

def run():
    ship_mode = extraction("ship_mode")
    segment = extraction("segment")
    city = extraction("city")
    state = extraction("state")
    analysis(ship_mode)

if __name__=="__main__":
    run()