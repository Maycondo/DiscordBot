
# Discord Bot

Bot automatizador desenvolvidor completamenter com linguagemde programaçao Python, com funções personalizadas.

## Estrutura do Projeto

- **`Main.py`**: Arquivo principal que inicializa o bot.
- **`Etiquette.py`**: Contém funcionalidades relacionadas a regras que o usuário dever sergui.
- **`.venv`**: Ambiente virtual para gerenciar as dependências do projeto.
- **`__pycache__`**: Diretório gerado automaticamente para armazenar os arquivos compilados.

## Tecnoligias Utilizadas 

- **[Python](https://www.python.org/)**: Linguagem principal para o desenvolvimento do Bot.
- **[discord.py](https://discordpy.readthedocs.io/)**: Biblioteca usada para criar o bot e interagir com API do discord.

## funcionalidades


- **Mensagem de Boas-vindas** 
   
    O Bot enviar menssagen de boas-vindas personalizadar cada novo membro que entra no servido.

 *Exemplo* 
 
    🎉 Bem vindo(a) ao servidor {member.mention}! Aproveite o servidor e divirta-se!


- **Moderação Básica**
 
    Comando para **banir** ou **expulsar** membros do servidor.

 *Exemplo* 

    ⚠️ O membro {member.mention} saiu ou foi removido do servidor. 🚪  

 *Exemplo* 
 
    🚨 Alerta: O usuário {member} foi banido do servidor {guild.name} em 🕒 {ban_time} UTC. 🚫 


- **Regras de Etiqueta**
 
    Comando para **banir** ou **expulsar** membros do servidor.
