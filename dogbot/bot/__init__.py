from dogbot.cqsdk import CQBot, RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage
from mongoengine import connect

# connect('aigis')

bot = CQBot(11235, 12450)

# bark!
from dogbot.bot.listeners.bark import bark
bot.add_listener(bark, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))

# helper
from dogbot.bot.listeners.helper import alias_command, unalias_command, alias_parser, help
bot.add_listener(alias_parser, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))
bot.add_listener(help, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))
bot.add_listener(unalias_command, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))
bot.add_listener(alias_command, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))

# roll
from dogbot.bot.listeners.roll import roll
bot.add_listener(roll, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))

# 喂桶
from dogbot.bot.listeners.bucket import bucket
bot.add_listener(bucket, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))

# 素材
from dogbot.bot.listeners.material import material
bot.add_listener(material, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))

# 计算器
from dogbot.bot.listeners.calc import calc
bot.add_listener(calc, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))

# 属性图与圆爹图
from dogbot.bot.listeners.unit import status, conne
bot.add_listener(status, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))
bot.add_listener(conne, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))

# emoji
from dogbot.bot.listeners.emoji import emoji_base, emoji_del, emoji_alias, emoji_parser
bot.add_listener(emoji_parser, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))
bot.add_listener(emoji_alias, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))
bot.add_listener(emoji_del, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))
bot.add_listener(emoji_base, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))

# 海报
from dogbot.bot.listeners.poster import poster
bot.add_listener(poster, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))

# twitter
from dogbot.bot.listeners.twitter import twitter
bot.add_listener(twitter, (RcvdDiscussMessage, RcvdGroupMessage, RcvdPrivateMessage))

# twitter定时任务
from dogbot.bot.twitter import poll_twitter
bot.scheduler.add_job(poll_twitter, 'interval', args=(bot, ), seconds=30, max_instances=10)
