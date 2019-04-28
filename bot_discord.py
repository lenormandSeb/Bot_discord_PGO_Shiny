from chromatique import Chromatique
import discord
from discord.ext.commands import Bot

chromatique = Chromatique()
bot = Bot(command_prefix="!")
bot.remove_command('help')

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

@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    async for use in reaction.users():
        if reaction.emoji == '👍':
            await channel.send('Ravi de t\'aider {0}, merci pour ton {1}'.format(user.name, reaction.emoji))

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(content='Hey {0}, désolé je n\'ai pas compris ta demande'.format(ctx.message.author.name))

bot.run('NTcxMDQ3MTE2NDA4MDk0NzMw.XMIZGA.uiYYWBCLq94u66YdVLIu4FMbM4I')
