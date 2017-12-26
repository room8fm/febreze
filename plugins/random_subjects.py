from slack_pinned_storage import SlackPinnedStorage
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from datetime import datetime

import os
import random

token = os.environ['SLACKAPP_API_TOKEN']
identifier = 'febrezeSubjects'
channel = '#room_febreze'

sps = SlackPinnedStorage(token, identifier, channel)

subjects = sps.get() or {}
pick_candidates = []

@listen_to('お題:(.*)')
def add_subjects(message, words):
    global subjects

    not_registered = []
    registered = []
    user_id = message.body['user']

    for word in words.split():
        if (word in subjects):
            not_registered.append(word)
        else:
            subjects[word] = {'user_id': user_id, 'registered_at': datetime.now()}
            registered.append(word)

    reply = ''
    if (registered):
        reply += 'お題、承り！！！\n```' + ', '.join(registered) + '```'
        sps.set(subjects)
    if (registered and not_registered):
        reply += '\n'
    if (not_registered):
        reply += '↓登録済み\n```' + ', '.join(not_registered) + '```'

    message.react('ok_woman')
    message.reply(reply)

@listen_to('お題([0-9]+)?$')
def pick_subjects(message, number):
    global pick_candidates
    global subjects
    number_to_pick = min(int(number), len(subjects)) if number else min(len(subjects), 3)

    reply = ''

    if subjects:
        if not pick_candidates:
            pick_candidates = random.sample(subjects.keys(), number_to_pick)
            reply = str(number_to_pick) + '個選出したよ\n```' + ', '.join(pick_candidates) + '```'
        else:
            reply = '選出済みだよ\n```' + ', '.join(pick_candidates) + '```'
    else:
        reply = 'お題がないよー\n```@febreze お題: ```\nで、お題を追加してね'

    message.reply(reply)

@listen_to('お題候補')
def show_subjects(message):
    global subjects
    message.react('ok_woman')

    count = len(subjects)
    reply = 'お題はないよー'

    if (count > 1):
        reply = 'お題は' + str(len(subjects)) + '個あります。\n```' + ', '.join(subjects) + '```'
    message.reply(reply)

@listen_to('お題リセット$')
def reset_subjects(message):
    global pick_candidates
    pick_candidates = []
    message.react('ok_woman')
    message.reply('リセッシュ！')
