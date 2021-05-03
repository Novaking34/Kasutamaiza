import discord
from discord.ext import commands
from discord.utils import get

class c139(commands.Cog, name="c139"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Dinomage_Li-Cho', aliases=['c139', 'Dinomage_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Dinomage Li-Cho',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334915.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Dinomage)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Dinosaur/Pendulum/Normal (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF) [Pendulum Scales]', value='5 (2050/1850) [3/3]', inline=False)
        embed.add_field(name='Pendulum Effect', value='Once per turn: You can target 1 Dinosaur monster you control; Return that target to your hand, then Special Summon this card from your Pendulum Zone.', inline=False)
        embed.add_field(name='Lore Text', value='Infused with a powerful magic. Li-Cho hopes to spread his new teachings across the realms. one day hoping to build a Dinomage empire of his own.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c139(bot))