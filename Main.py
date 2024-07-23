    
import discord
import datetime 
from Etiquette import etiquettes
from discord.ext import commands
    
intents = discord.Intents.default()
intents.bans = True
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

# Nome bot 
namebot = 'Chopper'

# Reconhecer que o Bot esta rodando.
@bot.event
async def on_ready():
    print(f'Bot chamando {bot.user} está rodando!')

# O bot reconhecer toda vez que o novo membro(usuário) entra no servido.
@bot.event
async def on_member_join(member):
    welcome_channel_id = 1251648035352481795
    channel = bot.get_channel(welcome_channel_id)

    if channel: 
       description = f'Bem vindo(a) ao servidor {member.mention} , leia as regras antes de começa a usar o servidor \n'
       embed = discord.Embed(
            title = 'Bem-vindo(a)',
            description = f'{description} você pode digita "!regras" no Chat do bot para que eu informe as regras do servidor ou ir em #regras',
            color=discord.Color.blue(),
        )
       await channel.send(embed=embed)
       print(10 * '-')
       print('Mensagem de boas-vindas enviada')
       return
    else:
        print(f'Canal com ID {welcome_channel_id} não encontrado')

# O bot reconhcer sempre que um membro(usuário) sai ou removido do servidor
@bot.event
async def on_member_remove(member):
       romeve_channel_id = 1265036153329942529
       channel = bot.get_channel(romeve_channel_id)

       if channel:
           embed = discord.Embed(
               title='Usuário Saiu',
               description=f'O membro {member.mention} saiu ou foi removido do servidor.',
               color=discord.Color.red(),
           )
           await channel.send(embed=embed)
           print(10 * '-')
           print('O membro {member.name} ({member.id}) saiu ou foi removido do servidor')
           return
       else:
           print(f'Canal com ID {romeve_channel_id} não encontrado')  

# O bot reconhecer quanto membro(usuário) é banidor
@bot.event
async def on_member_ban(guild, member):
        ban_channel_id = 1262080750535184395
        channel = bot.get_channel(ban_channel_id)
        ban_time = datetime.datetime.utcnow().strftime('%H:%M')

        if channel:
            embed = discord.Embed(
                description=f'Usuário {member} foi banido do servidor {guild.name} em {ban_time} UTC',
                color=discord.Color.red(),
            )
            await channel.send(embed=embed)
            print(10 * '-')
            print(f'Usuário {member} foi banido do servidor {guild.name}')
            return
        else:
           print(f'Canal com ID {ban_channel_id} não encontrado')  


# ! Captura todos os eventos que membro(usuário) mandar no servido  .
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    Chat_chanel_id = 1251648321664057354
    channel = bot.get_channel(Chat_chanel_id)
    
    # Comandos predefinidos para mandar no Chat do Bot.
    if channel and message.channel.id == Chat_chanel_id:
        message_content = message.content.lower()

        #  Commando !oi
        if '!oi' in message_content:
            embed = discord.Embed(
                title="Saudações!", 
                description=f"Olá, {message.author.mention} oque voce deseja hoje!",
                color=discord.Color.blue(),
            )
            await message.channel.send(embed=embed)
            return

        # Commando !ajudar 
        if '!ajuda' in message_content:
            embed = discord.Embed(
                title="Bem vindo!",
                description=f"Olá!{message.author.mention}  Eu sou o Chopper, um bot criado para ajudar você. Seja bem-vindo ao servidor! Vá no chat do bot para mais informações.",
            )
            await message.channel.send(embed=embed)
            return
        
        # Commando !regras onde o Bot vai imprimir todas as regras do servido.
        if '!regras' in message_content:
            await send_rules_message(message, etiquettes)
            return
        
        # Se member(usuário) tentar mandar comando sem ! vai enviar um messgem
        if not '!' in message_content:
            embed = discord.Embed(
                description=f"{message.author.mention} Comandos so funcionar com ' ! ' na frente",
                color=discord.Color.red()
            )
            await message.channel.send(embed=embed)
            return

        # Se nenhum comando for encontrado, responde com mensagem de erro
        embed = discord.Embed(
                description=f"{message.author.mention} esse comando não existir!",
                color=discord.Color.red()
        )
        await message.channel.send(embed=embed)


    await bot.process_commands(message) 
                                                                                                                                                                                 
# Função para imprimir regras na tela.      
async def send_rules_message(message, etiquettes):      
        rules_discription = format_rules(etiquettes)
        embed = discord.Embed(
            title="Regras do servidor",
            description=rules_discription,
            color=discord.Color.blue(),
        )
        await message.channel.send(embed=embed)
def format_rules(etiquettes):
    description = "Essas são as regras que devem ser seguidas:\n\n"
    for idx, rule in etiquettes.items():
        description += f"{idx}. {rule}\n\n"
    return description





bot.run('')