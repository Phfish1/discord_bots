import json

def get_token():
    info_file = open("first_bot/info.json")
    json_data = json.load(info_file)

    return json_data["token"]

