import json;  # Import JSON decoder / encoder library
from difflib import get_close_matches;
data = json.load(open("data.json"));  # JSON data loading


def translate(entry):
    entry = entry.lower();  # Case sensitivity
    if entry in data:
        return data[entry];
    # if user entered "texas" this will check for "Texas" as well.
    elif entry.title() in data:
        return data[entry.title()]
    elif entry.upper() in data: #in case user enters words like USA or NATO
        return data[entry.upper()]
    elif len(get_close_matches(entry, data.keys())) > 0: # Get best match out of a list
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(entry,data.keys())[0]);
        if yn == "Y":
            return data[get_close_matches(entry, data.keys())[0]];
        elif yn == "N":
            return "This word doesn't exist. Please double check it."; # Error handling to avoid Traceback
        else:
            return "We didn't understand your entry.";
    else:
        return "This word doesn't exist. Please double check it."; # Error handling to avoid Traceback

word = input("Enter word: "); # User input

output =translate(word);

# Make the output user friendly 
if type(output) == list:
    for item in output:
        print(item); # Print each item of an output if the output is a list
else:
    print(output); 
