from slackbot.bot import respond_to
from slackbot.bot import listen_to
import requests
import os

TOKEN = os.environ('SLACKBOT_API_TOKEN')

@listen_to('誰かに[やって|お願い].+')
def assign_someone(message):
    response = requests.get('https://slack.com/api/users.list', params={'token': TOKEN})
    members = [item.name for item in response.members]
    print(members)
