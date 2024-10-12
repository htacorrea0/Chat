#Flet é uma ferramenta que pode ser usada pra criar sites, apps e programas de computador. Front e back.

import flet as ft

def main(pagina): #função, recebe como parametro a pagina
    #titulo e botão inicial
    titulo = ft.Text("ZapZap")

    #websocket é um tunel de comunicação entre dois usuarios, ou seja, permite que as mensagens sejam vistas pelos 2

    def enviar_mensagem_tunel(mensagem):
        #vai fazer na tela de todos os users
        texto = ft.Text(mensagem)
        chat.controls.append(texto)#adiciona no final
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) #criei o tunel e passei a função com as coisas que eu quero que aconteça pros 2

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value #como são variaveis, tem q ter o f na proxima linha pra formatar e entre {} pra pegar o valor
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem) #mandei pro tunel
        campo_enviar_mensagem.value = "" #pra limpar depois de enviar a msg
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui a sua mensagem", on_submit=enviar_mensagem) #on submit é pra pegar o enter
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar]) #deixando um do lado do outro, visualmente

    chat = ft.Column()

    def entrar_chat(evento):
        #fechar o popup
        popup.open = False

        #sumir com o titulo
        pagina.remove(titulo)

        #sumir com o botão iniciar chat
        pagina.remove(botao)

        #carregar o chat
        pagina.add(chat)
        pagina.add(linha_enviar)

        #fulano entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

        #carregar o campo de enviar mensagem
        pagina.add(campo_enviar_mensagem)

        #carregar o botao enviar
        pagina.add(botao_enviar)
        
        pagina.update()

    #criar o popup
    titulo_popup = ft.Text("Bem vindo ao ZapZap!")
    caixa_nome = ft.TextField(label = "Digite o seu nome") #text.field é uma text box
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title = titulo_popup, content = caixa_nome, actions = [botao_popup]) #em [] pq actions esta no plural, entao eu tenho q passar uma lista, e lista é em []

    #botao inicial
    def abrir_popup(evento): #sempre que associamos uma função a um click de um botão, ela recebe o evento
        pagina.dialog = popup #pra dizer q é um popup
        popup.open = True #exibe o popup
        pagina.update() #obrigatoriamente quando alguma função edita algo na minha tela, pra que apareça o popup sem que ele precise dar f5
        print("Clicou no botão")

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup) #on_click passa oq acontece quando clicarem nesse botao
   
    #colocar os elementos na pagina
    pagina.add(titulo)
    pagina.add(botao)
    
ft.app(main, view = ft.AppView.WEB_BROWSER) #executa a main
    