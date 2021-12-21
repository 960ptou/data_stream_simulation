import simplejson as json

def loadJson(batch : str) -> json:
    return json.loads(batch)


def getDetails(batch : json) -> json:
    return json.loads(batch["details"])


def getData(batch : json) -> list:
    return batch["data"]


def jsonDataBatch(details : json, datas : list) -> str:
    items = {
        "details" : details,
        "data" : datas
    }

    return loadJson(json.dumps(items))

def popMultipleFromList(lst : list, indexes : list) -> list:
    #https://stackoverflow.com/questions/11303225/how-to-remove-multiple-indexes-from-a-list-at-the-same-time/41079803
    for index in sorted(indexes, reverse=True):
        del lst[index]

    return lst



if __name__ == "__main__":
    import sys
    sys.path.insert(0, "./../Fetch")
    from fetch import *
    from random import randint
    
    
    dataList = []
    names = []
    item_details = ["first", "second"]
    
    for i in range(0,1):
        name = f"Name{i}"

        names.append(name)
        D = data(name, first = randint(1,10), second = randint(20,30))
        dataList.append(D)
        
    detail = details(names, item_details)
    datas = dataBatch(detail, dataList)
    datas = json.loads(datas)

    print(getDetails(datas))
    print(getData(datas))
    
