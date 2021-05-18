import requests
import random
import time

page_id = "page id"
access_token = "access token"

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
