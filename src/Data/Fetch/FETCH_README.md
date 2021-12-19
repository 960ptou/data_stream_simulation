## This is the document for ONLY the fetch portion of the program


```Json
{
    "detail"  : {
        "items" : 9999999,
        "names" : ["A","B","..."],
        "item_detail" : ["D1","D2","Dn"]
    },

    "data" : [
        {
            "A" : {
                "D1" : ???,
                "D2" : ???,
                "Dn" : ???
            }
        },

        {
            "B" : {
                "D1" : ???,
                "D2" : ???,
                "Dn" : ???
            }
        },
        
        ...
        {
            ...
        }
    ]
}
```
- items => Sizes of the data batch
- names => Some representations (unique key) of the data
    - Should be constant in each file
- item_detail => What each data should contain
    - For error checking.