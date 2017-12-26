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
        get_member_list(message, senderId)

    assigneeId = random.choice(list(filter(lambda member: member != senderId, membersDict.keys())))
    message.send(u'<@{}>{}'.format(membersDict[assigneeId]['name'], 'さん！' 'オナシャス！！！！'))

@listen_to('random assign([1-9]+)?$')
def assign_members(message, number):
    global membersDict
    senderId = message.body['user']
    number_to_pick = min(int(number), len(membersDict)) if number else 2

    reply = ''

    if not membersDict:
        get_member_list(message, senderId)

    candidates = random.sample(list(map(lambda assigneeId: membersDict[assigneeId]['name'], membersDict.keys())), number_to_pick)
    body = '```' + ', '.join(candidates) + '```'
    message.send(body)

def get_member_list(message, senderId):
    message.reply('すみませんメンバー表ないんで取ってきます', in_thread=True)
    response = slack.users.list()

    for member in filter(lambda member: not member['is_bot'] and member['name'] != 'slackbot', response.body['members']):
        membersDict[member['id']] = member

    message.reply(membersDict[senderId]['name'] + 'さん！すいやせん！取ってきやした！', in_thread=True)
