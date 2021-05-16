

# SLACK_CLIENT_ID, SLACK_CLIENT_SECRET, SLACK_VERIFICATION_TOKEN, SLACK_BOT_USER_TOKEN, EVENT_KEY,

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from slackclient import SlackClient
import json
import random
import logging

logger = logging.getLogger(__name__)


MONTY_SCRIPT = "/home/NelliesNoodles/nelliesnoodles_mysite/MontySlackBot/test_HolyGrail.txt"
LIFE_OF_BRIAN_SCRIPT = "/home/NelliesNoodles/nelliesnoodles_mysite/MontySlackBot/test_LifeOfBrian.txt"

SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings,
'SLACK_BOT_ACCESS_TOKEN', None)
SLACK_BOT_OATH = getattr(settings,
'SLACK_BOT_OAUTH', None)
Client = SlackClient(SLACK_BOT_USER_TOKEN)


def get_life_of_brian():
    """
    Get lines from test_LifeOfBrian.
    """
    count = 0
    monty_list = ['coconut']
    try:
        with open(LIFE_OF_BRIAN_SCRIPT) as f:
            lines = f.readlines()

            for line in lines:
                count += 1
                #print(line)
                monty_list.append(line)
        random_line = random.randrange(0, count)
        picked_line = monty_list[random_line]
        return picked_line
    except:
        #print(f"file at : {LIFE_OF_BRIAN_SCRIPT} could not be opened.")
        return 'but it has FAAANNNGGsss'


def get_monty_script():
    """
    Get lines from test_HolyGrail.txt, a partial section of the Holy Grail script
    """
    count = 0
    monty_list = ['coconut']
    try:
        with open(MONTY_SCRIPT) as f:
            lines = f.readlines()

            for line in lines:
                count += 1
                #print(line)
                monty_list.append(line)
        random_line = random.randrange(0, count)
        picked_line = monty_list[random_line]
        return picked_line
    except:
        #print(f"file at : {MONTY_SCRIPT} could not be opened.")
        return 'but it has FAAANNNGGsss'

def post(request, *callback_args, **callback_kwargs):
    #print("post in MontySlackBot/views active")

    if request.method == 'POST':
        payload = request.body
        json_object = json.loads(payload)
        #print('POST REQUEST MADE BY SLACK')
        type_of_post = json_object.get('type')





        # verification challenge
        if type_of_post == 'url_verification':
            challenge = json_object.get("challenge")
            #print("THIS IS A URL VERIFICATION")
            return HttpResponse(challenge)


        if type_of_post == 'event_callback':
            #print("EVENT RECIEVED.")
            event_message = json_object.get('event')

            # ignore bot's own message
            if event_message.get('subtype') == 'bot_message':
                return HttpResponse('status.HTTP_200_OK')

            # process user's message
            user = event_message.get('user')
            text = event_message.get('text')
            channel = event_message.get('channel')
            token = event_message.get('token')
            bot_text = 'Here is your Monty Python Movie script line!  :wave:   '
            grail_line = get_monty_script()
            life_line = get_life_of_brian()

            if 'holy' and 'grail' in text.lower():
                bot_text = bot_text + "\n" + grail_line
                #print(bot_text)

                #print("a hello was sent from slack event.")
                #python_dict = {
                    #'token':token,
                    #'channel':channel,
                    #'text':bot_text
                   # }
                #json_response = json.dumps(python_dict)
                response = Client.api_call("chat.postMessage", channel=channel, text=bot_text)
                #print(response)
                #return HttpResponse(json_response)
            elif 'life' and 'brian' in text.lower():
                bot_text = bot_text + "\n" + life_line
                #print(bot_text)
                response = Client.api_call("chat.postMessage", channel=channel, text=bot_text)


    return HttpResponse('status.HTTP_200_OK')






def index(request):

    id = str(settings.SLACK_CLIENT_ID)

    return render(request, 'index.html', {'client_id': id})






