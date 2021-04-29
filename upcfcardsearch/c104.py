import discord
from discord.ext import commands
from discord.utils import get

class c104(commands.Cog, name="c104"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Fantastical_Kumo', aliases=['c104', 'Fantastical_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Fantastical Kumo',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321557.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Fantastical)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Toon/Fusion/Pendulum/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF) [Pendulum Scales]', value='3 (700/1500) [5/5]', inline=False)
        embed.add_field(name='Pendulum Effect', value='If you do not control another "Fantastical" card in your Pendulum Zone, this card\'s Pendulum Scale becomes 4. Once per turn, if you Pendulum Summon a Toon Monster: You can target 1 card in your face-up Extra Deck and either add it to your hand OR place it in an unoccupied Pendulum Zone, and if you do, destroy this card.', inline=False)
        embed.add_field(name='Monster Effect', value='2 Toon Monsters\nWhile you control "That\'s All Folks" and your opponent controls no other Toon Monsters, this card can attack your opponent directly. During your End Phase, if you do not control "That\'s All Folks": Destroy this card and all other Toon Monsters you control, then place this card in an unoccupied Pendulum Zone you control. Once per turn: You can target 1 monster on the field; reduce its ATK by 600, then if that monster\'s ATK is reduced to 0, destroy it.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c104(bot))