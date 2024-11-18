
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
 
<<<<<<< HEAD
    O Bot lembra os usuários das regras básicas do servido quanso e solicitado comamdo. **`!regras`**
=======
    O Bot lembra os usuários das regras básicas do servidor quando e solicitado comamdo. **`!regras`**
>>>>>>> 538dfed (Fazendo algumas alterações no bot é documentando.)

*Exemplo*   

    📜 Essas são as regras que devem ser seguidas:
      1️⃣ Respeito: Trate todos com respeito. Comentários ofensivos ou discriminatórios não serão tolerados.
      2️⃣ Sem Spam: 🚫 Evite spam ou flood nos canais.
      3️⃣ Canais Apropriados: 📂 Use os canais para os tópicos correspondentes.
      4️⃣ Conteúdo Proibido: 🚷 Não poste conteúdo ilegal ou NSFW.
      5️⃣ Moderadores: 🛡️ Siga as instruções dos moderadores para manter a harmonia no servidor. 

- **Sistema de comandos**
 
    O Bot responde a comando pré-configurados para realizar diversas ações. Só funcionar chat do bot.

*Exemplo*

   **`!ajudar`**: Mostra todos os comandos disponíveis.

<<<<<<< HEAD
   **`!Oi`**: Retorna um  apresentação de voltar
   
   **`!Regras`**: Retorna um  apresentação de voltar



 
=======
   **`!Oi`**: Retorna um  apresentação de voltar.
   
   **`!Regras`**: Imprimir todas as regras do servidor.

*Aviso se membro manda um commando sem esta listado,  o bot envia a seguinte mensagem de aviso.*

    ❌ {message.author.mention}, esse comando não existe! 🤔💡 Tente novamente ou use !ajuda para ver os comandos disponíveis.",.

*Se o usuário não utilizar **`!`** no início do comando, o bot responde com a seguinte mensagem  .*
    
    ⚠️ {message.author.mention}, os comandos só funcionarão se você usar '!' na frente! ❗😊

## Sobre a Biblioteca **`discord.py`**
 A Biblioteca **`discord.py `** foi usada para facilitar o desenvolvidor e crição do bot, Ela fornece uma interface amigavel para interagir com API do Discord.

 - Criar commandos personalizados
 - Gerenciar eventos como mensagens, reações e novos membros.
 - Enviar mensagens e gerenciar canais

 Para mais informações, visite a **[discord.py](https://discordpy.readthedocs.io/)**.
>>>>>>> 538dfed (Fazendo algumas alterações no bot é documentando.)
