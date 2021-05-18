import requests
import random
import time

page_id = "103806035233700"
access_token = "EAAr9nyC26ggBAFADFCIynFAeBY2pxFdBxHobM2Fv23BvjOZA0SIO4BZCRZBJRypA2xcmshlWkXGaZCMAMwUtOdZBQbXZA6qYRkkt2EsJNRg8aPBm2FHqCSQvZBcryuXGxPfJn4ne4GZBiNLTp7mmN9oAYHRnyjZAFsUlZCCtPFrXg9kJ4xw992vV8BS8CREMQfDXqZAulaXE5bZCNwZDZD"

msg_list = [
    "#SavePalestine",
    "#SaveAqsa",
    "#SaveMuslims",
    "#bangladeshstandswithpalestine",
    "#FreePalestine",
    "#AlAqsaMosque",
    "#IsraeliAttackonAlAqsa",
    "#IsraeliTerrorism",
    "#AlAqsaUnderAttack",
    "#savepalestine",
    "#savethemuslims",
    "#StopTerrorismAgainstMuslims",
    "#AlAqsa",
    "#StopConspiracyAgainstIslam",
    "#stopIsraeliTerrorism",
    "#PalestinianLivesMatter",
    "#PalestineWillBeFree",
]

post_url = "https://graph.facebook.com/{}/feed".format(page_id)

while True:
    time.sleep(2)
    random.shuffle(msg_list)
    message = " ".join(msg_list)
    payload = {"message": message, "access_token": access_token}
    r = requests.post(post_url, data=payload)
    print(r.text)
