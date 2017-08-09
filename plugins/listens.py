from slackbot.bot import listen_to

@listen_to('.*言語.*')
def language_ts(message):
    message.send('一番いい言語…Typescriptに決まってるだろ？')

@listen_to('.*型.*')
def type_ts(message):
    message.reply('Typescriptなら型安全が手に入るんだぜ')
