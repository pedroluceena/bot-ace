import discord
from discord.ext import commands
import random
import asyncio
import wikipedia
from Pymoe import Anilist
instance = Anilist()


wikipedia.set_lang("pt")


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '>', case_insensitive = True , intents = intents)

# Essa função será chamada quando bot estiver online
@client.event
async def on_ready():
  print('O Robo ta ligado pronto para servir: {0.user}'.format(client))

# Essa função responde olá para o usuário
@client.command()
async def ola(ctx):
  await ctx.send(f'Olá, {ctx.author}')

#Comandos Básicos do Ace Bot 
@client.command()
async def comandos(ctx):
  await ctx.send('COMANDOS BÁSICOS DO ACE BOT \n >Ola \n >dado \n >tabuada \n >regras \n >canal \n >pesquisar \n >play ')

#Entrada de um Membro novo no Server
@client.event
async def on_member_join(member):
  welcome = client.get_channel(814941053332881423)
  regras = client.get_channel(852486778157793280)
  canal = client.get_channel(852528776088387614)


  welcomeTitle = f'Bem Vindo! @{member}'
  embed = discord.Embed(
    title = welcomeTitle,
    description = 'ATENÇÃO!',
    colour = 255
  )

  embed.add_field(
    name = 'Leia as regras!',
    value = regras.mention,
    inline = False
  )

  embed.add_field(
    name = 'Leia sobre os canais!',
    value = canal.mention,
    inline = False
  )

  embed.set_image( url = 'https://media1.tenor.com/images/c5fad21f9828d19044a58f8b84a6e14b/tenor.gif?itemid=6013419' )

  messagem = await welcome.send(embed = embed)

  await asyncio.sleep(1800)

  await messagem.delete()

  

# Jogo de dado
@client.command()
async def dado(ctx, number):
  delta = random.randint(1, int(number))
  await ctx.send(f'O numero que saiu do dado foi {delta}')

# Tabuada
@client.command()
async def tabuada(ctx, numero):
  for c in range(1, 11):
   await ctx.send('{} x {} = {}'.format(numero, c , int 
   (numero) * c))


# Embed de Regras
@client.command()
async def regras(ctx):
  embed = discord.Embed(
    title = 'Regras',
    description = '1 - Compartilhe o conhecimento! \n''2 - Proíbido qualquer tipo de preconceito. \n''3 - Proíbido qualquer tipo de contéudo nsfw vulgo pornografia.\n''4 - Respeitar cada significado do Canal.\n''5 - Só certos membros são permitidos está aqui!\n''5.1 - Alunos de TI(Não Importa a Faculdade)\n' '5.2 - Ex-Alunos \n''5.3 - Programadores[A pessoa deve ser conhecida por algum membro e possuir um github] \n' '6 - Divirta-se ! \n',
    colour = 16711680
  )

  embed.set_author(
    name = 'SEJA BEM VINDO AO GRUPO DE ADS!',
    icon_url = 'https://cdn0.iconfinder.com/data/icons/shift-free/32/Error-512.png')
  

  embed.set_image(url = 'https://media1.tenor.com/images/dbd6f82a006047970f8a8c684bd2d5dc/tenor.gif?itemid=16034137')

  await ctx.send(embed = embed)

#Embed significado de cada Canal
@client.command()
async def canal(ctx):
  embed = discord.Embed(
    title = 'Canais de Texto e Audio ',
    description = 'Canal de Welcome -> Canal de Boas-Vindas. \n''Canal de Regras -> Onde você pode visualizar todas as regras do canal. \n' 'Canal de Off-Topic -> Canal Principal de Conversa sobre a faculdade e Assuntos diversos. \n' 'Canal de Vagas -> Divulgação de Vagas para os Colegas. \n' 'Canal de Music -> Canal para Gerenciamento do Bot de Musica. \n' 'Canal de Trabalho -> Onde você tira duvida  e compartilha os códigos com os colegas. \n' 'Gameplay -> Canal para zoeira e jogos. \n' 'Class Room -> Nossa sala de Aula \n' 'Grupo -> Canal Focado para o separação de grupos. \n',
    colour = 16776960
  )
  embed.set_author(
    name = 'GUIA DE CADA CANAL',
    icon_url = 'https://cdn0.iconfinder.com/data/icons/shift-free/32/Lemon-512.png')

  embed.set_image(url = 'https://media1.tenor.com/images/62eaf4b2823dd0973bc88f38e214b864/tenor.gif?itemid=14435882')
 
  await ctx.send(embed = embed)

  
#Funçãp de Pesquisar na wikipedia
@client.command()
async def pesquisar(ctx, about):

  try:
    summaryContent = wikipedia.summary(about, sentences=2)
    page = wikipedia.page(about)
  except :
    await ctx.send(f'Chave {about} não encontrada tente outra.')
    return

  urlContent = page.url
  imageContent = f'https://source.unsplash.com/1600x900/?{about}' 

  titleEmbed = f'O que é {about}?'

  embed = discord.Embed(
    title = titleEmbed,
    description = '',
    colour = 16776960
  )

  embed.set_author(
    name = 'Wikipedia',
    icon_url = 'https://cdn0.iconfinder.com/data/icons/socialize-part-3-icons-set/128/wikipedia.png'
  )

  embed.set_image(
    url = imageContent
  )

  embed.add_field(
    name = about,
    value = summaryContent,
    inline = False
  )

  embed.add_field(
    name = 'Saiba Mais: ',
    value = urlContent,
    inline = False
  )


  await ctx.send(embed = embed)


  
#Lista de Anime 
@client.command()
async def Anime (ctx , about):
  data = instance.search.anime(about)
  media = data["data"]["Page"]["media"][0]
  title = media["title"]["english"]
  popularity = media["popularity"]
  episodes = media["episodes"]
  averageScore = media["averageScore"]
  isAdult = media["isAdult"]
  isAdultResponse = ""

  if isAdult:
    isAdultResponse = "Sim"
  else:
    isAdultResponse = "Não"

  embed = discord.Embed(
    title = title,
    description = '',
    colour = 2067276
  )

  embed.add_field(
    name = 'Popularidade',
    value = popularity,
    inline = False
  )

  embed.add_field(
    name = 'Média',
    value = averageScore,
    inline = False
  )

  embed.add_field(
    name = 'Episódios',
    value = episodes,
    inline = False
  )

  embed.add_field(
    name = '+18',
    value = isAdultResponse,
    inline = False
  )

  await ctx.send(embed = embed)
 



@client.event
async def on_menssage(message):
  if message.content.startswith('>music'):
    canal = message.author.voice.voice_channel
    await client.join_voice_channel(canal)

client.run('KEY HERE')
