from preprocess import *

def processData(batch : str) -> json:
    dataBatch = loadJson(batch)

    details = getDetails(dataBatch)
    datas = getData(dataBatch)
    
    useless_index = []
    useless_name = []
    
    for (index, items), name in zip(enumerate(datas),details["names"]):
        items = loadJson(items)


        if any(items[name][para] == "NaN" for para in details["item_detail"]):
            useless_name.append(name)
            useless_index.append(index)


    for name in useless_name:
        details["names"].remove(name)

    popMultipleFromList(datas, useless_index)

    return jsonDataBatch(details, datas)
            




if __name__ == "__main__":
    import sys
    sys.path.insert(0, "./../Fetch")
    from fetch import *
    from random import randint
    
    
    dataList = []
    names = []
    item_details = ["first", "second"]
    
    for i in range(0,10):
        name = f"Name{i}"

        names.append(name)
        D = data(name, first = "NaN", second = randint(20,30))
        dataList.append(D)
        
    detail = details(names, item_details)
    datas = dataBatch(detail, dataList)
    print(loadJson(datas))

    result = processData(datas)
    print(result)

