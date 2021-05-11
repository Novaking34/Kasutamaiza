import discord
from discord.ext import commands
from discord.utils import get

class c285(commands.Cog, name="c285"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Imperial_Fusiongear', aliases=['c285', 'Gear_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Imperial Fusiongear',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361031.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Gear)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Fusion/Pendulum/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF) [Pendulum Scales]', value='6 (2500/0) [10/10]', inline=False)
        embed.add_field(name='Pendulum Effect', value='Synchro Pendulum monsters and Xyz Pendulum monsters cannot be destroyed by your opponent\'s card effects. You can destroy this card, and if you do, add 1 "Multipurpose Pendulumgear" from your face-up Extra Deck to your hand.', inline=False)
        embed.add_field(name='Monster Effect', value='2 Pendulum monsters with different names\nYou can target 1 card in your Pendulum Zone: Special Summon it with its effects negated, and if you do, destroy 1 Pendulum Monster you control with the highest ATK and all monsters your opponent controls with less ATK than that monster. If this card is destroyed in the Monster Zone: You can place this card in your Pendulum Zone. You can only use each effect of "Imperial Fusiongear" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c285(bot))