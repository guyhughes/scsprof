import sopel.module

@sopel.module.commands('helloworld')
def helloworld(bot,trigger):
	bot.say('hello world')
