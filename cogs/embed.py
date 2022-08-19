import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType
from config import *

class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Embed command
    @slash_command(name='embed-create', description='Crea un embed para ti!', guild_ids=[ServersID])
    async def embed_create(self, 
    ctx:Interaction,
    title: str = nextcord.SlashOption(name='embed-title', description='Titulo de tu embed', required=False),
    description: str = nextcord.SlashOption(name='embed-description', description='Mensaje de descripcion de su embed', required=False),
    colour: str = nextcord.SlashOption(name='embed-colour', description='Proporcione un código hexadecimal para el color de su embed', required=False),
    footer: str = nextcord.SlashOption(name='embed-footer', description='Mensaje del footer de su embed', required=False),
    footer_icon: nextcord.Attachment = nextcord.SlashOption(name='embed-footer-icon', description='Seleccione un archivo de imagen para el icono del footer', required=False),
    channel: nextcord.abc.GuildChannel = nextcord.SlashOption(channel_types=[ChannelType.text],name='channel', description='Seleccione el canal donde se enviara su embed', required=False),
    image: nextcord.Attachment = nextcord.SlashOption(name='embed-image', description='Seleccione un archivo de imagen para incrustar la imagen', required=False),
    thumbnail: nextcord.Attachment = nextcord.SlashOption(name='embed-thumbnail', description='Seleccione un archivo de imagen para incrustar la miniatura', required=False),
    author: str = nextcord.SlashOption(name='embed-author', description='Mensaje del autor de su embed', required=False),
    author_icon: nextcord.Attachment = nextcord.SlashOption(name='embed-author-icon', description='Seleccione un archivo de imagen', required=False)
    ):
        embed = nextcord.Embed()
        if not channel:
            channel = ctx.channel
        if author is not None and author_icon is not None:
            embed.set_author(name=author, icon_url=author_icon)
        elif author is not None and author_icon is None:
            embed.set_author(name=author)
        elif author is None and author_icon is not None:
            pass
        if title:
            embed.title=title
        if description:
            embed.description=description
        if footer_icon is not None and footer_icon is not None:
            embed.set_footer(text=footer, icon_url=footer_icon)
        elif footer is not None and footer_icon is None:
            embed.set_footer(text=footer)
        elif footer is None and footer_icon is not None:
            pass
        if image:
            embed.set_image(url=image)
        if thumbnail:
            embed.set_thumbnail(url=thumbnail)
        if colour:
            embed.colour=int("0x" + colour, 16)
        if not author and not title and not description and not footer and not image and not thumbnail and not colour:
            await ctx.response.send_message("Por favor, escriba alguno de estos valores", ephemeral=True)
        else:
            await channel.send(embed=embed)

#Setup 
def setup(client):
    client.add_cog(Embed(client))