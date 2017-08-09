from slackbot.bot import Bot

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()

@respond_to('好きな言語は？')
def what(message):
    message.reply('Typescript')

@listen_to('.*言語.*')
def langage_ts(message):
    message.send('Typescriptが一番いいに決まってるだろ')

@listen_to('.*型.*')
def type_ts(message):
    message.send('Typescriptなら型安全が手に入るんだぜ')
