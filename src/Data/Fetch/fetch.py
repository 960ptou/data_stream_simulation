import simplejson as json

def details(names : list, item_detail : list) -> str:
    items = {
        "items" : len(item_detail),
        "item_detail" : item_detail,
        "names" : names
    }
    
    return json.dumps(items)


def dataBatch(details : json, datas : list) -> str:
    items = {
        "details" : details,
        "data" : datas
    }
    
    return json.dumps(items)


def data(name : str, **kwargs) -> str:
    items = {
        name : kwargs
    }
    
    return json.dumps(items)



if __name__ == "__main__":
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
    print(json.dumps(datas))

