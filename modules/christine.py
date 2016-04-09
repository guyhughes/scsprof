from sopel import module
from random import randint 
def getRandom(l):
    return l[randint(0,len(l)-1)]


# TODO: if a user says dummy and list in one line they must be kicked

@module.rule(r".*([Ll]inked\s*[Ll]ist|([Cc]hristine)).*")
def christine(bot, trigger):
    bot.reply(getRandom([
            'Come see me during office hours.',
            'Is that a linked list?',
            'NO dummy nodes!',
            'Go link yourself to your dummy node.',
            'You should ask SCS technical support.',
            'Java is for people who can\'t c.'
            ]))

@module.rule('.*dummy.*')
def dummy(bot, trigger):
    bot.reply(getRandom([
        'How dare you mention dummy nodes?!',
        'Yes if you used a dummy node, you\'re about as dumb as you look.',
        'Circular linked lists should never use dummy nodes. That would be too easy.',
        "Did you say dummy? You better not be talking about dummy nodes." 
    ]))

@module.rule(r".*\W*(ba|c|z|po)sh\W*.*")
def csh(bot, trigger):
    bot.reply(getRandom([
        'csh is the best shell.',
        'Have you tried csh?',
        'I love csh',
        'You know, I learned csh back in 1901 because csh is the best shell.',
        'I did my PhD in prolog. csh is my favourite language though.t'
    ]))
