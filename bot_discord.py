from chromatique import Chromatique
import discord
import json
import os
import pymysql
from discord.ext.commands import Bot

access_token = os.environ['ACCESS_TOKEN']

connection = pymysql.connect(host='localhost',
                             user='',
                             password='',
                             db='')

cursor = connection.cursor()

chromatique = Chromatique()
bot = Bot(command_prefix="!")
bot.remove_command('help')
os.chdir('/')

""" @bot.event
async def on_ready()
 """
@bot.event
async def on_member_join(member):
    #find user exist
    find_user = "SELECT * FROM users where pseudo_id = '%s'" % (member.guild.id)
    cursor.execute(find_user)
    count = cursor.rowcount
    if count == 0:
        print('create user')
        sql = "INSERT INTO users (pseudo, pseudo_id) VALUES ('%s', '%s')" % (member.guild.name, member.guild.id)
        try :
            cursor.execute(sql)
            connection.commit()
        except:
            connection.rollback()
    connection.close()

@bot.command()
async def chroma(ctx, arg):
    c = chromatique.get_chroma(arg)
    pokemon = discord.Embed(
        title = 'Voici {0} chromatique'.format(arg),
        colour = 255
    )
    pokemon.set_image(url='https://www.serebii.net/Shiny/SM/{0}.png'.format(c.get('numero')))
    pokemon.set_thumbnail(url='https://www.serebii.net/sunmoon/pokemon/{0}.png'.format(c.get('numero')))
    await ctx.send(content='hey',embed=pokemon)


@bot.command()
async def get_all_shiny(ctx):
    author_name = ctx.message.author.name
    embed = discord.Embed(
        colour = 34
    )
    embed.add_field(name='1er Génération', value=chromatique.get_gen(1), inline=False)
    embed.add_field(name='2eme Génération', value=chromatique.get_gen(2), inline=False)
    embed.add_field(name='3eme Génération', value=chromatique.get_gen(3), inline=False)
    embed.add_field(name='4eme Génération', value=chromatique.get_gen(4), inline=False)
    await ctx.send(content='Hey {0} : Voici la liste des chromatiques disponible dans Pokemon GO'.format(author_name),embed = embed)

@bot.command()
async def get_shiny(ctx, arg):
    author_name = ctx.message.author.name
    embed = discord.Embed(
        colour = 34
    )
    if int(arg) == 1:
        content = 'ere'
    else:
        content = 'ème'
    embed.add_field(name='Les chromatiques de la {0}{1} Génération'.format(arg,content), value=chromatique.get_gen(arg), inline=False)
    msg = await ctx.send(content='Hey {0} : Voici la liste des chromatiques disponible dans Pokemon GO'.format(author_name),embed = embed)
    await msg.add_reaction('\U0001F44D')

@bot.command()
async def set_shiny(ctx, param):
    #find user
    find_user = "SELECT * FROM users WHERE pseudo_id = '%s'" % (ctx.message.author.id)
    cursor.execute(find_user)
    count = cursor.rowcount
    if count == 0:
        sql = "INSERT INTO users (pseudo, pseudo_id, lvl, experience) VALUES ('%s', '%s', '%d', '%d')" % (ctx.message.author.name, ctx.message.author.id, 0, 0)
        try :
            cursor.execute(sql)
            connection.commit()
        except:
            connection.rollback()
    else:
        cursor.execute(find_user)
        user = cursor.fetchall()
        for row in user:
            userid = row[0]
            userpseudo = row[1]
            useridpseudo = row[2]
            userlvl = row[3]
            userexp = row[4]
        print("id= %s, pseudo= %s, idpseudo= %s, lvl= %s, exp= %s" % (userid, userpseudo, useridpseudo, userlvl, userexp))

    addChroma = discord.Embed(
        title = 'J\'ai bien ajouté tes chromatique {0}'.format(ctx.message.author.name),
        color = discord.Color.green()
    )
    await ctx.send(embed=addChroma)

@bot.command(pass_context=True)
async def help(ctx):
    helpcommand = discord.Embed(
        title = 'Voici les commande pour le bot',
        color = discord.Color.orange(),
    )
    helpcommand.add_field(name='!chroma nom_du_pokemon', value='Cherche la version chromatique du pokemon', inline=True)
    helpcommand.add_field(name='!get_all_shiny', value='Retourne la liste des chromatiques disponible dans le jeu Pokemon Go', inline=True)
    helpcommand.add_field(name='!get_shiny choix_de_la_génération', value='Retourne la liste des chromatiques de la génération choisi disponible dans le jeu Pokemon Go', inline=True)
    helpcommand.add_field(name='!help', value='Retourne cette aide', inline=True)
    helpcommand.set_author(name='Help')
    message = await ctx.send(content='{0}'.format(ctx.message.author), embed=helpcommand)
    await message.add_reaction('👍')

async def update_data(users, user):
    if not str(user) in users:
        users[user]= {}
        users[user]['experience'] = 0
        users[user]['lvl'] = 1
        users[user]['chromatique'] = []

async def add_chromatique(users, user, param):
    count = 0
    for pokemon in param.split(','):
        if not pokemon.strip() in users[str(user)]['chromatique']:
            count += 1
            users[str(user)]['chromatique'].append(pokemon.strip())
    users[str(user)]['experience'] += count

async def lvl_up(ctx, users, user, channel):
    experience = users[user]['experience']
    lvl_start = users[user]['lvl']
    lvl_end = int(experience ** (1/2))
    if int(lvl_start) < lvl_end:
        await channel.send(content='{0} as gagné un niveau, tu es maintenant lvl {1}'.format(ctx.author.name, lvl_end))
        users[user]['lvl'] = lvl_end

@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    async for use in reaction.users():
        if reaction.emoji == '👍':
            await channel.send('Ravi de t\'aider {0}, merci pour ton {1}'.format(user.name, reaction.emoji))

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(content='Hey {0}, désolé je n\'ai pas compris ta demande'.format(ctx.message.author.name))

bot.run(access_token)
