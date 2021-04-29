import discord
from discord.ext import commands
from discord.utils import get

class c117(commands.Cog, name="c117"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Neleus_Heavenslayer', aliases=['c117'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Neleus, Heavenslayer',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2328203.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Zombie/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2000/0)', inline=False)
        embed.add_field(name='Monster Effect', value='If you have 3 or more cards in the Extra Deck than your opponent: You can Special Summon this card from your hand. You can pay 1000 LP; look at your opponent\'s Extra Deck and banish all monsters on the field face-down with the same name as any card in your opponent\'s Extra Deck, also, neither player can Special Summon monsters from the Extra Deck for the rest of the turn. If a card is added to your opponent\'s Extra Deck: You can add this card from your GY to your hand. You can only use each effect of "Neleus, Heavenslayer" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c117(bot))