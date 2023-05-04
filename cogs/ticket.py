import discord

from discord.ext import commands
from discord import app_commands


import random
import datetime


import discord

from discord.ext import commands
from discord import app_commands

import random
import datetime


from config.config import funfact
funFact = [funfact]




class Ticket_Sel(discord.ui.Select):
    def __init__(self):

        options=[
            discord.SelectOption(label="Partenariat",emoji="<:partner:1103436953522815066>",description="Faire une demande de partenariat"),
            discord.SelectOption(label="Repport",emoji="<:support:1103436986615869441>",description="Signaler un membre"),
            discord.SelectOption(label="Prendre Commande",emoji="<:gift:1103437380570058862>",description="Prendre une commande"),
            discord.SelectOption(label="Devenir Staff",emoji="<:staff:1103437379269820426>",description="Postuler pour devenir Staff"),
            discord.SelectOption(label="Question",emoji="<:person:1103436970786558052>",description="Poser une question")
            ]
        super().__init__(placeholder="Séléctionne ta catégorie",max_values=1,min_values=1,options=options, custom_id="ticket_selec")
    async def callback(self, interaction2: discord.Interaction):
        client1 = interaction2.user

        # Remplace ID_ROLE_SUPPORT par l'ID du rôle support sur ton serveur
        support = interaction2.guild.get_role(ID_ROLE_SUPPORT)

        # Remplace ID_ROLE_OWNER par l'ID du rôle owner sur ton serveur
        owner = interaction2.guild.get_role(ID_ROLE_OWNER)

        overwrite2 = interaction2.channel.overwrites_for(interaction2.user)
        overwrite2.read_messages= False
        overwrite2.send_messages = False
        overwrite2.view_channel = False


        overwrite3 = interaction2.channel.overwrites_for(support)
        overwrite3.send_messages = False



        class button_inside(discord.ui.View):
            def __init__(self) -> None:
                super().__init__(timeout=None)

            @discord.ui.button(label="Fermer ticket", style=discord.ButtonStyle.primary, emoji="<:wrong:1103445581889806426>", custom_id="fermer_button")
            async def fermer(self, interaction: discord.Interaction, button: discord.ui.Button):
                if interaction.user.id == client1.id:
                    await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
                else:
                    embed4 = discord.Embed(
                        description=f"{interaction.channel.mention} a bien été fermé !", color=0x0ce838)

                    embed6 = discord.Embed(title=f"Fermeture du {interaction.channel.name}", color=discord.Color.blurple())
                    embed6.set_thumbnail(url=client1.avatar)
                    embed6.add_field(name="➔ Modérateur Responsable", value=interaction.user.mention, inline=True)
                    embed6.add_field(name="➔ Utilisateur", value=client1.mention, inline=True)
                    embed6.set_footer(text=random.choice(funFact))
                    embed6.timestamp = datetime.datetime.now()

                    # Remplace ID_CHANNEL_LOGS par l'ID du channel des logs (Active le mode développeur sur Discord)
                    logs = interaction.guild.get_channel(ID_CHANNEL_LOGS)

                    await interaction.channel.set_permissions(client1, overwrite=overwrite2)
                    await interaction.response.send_message(embed=embed4)
                    await logs.send(embed=embed6)

            @discord.ui.button(label="Supprimer", style=discord.ButtonStyle.danger, emoji="🗑️", custom_id="supprimer_button")
            async def supprimer(self, interaction: discord.Interaction, button: discord.ui.Button):
                if interaction.user.id == client1.id:
                    await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
                    return
                else:
                    await interaction.channel.delete()

                    embed8 = discord.Embed(title=f"Suppression du {interaction.channel.name}", color=discord.Color.red())
                    embed8.set_thumbnail(url=client1.avatar)
                    embed8.add_field(name="➔ Modérateur Responsable", value=interaction.user.mention, inline=True)
                    embed8.add_field(name="➔ Utilisateur", value=client1.mention, inline=True)
                    embed8.set_footer(text=random.choice(funFact))
                    embed8.timestamp = datetime.datetime.now()

                    # Remplace ID_CHANNEL_LOGS par l'ID du channel des logs (Active le mode développeur sur Discord)                        
                    logs = interaction.guild.get_channel(ID_CHANNEL_LOGS)
                    await logs.send(embed=embed8)

            @discord.ui.button(label="Claim", style=discord.ButtonStyle.green, emoji="🙋", custom_id="claim_button")
            async def claim(self, interaction: discord.Interaction, button: discord.ui.Button):
                if interaction.user.id == client1.id:
                    await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
                    return
                else:
                    await interaction.channel.set_permissions(support, overwrite=overwrite3)

                    embed10 = discord.Embed(
                        description=f"{interaction.user.mention} a claim ce ticket !", color=discord.Color.blue())
                    await interaction.response.send_message(embed=embed10)





        from config.config import categorie_partenariat
        from config.config import categorie_commande
        from config.config import categorie_repport
        from config.config import categorie_question
        from config.config import categorie_staff

        categorie_partenariat = discord.utils.get(interaction2.guild.categories, name=categorie_partenariat)
        categorie_commande = discord.utils.get(interaction2.guild.categories, name=categorie_commande)
        categorie_repport = discord.utils.get(interaction2.guild.categories, name=categorie_repport)
        categorie_staff = discord.utils.get(interaction2.guild.categories, name=categorie_staff)
        categorie_question = discord.utils.get(interaction2.guild.categories, name=categorie_question)

        overwrite = interaction2.channel.overwrites_for(interaction2.user)
        overwrite.read_messages= True
        overwrite.send_messages = True
        overwrite.view_channel = True

        from config.config import logo

        embed = discord.Embed(title="Ticket Ouvert", description=f"{client1.mention} vous venez d'ouvrir un ticket.\nUne personne de notre équipe s'occupera de vous au plus vite.", color=discord.Color.blurple())
        embed.set_thumbnail(url=logo)
        embed.set_footer(text=random.choice(funFact))
        embed.timestamp = datetime.datetime.now()



        if self.values[0] == "Partenariat":      
            channel = await interaction2.guild.create_text_channel(f'Ticket-{interaction2.user.name}', category=categorie_partenariat)
            await channel.set_permissions(interaction2.user, overwrite=overwrite)
            await interaction2.response.send_message(f"{channel.mention}", ephemeral=True)
            mess =  await channel.send(embed=embed, content=owner.mention, view=button_inside())
            mess: discord.Message
            await mess.pin()
            await mess.channel.purge(limit=1)
            

            
        elif self.values[0] == "Repport":
            channel = await interaction2.guild.create_text_channel(f'Ticket-{interaction2.user.name}', category=categorie_repport)
            await channel.set_permissions(interaction2.user, overwrite=overwrite)
            await interaction2.response.send_message(f"{channel.mention}", ephemeral=True)
            mess = await channel.send(embed=embed, content=f"{owner.mention} {support.mention}", view=button_inside())
            mess: discord.Message
            await mess.pin()
            await mess.channel.purge(limit=1)
        
        elif self.values[0] == "Prendre Commande":
            channel = await interaction2.guild.create_text_channel(f'Ticket-{interaction2.user.name}', category=categorie_commande)
            await channel.set_permissions(interaction2.user, overwrite=overwrite)
            await interaction2.response.send_message(f"{channel.mention}", ephemeral=True)
            mess =  await channel.send(embed=embed, content=owner.mention, view=button_inside())
            mess: discord.Message
            await mess.pin()
            await mess.channel.purge(limit=1)            
        
        elif self.values[0] == "Devenir Staff":
            channel = await interaction2.guild.create_text_channel(f'Ticket-{interaction2.user.name}', category=categorie_staff)
            await channel.set_permissions(interaction2.user, overwrite=overwrite)
            await interaction2.response.send_message(f"{channel.mention}", ephemeral=True)
            mess =  await channel.send(embed=embed, content=owner.mention, view=button_inside())
            mess: discord.Message
            await mess.pin()
            await mess.channel.purge(limit=1)


        elif self.values[0] == "Question":
            channel = await interaction2.guild.create_text_channel(f'Ticket-{interaction2.user.name}', category=categorie_question)
            await channel.set_permissions(interaction2.user, overwrite=overwrite)         
            await interaction2.response.send_message(f"{channel.mention}", ephemeral=True)
            mess =  await channel.send(embed=embed, content=f"{owner.mention} {support.mention}", view=button_inside())
            mess: discord.Message
            await mess.pin()
            await mess.channel.purge(limit=1)


class SelectView(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        self.add_item(Ticket_Sel())


class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='ticket', description="Active le système de ticket")
    @app_commands.default_permissions(administrator=True)
    async def ticket_slash(self, interaction: discord.Interaction):
        from config.config import logo

        embed = discord.Embed(title="**Ouvrir un ticket**",
                            description="Pour créer un ticket, merci de bien vouloir sélectionner une des catégorie ci-dessous.", color=discord.Color.blurple())
        embed.set_thumbnail(url=logo)
        embed.set_footer(text=random.choice(funFact))
        embed.timestamp = datetime.datetime.now()
        await interaction.channel.send(embed=embed, view=SelectView())
        await interaction.response.send_message("Système de tiket bien envoyé !", ephemeral=True)

    @app_commands.command(name='fermer', description='Ferme le ticket')
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(
        user = "L'utilisateur à supprimer du ticket",
    )
    async def close_command(self, interaction: discord.Interaction, user: discord.Member):
        
        ticket, name = interaction.channel.split('-')

        overwrite2 = interaction.channel.overwrites_for(user)
        overwrite2.read_messages= False
        overwrite2.send_messages = False
        overwrite2.view_channel = False
        
        embed4 = discord.Embed(
            description=f"{interaction.channel.mention} a bien été fermé !", color=0x0ce838)

        embed6 = discord.Embed(title=f"Fermeture du {interaction.channel.name}", color=discord.Color.blurple())
        embed6.set_thumbnail(url=user.avatar)
        embed6.add_field(name="➔ Modérateur Responsable", value=interaction.user.mention, inline=True)
        embed6.add_field(name="➔ Utilisateur", value=user.mention, inline=True)
        embed6.set_footer(text=random.choice(funFact))
        embed6.timestamp = datetime.datetime.now()
        
        # Remplace ID_CHANNEL_LOGS par l'ID du channel des logs (Active le mode développeur sur Discord)
        logs = interaction.guild.get_channel(ID_CHANNEL_LOGS)

        for user in interaction.guild.members:
            if user.name == name:
                await interaction.response.send_message(embed=embed4)
                await logs.send(embed=embed6)          
                await interaction.channel.set_permissions(user, overwrite=overwrite2)     

    @app_commands.command(name='supprimer', description='Supprime le ticket')
    @app_commands.default_permissions(administrator=True)
    async def supprimer_command(self, interaction: discord.Interaction):

        
        embed8 = discord.Embed(title=f"Suppression du {interaction.channel.name}", color=discord.Color.red())
        embed8.set_thumbnail(url=user.avatar)
        embed8.add_field(name="➔ Modérateur Responsable", value=interaction.user.mention, inline=True)
        embed8.add_field(name="➔ Utilisateur", value=user.mention, inline=True)
        embed8.set_footer(text=random.choice(funFact))
        embed8.timestamp = datetime.datetime.now()

        # Remplace ID_CHANNEL_LOGS par l'ID du channel des logs (Active le mode développeur sur Discord)
        logs = interaction.guild.get_channel(ID_CHANNEL_LOGS)

        ticket, name = interaction.channel.split('-')

        for user in interaction.guild.members:
            if user.name == name:
                await interaction.channel.delete()
                await logs.send(embed=embed8)

    @app_commands.command(name='claim', description='Claim le ticket')
    @app_commands.default_permissions(administrator=True)
    async def supprimer_command(self, interaction: discord.Interaction):

        # Remplace ID_ROLE_SUPPORT par l'ID du rôle support sur ton serveur
        support = interaction.guild.get_role(ID_ROLE_SUPPORT)

        overwrite3 = interaction.channel.overwrites_for(support)
        overwrite3.send_messages = False


        await interaction.channel.set_permissions(support, overwrite=overwrite3)

        embed10 = discord.Embed(
            description=f"{interaction.user.mention} a claim ce ticket !", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed10)

async def setup(bot):
    await bot.add_cog(Ticket(bot))                        