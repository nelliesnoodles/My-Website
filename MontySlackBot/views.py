

# SLACK_CLIENT_ID, SLACK_CLIENT_SECRET, SLACK_VERIFICATION_TOKEN, SLACK_BOT_USER_TOKEN, EVENT_KEY,

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from slackclient import SlackClient
import json

import logging

logger = logging.getLogger(__name__)




SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings,
'SLACK_BOT_ACCESS_TOKEN', None)
SLACK_BOT_OATH = getattr(settings,
'SLACK_BOT_OAUTH', None)
Client = SlackClient(SLACK_BOT_USER_TOKEN)



def post(request, *callback_args, **callback_kwargs):
    print("post in views active")

    if request.method == 'POST':
        payload = request.body
        json_object = json.loads(payload)
        print('POST REQUEST MADE BY SLACK')
        type_of_post = json_object.get('type')
        #print(json_object)




        # verification challenge
        if type_of_post == 'url_verification':
            challenge = json_object.get("challenge")
            print("THIS IS A URL VERIFICATION")
            return HttpResponse(challenge)


        if type_of_post == 'event_callback':
            print("EVENT RECIEVED.")
            event_message = json_object.get('event')

            # ignore bot's own message
            if event_message.get('subtype') == 'bot_message':
                return HttpResponse('status.HTTP_200_OK')

            # process user's message
            user = event_message.get('user')
            text = event_message.get('text')
            channel = event_message.get('channel')
            token = event_message.get('token')
            bot_text = 'Hi <@{}> :wave:'.format(user)
            if 'hi' in text.lower():

                print("a hello was sent from slack event.")
                python_dict = {
                    'token':token,
                    'channel':channel,
                    'text':bot_text
                    }
                #json_response = json.dumps(python_dict)
                response = Client.api_call("chat.postMessage", channel=channel, text=text)
                print(response)
                #return HttpResponse(json_response)


    return HttpResponse('status.HTTP_200_OK')


def index(request):

    id = str(settings.SLACK_CLIENT_ID)

    return render(request, 'index.html', {'client_id': id})






