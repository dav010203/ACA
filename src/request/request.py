import requests, json

def fetching(name):
    base = "https://itunes.apple.com/search"
    param = {}
    param["country"] = "AM"
    param["term"] = name
    param['media'] = 'music'

    res = requests.get(base, params=param)
    return res.json()

def get_music_list(js):
    for track in js['results']:
        if track['artistName'] == "Rihanna":
            print("{}".format(track['trackName']))

get_music_list(fetching("Rihanna"))