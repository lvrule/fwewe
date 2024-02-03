from telnetlib import STATUS
import os
import vk_api, random, time, threading, sys, scheduler  
import requests
from bs4 import BeautifulSoup
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import datetime
from datetime import time
from datetime import date
from random import randint
from time import sleep
import pytz
from translate import Translator
import wikipedia



vk_session = vk_api.VkApi(
    token="vk1.a.Onw0i_-FvIyjVoFbDsUd2GCOp3tdi2XmjHg464-rGZo6ix_X4tGMV4P6tcCjuSh1zQ13Wj-A_zDRk80_MR1EYRN-LPoTfckVrUz5ZkDB5hKxrEUnKxiQ-8gnHF_2oHoynBBZLtKL_G-SQvcn1k6VsMdknxOytm2G--oZzC4i59NB5FSEMu4vQnVN4gFJT-_Jcu4f1AhRFkxUYbOUo9W_Tg")
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
def captcha_handler(captcha):
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)

def ping():
    number = list([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5])
    random.shuffle(number)
    ping1 = random.choice(number)
    ping = f'{ping1}{second}' 
    print(ping)

def get_user_status(user_id):
    response = vk.status.get(user_id=user_id)
    status = response['text']
    return status

#gtime = datetime.now()
#curtime = gtime.strftime("%d.%m.%Y, %H:%M:%S")
#timemsk = gtime.strftime("%H:%M:%S")

def get_user_group(user_id):
    response = vk.messages.getConversations(user_id=user_id, count=0)
    countb = response['count']
    countunread = response['unread_count']  
    return countb
    return countunread

def set_user_online(peer_id):
    response = vk.account.setOnline()
    online = response
    online = ("🟢")
    return online

def set_user_offline(peer_id):
    response = vk.account.setOffline()
    offline = response
    offline = ("🟢")
    return offline

def get_group_link(peer_id):
    response = vk.messages.getInviteLink(peer_id=peer_id, reset=0)
    grouplink = response['link']
    return grouplink

def count_messages(peer_id):
    response = vk.messages.getHistory(peer_id=peer_id, count=0)
    count = response['count']
    return count

def get_user_info(user_id):
    user = vk.users.get(user_ids=user_id)[0]
    userinf = f"{user['first_name']} {user['last_name']}"
    return userinf

def wiki_request():
    wikipedia.set_lang("ru")
    object = wikipedia.page(f"{zapros}") 
    originaltitle = object.original_title
    itoog = object.summary[:950]
    return originaltitle
    return itoog

def spam_hate():
    file1 = open("spamtxt.txt", "r", encoding='utf-8')
    text = (random.choice(file1.readlines()))
    vk.messages.send(message_id=event.message_id,peer_id=event.peer_id, message=f"{text}", random_id=0, captcha_handler=captcha_handler)
    time.sleep(1)
    return 

def my_func():
    for _ in range(1000000):
        pass


#st = time.process_time()
#my_func()
#et = time.process_time()

onlineuser = ("❌")
offlineuser = ("❌")

print("🤖БОТ ЗАПУЩЕН✅")

pref = 'аа'  # Префикс команды

command = ""
second = 'сек.'

while True:
    try:
        for event in longpoll.listen():
         if event.type == VkEventType.MESSAGE_NEW:
             words = event.text.lower().split(' ')
             command = words[0]
             message = event.message
             message_list = message.split()                       
             if len(message_list) > 0:
              pref = message_list[0]
             if pref == 'аа':
                if len(words) > 1:
                    try:
                     command = words[1]
                    except:
                        print('pass')
                        continue

                
                if command == "команды":
                    try:
                        vk.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=f"❄️Команды юзер бота\n\n {pref} погода 'запрос' (показывает температуру в указаном городе)\n{pref} вики 'запрос' (статья из википедии)\n{pref} смс (кол-во смс в личке)\n{pref} пинг (показывает пинг бота)\n{pref} цвета (палитра из сердечек)\n{pref} love (валентинка)\n{pref} факт (рандомный интересный факт)\n{pref} линк (ссылка на приглос в беседу)", random_id=0, captcha_handler=captcha_handler)
                    except:
                        time.sleep(2)
                        vk.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=f"Ошибка, команды...", random_id=0, captcha_handler=captcha_handler) 

                if command == "смс":
                    try:
                        total_messages = count_messages(event.peer_id)
                        vk.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=f"Сообщений в диалоге: {total_messages}", random_id=0, reply_to=event.message_id)
                    except:
                        vk.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=f"Ошибка выполнение команды 'количество сообщений'", random_id=0, reply_to=event.message_id)

                if command == "факт":
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"Ищу факты...", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    try:
                        url = "https://randstuff.ru/fact/"
                        response = requests.get(url)
                        bs = BeautifulSoup(response.text,"lxml")
                        temp = bs.findAll('table', 'text')
                        tempfackt = bs.find('td')
                        itogfact = tempfackt.text
                        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💬Факт:\n{itogfact}", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    except:
                        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"Упсс... не нашел факт(", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)

                if command == "пинг":
                    try:
                        vk.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=f"❄️Пинг: {et - st:0.2f}мс.", random_id=0, captcha_handler=captcha_handler)
                    except:
                        time.sleep(2)
                        vk.messages.edit(message_id=event.message_id, peer_id=event.peer_id, message=f"Ошибка, пинг не получен.", random_id=0, captcha_handler=captcha_handler)    
                
                if command == "линк":
                    grouplink = get_group_link(event.peer_id)
                    fromchatlink = event.from_chat
                    try:
                        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"🔗Ссылка на эту беседу: {grouplink}", random_id=0, reply_to=event.message_id)
                    except:
                        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❌Ошибка, нету полномочий...", random_id=0, reply_to=event.message_id)
                    
                if command == "love":
                 try:
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"I", random_id=0, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message="love", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message="you", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message="❤️", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❤️🧡", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❤️🧡💛", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❤️🧡💛💚", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❤️🧡💛💚💙", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❤️🧡💛💚💙💜", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"🧡💛💚💙💜❤️", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1) 
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💛💚💙💜❤️🧡", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1) 
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💚💙💜❤️🧡💛", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1) 
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💙💜❤️🧡💛💚", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1) 
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💜❤️🧡💛💚💙", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)  
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❤️Ты зайка:)", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1) 
                 except:
                    time.sleep(3)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💬Ошибка....", random_id=0, captcha_handler=captcha_handler)
                    continue         
                if command == "цвета":
                 try:                      
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                    time.sleep(1)
                 except:
                    
                    vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💬Ошибка....", random_id=0, captcha_handler=captcha_handler)
                    continue
                 
                if command == "погода":
                    message_list = message.split()                       
                    if len(message_list) > 2:
                        city = message_list[2]
                        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"🕗Обработка...", random_id=0, reply_to=event.message_id)
                        time.sleep(1)
                        api = 'e29fada8e792a55ce8bae5df8383f648'
                        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
                        try:
                            weather_data = requests.get(url).json()
                            temp = weather_data['main']['temp']
                            tempitog = temp - 273.15
                            vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"🌤️Погода в: {city}\n\n🌡️Температура: {tempitog:.2f}", random_id=0, reply_to=event.message_id)
                        except:
                            vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"❌Ошибка, я не нашел такого города... {tempitog}", random_id=0, reply_to=event.message_id)
                
                if command == "вики": 
                    message_list = message.split()  
                    try:
                        result = ''
                        zapros = ''
                        zaprostwo = ''
                        zaprosthree = ''
                        zaprosfour = ''
                        if len(message_list) > 2:   
                            zapros = message_list[2]
                            wikipedia.set_lang("ru")
                            zaprostwo = ''
                        if len(message_list) > 3:   
                            zaprostwo = message_list[3]
                            if zaprostwo == '':
                                zaprosthree == ''
                                continue
                        if len(message_list) > 3:   
                            zaprosthree = message_list[3]
                            if zaprosthree == '':
                                zaprosfour == ''
                                continue  
                        if len(message_list) > 3:   
                            zaprosfour = message_list[3]
                            if zaprosfour == '':
                                continue   
                        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"🕗Обработка...", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                        result = wikipedia.summary(f'{zapros} {zaprostwo} {zaprosthree} {zaprosfour}', sentences=9)
                        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"Завершено!", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                        time.sleep(1)
                        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"{result}", random_id=0, reply_to=event.message_id, captcha_handler=captcha_handler)
                        result = ''
                        zapros = ''
                        zaprostwo = ''
                        zaprosthree = ''
                        zaprosfour = ''
                    except:
                        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💬По запросу: {zapros} {zaprostwo} {zaprosthree} {zaprosfour}\n ❌Ничего не нашлось...", random_id=0, captcha_handler=captcha_handler)
  
                if command == "инфо":
                    ingroup = event.from_chat
                    if ingroup == 'True':
                        mentions = temp['mentions']
                        getfriend = vk.friends.get(user_id=event.user_id, count=0)
                        gettfriend = getfriend['count']
                        userinf = get_user_info(event.user_id)
                        countfollow = vk.users.getFollowers(user_id=event.user_id, count=0)
                        userinff = countfollow['count']
                        statususer = get_user_status(event.peer_id)
                        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"👤Имя пользователя: {userinf} {mentions}\n✉Подписчиков: {userinff}\n🤝Друзей: {gettfriend}\nCтатус: {statususer}\nTrue?{ingroup}", random_id=0, reply_to=event.message_id)
                    else:
                        getfriend = vk.friends.get(user_id=event.user_id, count=0)
                        gettfriend = getfriend['count']
                        userinf = get_user_info(event.user_id)
                        countfollow = vk.users.getFollowers(user_id=event.user_id, count=0)
                        userinff = countfollow['count']
                        statususer = get_user_status(event.peer_id)
                        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"👤Имя пользователя: {userinf}\n✉Подписчиков: {userinff}\n🤝Друзей: {gettfriend}\nCтатус: {statususer}\nFalse?{ingroup}", random_id=0, reply_to=event.message_id)

                if command == "аниме":
                 try:
                    url = "https://serialochka.ru/6241-dosanko-gyaru-chudo-kak-mily.html"
                    urltwo = "https://serialochka.ru/5346-povsednevnaya-zhizn-bessmertnogo-korolya.html"
                    headers = requests.utils.default_headers()

                    headers.update(
                        {
                            'User-Agent': 'My User Agent 1.0',
                        }
                    )
                    response = requests.get(url, headers=headers)
                    responsetwo = requests.get(urltwo, headers=headers)

                    bs = BeautifulSoup(response.text,"lxml")
                    one = bs.find('div', 'waiting')

                    bstwo = BeautifulSoup(responsetwo.text,"lxml")
                    two = bstwo.find('div', 'waiting')
                    today = datetime.datetime.now()
                    bday = datetime.datetime(2024,9,10)
                    bdaytwo = datetime.datetime(2025,1,13)
                    bdaythree = datetime.datetime(2024,4,23)
                    time_diff = bday - today
                    time_difftwo = bdaytwo - today
                    time_diffthree = bdaythree - today
                    current_date = datetime.datetime.now()
                    vk.messages.send(message_id=event.message_id,random_id=0,peer_id=event.peer_id, message=f'======== Инфаааааа! ========\nНа: {current_date}')
                    vk.messages.send(message_id=event.message_id,peer_id=event.peer_id, message=f"Хоримия 3 сезон осталось: {time_diff}\nАнгел по соседству 2 сезон: {time_difftwo}\n	Моя девушка не только милая 2 сезон: {time_diffthree}", random_id=0)
                    vk.messages.send(message_id=event.message_id,peer_id=event.peer_id, message=f"Досанко-гяру чудо как милы: {one.text}\n\n\nПовседневная жизнь бессмертного короля: {two.text}", random_id=0)
                 except:
                    current_date = datetime.datetime.now()
                    vk.messages.send(message_id=event.message_id,random_id=0,peer_id=event.peer_id, message=f'я где то что то поебался проверь сам\n{current_date}')
                     
    except:
        print("код где-то сломался")
        vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"💬Ошибка....", random_id=0, captcha_handler=captcha_handler)
    
 
                    #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
#
#                       message_list = message.split()                       
#                    if len(message_list) > 2:
#                       third_word = message_list[2]
#                       vk.messages.edit(message_id=event.message_id,peer_id=event.peer_id, message=f"третье слово: {third_word}\nЗаписал в перемменую third_word", random_id=0, reply_to=event.message_id)
#   