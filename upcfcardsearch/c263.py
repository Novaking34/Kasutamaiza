import discord
from discord.ext import commands
from discord.utils import get

class c263(commands.Cog, name="c263"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Choixier_Calling', aliases=['c263', 'Choixier_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Choixier Calling',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360645.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Choixier)', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Activate 1 of the following effects;\n● Special Summon 1 "Raven Token" (Winged-Beast/EARTH/Level 2/ATK 1000/DEF 1000).\n● If your opponent controls more monsters than you do: Special Summon "Raven Tokens" (Winged-Beast/EARTH/Level 2/ATK 1000/DEF 1000) up to the difference.\nYou can only activate each effect of "Choixier Calling" once per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c263(bot))