import discord
from discord.ext import commands
from discord.utils import get

class c238(commands.Cog, name="c238"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Gladio', aliases=['c238', 'Magia_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Gladio',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359255.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2100/1900)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card battles a Defense Position monster, it gains 500 ATK/DEF during Damage Calculation only. You can only use each of the following effects of "Magia Gladio" once per turn. If a card(s) you control is destroyed: You can shuffle 3 "Magia" cards from your GY into the Deck; Special Summon this card from your hand. If this card is Normal or Special Summoned: You can Special Summon 1 "Magia" monster from your GY in Defense Position.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c238(bot))