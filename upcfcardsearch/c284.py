import discord
from discord.ext import commands
from discord.utils import get

class c284(commands.Cog, name="c284"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Acceleration_Synchrogear', aliases=['c284', 'Gear_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Acceleration Synchrogear',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361028.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Gear)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Synchro/Pendulum/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF) [Pendulum Scales]', value='6 (2000/0) [10/10]', inline=False)
        embed.add_field(name='Pendulum Effect', value='Fusion Pendulum monsters and Xyz Pendulum monsters cannot be targeted by your opponent\'s card effects. You can destroy this card, and if you do, add 1 "Multipurpose Pendulumgear" from your Deck to your hand.', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + 1 or more non-Tuner monsters\nDuring the Damage Step, if this card battles an opponents monster: This card gains 500 ATK, then you can change the battle position of that monster. If this card inflicts battle damage: You can target 1 Spell/Trap on the field; banish it. If this card is destroyed in the Monster Zone: You can place this card in your Pendulum Zone. You can only use each effect of "Acceleration Synchrogear" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c284(bot))