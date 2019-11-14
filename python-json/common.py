#  working With commonly with the JSON object 
import json


# The process of encoding JSON is usually called serialization.

sample_data="""{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}"""




# y = json.loads(sample_data)

# print(y['glossary']['GlossDiv'])

#  Reading From the File 


with open('test.json' ,'r') as reader:
    # for i in reader:
    with open('test.json' ,'w') as writer:
        json.dump(sample_data, writer)
    #     print(i)


