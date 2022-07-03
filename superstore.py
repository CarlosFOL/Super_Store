#from statistics import mean, mode, multimode
#Varios analísis

def extraction(file_name):
    with open(f"./files/{file_name}.txt", "r", encoding="utf-8") as f:
        generator = (x.strip("\n") for x in f)
    return generator

def run():
    ship_mode = extraction("ship_mode")
    for i in ship_mode:
        print(i)


if __name__=="__main__":
    run()