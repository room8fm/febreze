from slackbot.bot import respond_to

@respond_to('.*好きな.*言語.*？.*')
def what(message):
    message.reply('Typescript')

subjects = []

@respond_to('お題:(.*)')
def add_subject(message, subs):
    global subjects
    subjects += subs.split()

@respond_to('お題候補')
def add_subject(message):
    global subjects
    message.react('ok_woman')
    reply = 'お題は' + subjects.count() + '個あります。\n```' + ', '.join(subjects) + '```'
    message.reply(reply)
