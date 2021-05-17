import discord
from discord.ext import commands
from discord.utils import get

class c317(commands.Cog, name="c317"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Alice_Master_of_Luck', aliases=['c317'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Alice, Master of Luck',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2367734.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Link/Effect (LIGHT)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='5 (3000/⬅️↙️⬇️↘️➡️)', inline=False)
        embed.add_field(name='Monster Effect', value='3+ Effect Monsters\nMust be Link Summoned. Once per turn, you can Tribute 1 monster this card points to; excavate the top 5 cards of your Deck, and if you do, equip 3 of them to this card. Place the remaining cards on the bottom of your Deck. Once per turn, if this card would be destroyed, you can send 1 card equipped to this monster to the GY instead. This card gains the following effects based on the card types equipped to it. ●Monster: Unaffected by other monster effects, and gains ATK equal to the combined original ATKs of monsters equipped to this card. ●Spell: Unaffected by Spells. Once per turn: You can activate the effect of 1 Normal Spell equipped to this card, and if you do, banish that card after that effect resolves. ●Trap: Unaffected by Traps. (Quick Effect): You can activate the effect of 1 Normal Trap equipped to this card, and if you do, banish that card after that effect resolves.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c317(bot))