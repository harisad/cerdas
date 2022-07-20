from flask import Flask
from flask import request
from flask import Response
import requests
import random
import json

TOKEN = "5581992227:AAGKSw0YcIQlIW8Ug6h-ANO90rr7oLYfYcQ"
app = Flask(__name__)
def parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id,txt
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r
def tel_send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://i.postimg.cc/vBtBjRvm/photo-6242397900453818906-y.jpg",
        'caption': "Ya Jelas yang di foto ini"
    }
 
    r = requests.post(url, json=payload)
    return r

def tel_send_poll(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    randnum = random.randint(0,4)
    payload = {
        'chat_id': chat_id,
        "question": "Seberapa peduli kamu terhadap cinta?",
        "options": json.dumps(["10%", "25%", "50%", "75%" , "100%"]),
        "is_anonymous": False,
        "type": "quiz",
        "correct_option_id": randnum
    }
 
    r = requests.post(url, json=payload)
 
    return r

def tel_send_poll2(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    randnum = random.randint(0,4)
    payload = {
        'chat_id': chat_id,
        "question": "Seberapa cuek kamu?",
        "options": json.dumps(["10%", "25%", "50%", "75%" , "100%"]),
        "is_anonymous": False,
        "type": "quiz",
        "correct_option_id": randnum
    }
 
    r = requests.post(url, json=payload)
 
    return r

def tel_send_image2(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://i.postimg.cc/DwY47Ksp/4c9157ef-6d83-4446-a5fe-4b9a85e851bd.jpg",
        'caption': "Ya Jelas yang di foto ini"
    }
 
    r = requests.post(url, json=payload)
    return r

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
       
        chat_id,txt = parse_message(msg)
        if txt == "/help":
            tel_send_message(chat_id,"COMMAND BOT \n Arsyila \n siapa wanita tercantik? \n pasangan terbaik? \n haris nyebelin? \n kamu itu apa? \n /polling \n /cuek \n /gombal")
        if txt == "Siapa namamu?":
            namamu = ["Arsyila" , "Haris"]
            tel_send_message(chat_id,random.choice(namamu))

        if txt == "kamu itu apa?":
            robot = ["Aku bot dibuat Haris" , "Aku manusia sama sepertimu"]
            tel_send_message(chat_id,random.choice(robot))

        if txt == "cila sayang haris?":
            syg = ["sayang bangeeeeeettttttt", "sayang dong masa enggak"]
            tel_send_message(chat_id,random.choice(syg))

        if txt == "haris nyebelin?":
            nyebelin = ["nyebelin banget", "enggak sih", "nyebelin tapi cila sayang"]
            tel_send_message(chat_id,random.choice(nyebelin))

        if txt == "/polling":
            tel_send_poll(chat_id)

        if txt == "/cuek":
            tel_send_poll2(chat_id)

        if txt == "siapa wanita tercantik?":
            tel_send_image(chat_id)
        
        if txt == "pasangan terbaik?":
            tel_send_image2(chat_id)

        if txt == "/gombal":
            gombal = ["Seandainya aku ini gelas, aku pengen deh kamu yang jadi airnya. Soalnya cuma kamu yang bisa mengisi kekosongan hidup aku",
                      "Aku punya kemoceng buat kamu nih. Buat bersihin hati kamu dari nama-nama cowok yang udah nyakitin kamu",
                      "Kamu itu sama seperti kemerdekaan. Sama-sama harus diperjuangkan",
                      "Semenjak lihat kamu aku tuh jadi sakit mata, karena semua yang aku lihat jadi hitam putih. Cuma kamu doang yang berwarna",
                      "Meskipun kamu dari ujung lautan ngelempar senyum, tapi langsung masuk ke hati aku"]

            tel_send_message(chat_id, random.choice(gombal))

        if txt == "Arsyila":
            syila = ["iya apa?","cila cantik","kesayangan haris", "apa si manggil manggil"]
            tel_send_message(chat_id,random.choice(syila))      
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
    app.run()
