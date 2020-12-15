# importing the module
import json

# Opening JSON file
with open('data.json') as json_file:
    data = json.load(json_file) #data is a dictionary

data = { "whisper" : [ "subrand": ]

                           ,
        "gillette":[
              {"sub_brand" : "" ,
               "sku"}]
                  }


for brand,branddetailslist in data.items():
    if(brand == 'gillette'):
        branddetailslist
