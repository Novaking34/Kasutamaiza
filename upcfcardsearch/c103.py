import discord
from discord.ext import commands
from discord.utils import get

class c103(commands.Cog, name="c103"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Fantastical_Elephante', aliases=['c103', 'Fantasical_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Fantastical Elephante',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321556.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Fantastical)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast/Toon/Fusion/Pendulum/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF) [Pendulum Scales]', value='4 (1500/1600) [1/1]', inline=False)
        embed.add_field(name='Pendulum Effect', value='If you do not control another "Fantastical" card in your Pendulum Zone, this card\'s Pendulum Scale becomes 4. Once per turn: You can return 1 Toon Monster you control to your hand; take 1 Toon Pendulum Monster from your Deck and either add it to your hand or place it in your face-up Extra Deck.', inline=False)
        embed.add_field(name='Monster Effect', value='2 Toon Monsters\nWhile you control "That\'s All Folks" and your opponent controls no other Toon Monsters, this card can attack your opponent directly. During your End Phase, if you do not control "That\'s All Folks": Destroy this card and all other Toon Monsters you control, then place this card in an unoccupied Pendulum Zone you control. Once per turn: You can shuffle 3 card that specifically list "Toon Monster" in its text from your GY into your Deck; gain 1500 LP.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c103(bot))