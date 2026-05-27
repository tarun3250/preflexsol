# Practice question
# Create nested dictionary for:
# user
# skills
# college
# course
# Convert to formatted JSON.

import json

details={"User":"tarun", 
         "skills":{"lang":["pyhton", "java"], 
                                   "frameworks":["flask" ,"spring"],
                                   "IDE":"Vs_code" "pycharm"},
        "College":"MS Ramaiah",
        "course":"MCA"}
print("the keys of dictionary are: ",details.keys())
print("the values of dictionary are: ",details.values())
conv_json=json.dumps(details)
print(conv_json)
print(type(conv_json))

