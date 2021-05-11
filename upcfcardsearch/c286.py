import discord
from discord.ext import commands
from discord.utils import get

class c286(commands.Cog, name="c286"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Oblique_Xyzgear', aliases=['c286', 'Gear_4'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Oblique Xyzgear')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361044.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Gear)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Xyz/Pendulum/Effect (WATER)', inline=False)
        embed.add_field(name='Rank (ATK/DEF) [Pendulum Scales]', value='6 (2500/0) [10/10]', inline=False)
        embed.add_field(name='Pendulum Effect', value='If a Synchro Pendulum monster or Fusion Pendulum monster battles, your opponent cannot activate cards or effects until the end of the Damage Step. You can destroy this card, and if you do, add 1 "Multipurpose Pendulumgear" from your GY to your hand.', inline=False)
        embed.add_field(name='Monster Effect', value='2 Level 6 monsters\nIf you can Pendulum Summon Level 6, you can Pendulum Summon this face-up card in your Extra Deck. If this card is Pendulum Summoned: You can attach 1 Pendulum Monster from your GY to this card. (Quick Effect): You can detach 1 material and target 1 monster in either player\'s GY; banish it, and if you do, you can change the battle position of one of your opponent\'s monsters. If this card is destroyed in the Monster Zone: You can place this card in your Pendulum Zone. You can only use each effect of "Oblique Xyzgear" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c286(bot))