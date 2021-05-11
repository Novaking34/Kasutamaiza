import discord
from discord.ext import commands
from discord.utils import get

class c282(commands.Cog, name="c282"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Multipurpose_Pendulumgear', aliases=['c282', 'Gear_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Multipurpose Pendulumgear',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361022.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Gear)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Tuner/Pendulum/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF) [Pendulum Scales]', value='6 (500/500) [4/4]', inline=False)
        embed.add_field(name='Pendulum Effect', value='You can Fusion Summon 1 Pendulum Fusion monster from your Extra Deck using this card in the Pendulum Zone, and monsters from your hand or field as material, also, you cannot Special Summon monsters from the Extra Deck this turn, except Pendulum or Link monsters. You can only use this effect of "Multipurpose Pendulumgear" once per turn.', inline=False)
        embed.add_field(name='Monster Effect', value='You cannot Special Summon monsters from the Extra Deck the turn you Special Summon this card, except Pendulum or Link monsters. Cannot be used as Link Material. If this card is Normal or Pendulum Summoned: You can target 1 Pendulum monster you control; it becomes Level 6, but it cannot be used as Synchro Material. If this card is in your hand: You can target 1 Pendulum monster you control; Special Summon this card, and if you do, this card\'s Level is reduced by the Level of the targeted monster. You can only use each effect of "Multipurpose Pendulumgear" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c282(bot))