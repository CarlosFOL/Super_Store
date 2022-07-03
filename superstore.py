#Varios analísis

def max_and_min(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        max_freq = max([value for value in results.values()])
        min_freq = min([value for value in results.values()])
        for key, value in results.items():
            if max_freq == value:
                print(f"Max: {key} with: {max_freq}")
            elif min_freq == value:
                print(f"Min:{key} with: {min_freq}")
    return wrapper


def mode(iterable):
    elements = set(iterable)
    dic_frequencies = {}
    for i in elements:
        frequency = 0
        for _ in iterable:
            if i == _:
                frequency += 1
        dic_frequencies[i] = frequency
    return dic_frequencies

@max_and_min
def analysis(data):
    frequency = mode(data)
    return frequency

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
    analysis(segment)
    analysis(city)
    analysis(state)

if __name__=="__main__":
    run()