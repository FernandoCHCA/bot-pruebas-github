from config import *
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType

class ServerInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.slash_command(guild_ids=[ServersID], name='server-info', description='Mira la informacion del servidor!')
    async def server_info(self, interaction: Interaction):
        #role_count = len(interaction.guild.roles)
        embed = nextcord.Embed(color=0x1FD3F3)
        Contador_humanos = len(interaction.guild.humans)
        Contador_bots = len(interaction.guild.bots)
        list_of_bots = [bot.mention for bot in interaction.guild.members if bot.bot]
        list_of_roles = [role.mention for role in interaction.guild.roles if role.role]

        embed.set_author(name=interaction.guild)
        embed.set_thumbnail(interaction.guild.icon)
        embed.add_field(name='Owner', value=interaction.guild.owner.mention, inline=False)
        embed.add_field(name='Creado', value=interaction.guild.created_at.__format__('%d/%m/%Y, %H:%M:%S PM'), inline=False)
        embed.add_field(name='Contador de Miembros', value='〔🧒🏻​ {} humanos〕 | 〔🤖​ {} bots〕 | 〔🧔🏻​ {} total〕'.format(Contador_humanos, Contador_bots, interaction.guild.member_count), inline=False)
        #embed.add_field(name='Top rol', value=interaction.guild.roles[-31])
        #embed.add_field(name='Bots', value=list_of_bots, inline=False)
        embed.add_field(name='Roles', value=list_of_roles, inline=False)
        #embed.set_footer(text=f'Requested by: {interaction.user.name}#{interaction.user.discriminator}\n{Fecha_actual}', icon_url='https://i.ibb.co/nCCJ2Wb/378-3782140-discord-server-icon-cute-imagenes-para-perfil-de.png')
        await interaction.response.send_message(embed=embed)

#Setup 
def setup(client):
    client.add_cog(ServerInfo(client))