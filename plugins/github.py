from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slacker import Slacker
import random
import requests
import os

slack = Slacker(os.environ['SLACKBOT_API_TOKEN'])
membersDict = {}

@listen_to('[誰|だれ]か.*[やって|お願い|助けて|手伝って].+')
def assign_someone(message):
    global membersDict
    senderId = message.body['user']

    if not membersDict:
        message.reply('すみませんメンバー表ないんで取ってきます', in_thread=True)
        response = slack.users.list()

        for member in filter(lambda member: not member['is_bot'] and member['name'] != 'slackbot', response.body['members']):
            membersDict[member['id']] = member

        message.reply(membersDict[senderId]['name'] + 'さん！すいやせん！取ってきやした！', in_thread=True)

    assigneeId = random.choice(list(filter(lambda member: member != senderId, membersDict.keys())))
    message.send(u'<@{}>{}'.format(membersDict[assigneeId]['name'], 'さん！' 'オナシャス！！！！'))
