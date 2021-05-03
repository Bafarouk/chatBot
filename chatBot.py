from chatterbot import ChatBot
from flask import Flask, request
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask('__name__')
bot = ChatBot('chatterbot', storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')


# routes
@app.route('/')
def home():
    return str('Welcome Home')


@app.route('/user', methods=['POST'])
def user():
    jsony = request.json  # transform response to json
    data = jsony['msg']  # extract the data
    return str(bot.get_response(data))


app.run()
