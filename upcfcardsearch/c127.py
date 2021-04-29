import discord
from discord.ext import commands
from discord.utils import get

class c127(commands.Cog, name="c127"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Automaton_the_Ultimate', aliases=['c127','Automaton_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Automaton the Ultimate',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334886.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Automaton)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card is Normal Summoned while you control "Right Arm of Automaton", "Left Arm of Automaton", "Right Leg of Automaton". and "Left Leg of Automaton", this card ATK/DEF becomes 5000 and it cannot be Tributed, also this card is unaffected by your opponent\'s card effects. If this card would would be sent to the GY, you can banish 1 "Automaton" Normal Monster you control or in your GY instead. If this card leaves the field, you lose the Duel.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c127(bot))