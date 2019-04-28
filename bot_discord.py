from chromatique import Chromatique
import discord
from discord.ext.commands import Bot

chromatique = Chromatique()

bot = Bot(command_prefix="!")

@bot.command()
async def test(ctx):
    print(ctx.guild)
    print(ctx.message)
    print(ctx.author)
    await ctx.send('hey {0} : voici ton message {1}'.format(ctx.author, ctx.message.content))

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


bot.run('NTcxMDQ3MTE2NDA4MDk0NzMw.XMIZGA.uiYYWBCLq94u66YdVLIu4FMbM4I')
