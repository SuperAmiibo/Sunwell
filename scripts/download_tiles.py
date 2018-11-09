import json
import os
import requests
import sys


        
def loadCards(cards):
    length = len(cards)
    index = 0
    for card in cards:
        index = index + 1
        id = card["id"];
        if "type" in card.keys():
            if (card['type'] != 'ENCHANTMENT'):
                url = "https://art.hearthstonejson.com/v1/tiles/" + id + ".png"
                root = "./tiles/"
                path = root + "/" + id + ".png"
                            
                img = os.path.exists(path)
                if (img):
                    data = open(path,'rb').read(4)
                    if data[:4] != '\x89\x50\x4e\x47': 
                        try:
                            r = requests.get(url)
                            r.raise_for_status()                
                            with open(path,"wb") as f:
                                f.write(r.content)
                                print("complete: " + id + "(" + str(index) + "/" + str(length) + ")")
                        except requests.exceptions.HTTPError as e:
                            print (e)
                    print("exsit: success " + id)

                else:
                    try:
                        r = requests.get(url)
                        r.raise_for_status()                
                        with open(path,"wb") as f:
                            f.write(r.content)
                            print("complete: " + id + "(" + str(index) + "/" + str(length) + ")")
                    except requests.exceptions.HTTPError as e:
                        print (e)
                
        
def loadJson():
    file = open("./cards.json")
    json_content = json.load(file)
    
    return json_content

def main():
    
    all_cards = loadJson()
    loadCards(all_cards)

if __name__ == "__main__":
	main()
