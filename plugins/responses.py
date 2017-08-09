from slackbot.bot import respond_to

@respond_to('.*好きな.*言語.*？.*')
def what(message):
    message.reply('Typescript')

