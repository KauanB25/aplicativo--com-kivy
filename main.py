from kivymd.app import MDApp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from functools import partial
from kivymd.uix.floatlayout import MDFloatLayout


def envio_email(email):
        # Configurações do servidor SMTP
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 587
        SMTP_USERNAME = ''
        SMTP_PASSWORD = ''

        # Criação da mensagem
        msg = MIMEMultipart()
        msg['From'] = ''
        msg['To'] = email
        msg['Subject'] = 'Testando código python'

        # Corpo do e-mail
        body = 'Conteúdo do e-mail.'
        msg.attach(MIMEText(body, 'plain'))

        # Conexão com o servidor SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        # Envio do e-mail
        server.send_message(msg)
        server.quit()

KV = '''
MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: "vertical"
                    md_bg_color: "#1E1E15"
                    Barra:
                    MyBox:
        MDNavigationDrawer:
            id: nav_drawer
            #on_close: lambda: app.close_drawer()  # Adiciona o evento de callback
            orientation: "vertical"
            radius: (0, 16, 16, 0)
            ContentNavigationDrawer:
                id: content_drawer  # Adiciona um ID ao ContentNavigationDrawer
                orientation: 'vertical'
                nav_drawer: nav_drawer
                MDLabel:
                    text: 'Emais cadastrados'
                    pos_hint: {'center_x': .5, 'center_y': .9}            
<MyBox>:
    MDFloatLayout:
        md_bg_color: 'white'
        MDIconButton:
            icon: "alert-outline"
            pos_hint: {"center_x": .5, "center_y": .5}
            icon_size: "100sp"
            md_bg_color: 'red'
            theme_icon_color: "Custom"
            icon_color: 'white'
            on_release: app.disparo_emails()

<CadastroEmail>:
    orientation: 'vertical'
    size_hint: .7, .7
    pos_hint: {'center_x': .5, 'center_y': .5}
    MDBoxLayout:
        size_hint_y: .2
        padding: [25, 0, 25, 0]
        md_bg_color: app.theme_cls.primary_color
        MDLabel:
            text: 'Cadastro de emails'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
        MDIconButton:
            theme_text_color: 'Custom'
            icon: 'close'
            text_color: 1, 1, 1, 1
            on_release: root.fechar()
    MDFloatLayout:
        MDTextField:
            id: email1
            pos_hint: {'center_x': .5, 'center_y': .8}
            size_hint_x: .9
            hint_text: root.email1_class
        MDTextField:
            id: email2
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: .9
            hint_text: root.email2_class
        MDTextField:
            id: email3
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint_x: .9
            hint_text: root.email3_class
        MDRaisedButton:
            text: "Salvar"
            pos_hint: {'center_x': .5, 'center_y': .2}
            on_release: root.salvar()
            on_release: app.atualizar()


<Barra>:
    title: "App"
    anchor_title: "left"
    right_action_items: [["plus", lambda x: root.abrir()]]
    left_action_items: [['menu', lambda x: app.root.ids.nav_drawer.set_state("open")]]

'''


email1 = 'Email 1'
email2 = 'Email 2'
email3 = 'Email 3'


class CadastroEmail(MDCard):
    email1_class = email1
    email2_class = email2
    email3_class = email3

    

    def salvar(self):
        global email1, email2, email3
        email1 = self.ids.email1.text
        email2 = self.ids.email2.text
        email3 = self.ids.email3.text
        
    def atualizar_campos(self):
        global email1, email2, email3
        self.email1_class = email1
        self.email2_class = email2
        self.email3_class = email3
        self.ids.email1.hint_text = self.email1_class
        self.ids.email2.hint_text = self.email2_class
        self.ids.email3.hint_text = self.email3_class
    def fechar(self):
        print(f'email1: {email1}')
        self.parent.remove_widget(self)


class ContentNavigationDrawer(MDFloatLayout):
    nav_drawer = None
    clas_em1 = email1
    clas_em2 = email2
    clas_em3 = email3
    
    def __init__(self, **kwargs):
        super(ContentNavigationDrawer, self).__init__(**kwargs)
        
        self.label1 = MDLabel(text='Email 1: ' + self.clas_em1,pos_hint={'center_x': .5, 'center_y': .7})
        self.label2 = MDLabel(text='Email 2: ' + self.clas_em2,pos_hint={'center_x': .5, 'center_y': .6})
        self.label3 = MDLabel(text='Email 3: ' + self.clas_em3,pos_hint={'center_x': .5, 'center_y': .5})
        self.botao = MDRectangleFlatButton(text='Atualizar',on_release=partial(self.atualizar))
        self.add_widget(self.label1)
        self.add_widget(self.label2)
        self.add_widget(self.label3)
        self.add_widget(self.botao)
    def atualizar(self,*args):
        global email1, email2, email3
        self.remove_widget(self.label1)
        self.remove_widget(self.label2)
        self.remove_widget(self.label3)
        self.remove_widget(self.botao)
        if email1 =='':
            email1='Email 1'
        if email2=='':
            email2 = 'Email 2'
        if email3=='':
            email3 = 'Email 3'
        self.label1 = MDLabel(text='Email 1: ' + email1,pos_hint={'center_x': .5, 'center_y': .7})
        self.label2 = MDLabel(text='Email 2: ' + email2,pos_hint={'center_x': .5, 'center_y': .6})
        self.label3 = MDLabel(text='Email 3: ' + email3,pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.label1)
        self.add_widget(self.label2)
        self.add_widget(self.label3)
        self.add_widget(self.botao)


class Barra(MDTopAppBar):
    nav_drawer = ObjectProperty()

    def abrir(self):
        self.parent.parent.add_widget(CadastroEmail())


class MyBox(MDBoxLayout):
    def get_text(self):
        text = self.ids.campo.text
        print(f'{text}')


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.nav_drawer.nav_drawer = self.root.ids.nav_drawer

    def disparo_emails(self):
        emails=[email1,email2,email3]
        for c in emails:
            try:
                envio_email(email=c)
            except:
                print('Erro')

    def atualizar(self):
        content_drawer = self.root.ids.content_drawer
        content_drawer.atualizar()

    


MyApp().run()
