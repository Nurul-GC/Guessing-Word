#  Copyright (c) 2019-2020 Nurul GC
#  Direitos Autorais (c) 2019-2020 Nurul GC
#
#  Jovem Programador
#  Estudante de Engenharia de Telecomunicaçoes
#  Tecnologia de Informação e de Medicina.
#  Foco Fé Força Paciência
#  Allah no Comando.

from random import *
from tkinter import *
import tkinter.ttk as ttk
from tk_tools.tooltips import ToolTip
from tkinter.messagebox import *
from tkinter.scrolledlist import ScrolledList


class J3A7P6:
    """
    Type: PythonSource
    Name: Game Guessing Word
    Modified: 18/04/2020 10:00pm
    Created: 31/03/2020 07:00am
    Version: 0.1-042020 - 0.2-042020 - 0.3-042020 - 0.4-012021
    Autor: Nurul GC - https://artesgc.home.blog
    cor: (2)MistyRose1, (1)#d513bc
    """

    def __init__(self):
        self.gc_ = None
        self.janela = None
        self.gc = Tk()
        # self.gc.iconbitmap(default='./img/adivinhapalavra_gc.ico')
        self.gc.title('  🙋')
        self.gc.resizable(0, 0)

        #
        self.ft = PhotoImage(file='./img/02.png')
        self.ft2 = PhotoImage(file='./img/04.png')
        self.nome = StringVar()
        self.nivel = IntVar()
        self.n_tentativas = IntVar()
        self.rodada = IntVar()
        self.pontos = IntVar()
        self.chute = StringVar()

        #
        self.menu = Menu(self.gc)
        self.tab = ttk.Notebook(self.gc)
        self.tab.pack(expand=1, fill='both')
        self.jogo()

    def jogo(self):

        def en():
            showinfo("Caution", "For a better gaming experience read the instructions in the options menu. \nThanks for your support! - ArtesGC")
            palavra_ = ['ACCESSIBLE', 'ACCOMMODATING', 'ACCOMPLISHED', 'ADMIRABLE', 'ADONISAFORTUNATE', 'ADVENTURE', 'AFFECTIVE', 'AIRY', 'ALLOWABLE', 'ALTRUIST', 'AMAZING', 'ANGELIC', 'ANIMATED',
            'APPLIED', 'ASSERTIVE', 'ASTUTE', 'ATTENTION', 'ATTENTIOUS', 'ATTRACTIVE', 'AUSPICIOUS', 'AUTHENTIC', 'AVAILABLE', 'AWARE', 'AWESOME', 'BALANCED', 'BASED', 'BEAUTIFUL', 'BEAUTY',
            'BEHAVIOR', 'BENEFACTOR', 'BENEFICIAL', 'BENEVOLENT', 'BENIGN', 'BEST', 'BIG', 'BLESSED', 'BOLD', 'BOMBASTIC', 'BRILLIANT', 'BRINGING', 'BRIOUS', 'CALM', 'CANDIDATE', 'CAPABLE',
            'CAPTIVATING', 'CAREER', 'CAREFUL', 'CARETAKER', 'CAT', 'CAUTIOUS', 'CENTERED', 'CHARISMATIC', 'CHARITABLE', 'CHARMING', 'CHIC', 'CIRCUMSPECT', 'CIVIC', 'CIVIL',
            'CIVILIZED', 'CLAIRVOYANT', 'CLEMENT', 'CLEVER', 'COHERENT', 'COLLABORATOR', 'COLLEAGUE', 'COMEDY', 'COMMENDABLE', 'COMMITTED', 'COMPACENT', 'COMPANION', 'COMPASSIONATE', 'COMPETENT',
            'CONFIDENT', 'CONSCIOUS', 'CONVICTED', 'COOL', 'COOPERATOR', 'CORDIAL', 'CORRECT', 'COURAGEOUS', 'CREATIVE', 'CREDIBLE', 'CRITERIOUS', 'CRIVEL', 'CULT', 'CUTE', 'CUTS', 'DECENT',
            'DECIDED', 'DEDICATED', 'DELICATE', 'DESIRAVELABLE', 'DEVELOPED', 'DEVOTEE', 'DILIGENT', 'DIPLOMATIC', 'DIRECT', 'DISCIPLINED', 'DISCREET', 'DISTINCT', 'DOCILE', 'DREAMER', 'DREAMLIKE',
            'DRESSY', 'DYNAMIC', 'EDUCATED', 'EFFECTIVE', 'EFFICIENT', 'ELEGANT', 'ELOCQUENT', 'EMANCIPATED', 'EMINENT', 'EMPATHIC', 'EMPHASIZED', 'ENCHANTING', 'ENCOURAGING', 'ENTHUSIASMED',
            'ENTHUSIAST', 'ENTREPRENEUR', 'ENVOLVED', 'ETERNAL', 'EXAMPLE', 'EXCELLENT', 'EXCITED', 'EXPERIENT', 'EXPERT', 'EXTRAORDINARY', 'EXTREME', 'EXTROVERTED', 'EXUBERANT', 'EXULTANT',
            'FABULOUS', 'FAIR', 'FAITHFUL', 'FANTASTIC', 'FASCINATING', 'FAST', 'FEARLESS', 'FELLOW', 'FERVOROUS', 'FIGHTER', 'FIRM', 'FIT', 'FLATTERING', 'FORMIDABLE', 'FRANC', 'FREE', 'FREEDOM',
            'FRIEND', 'FRIENDLY', 'FRONT', 'FUN', 'FUNNY', 'GALANTE', 'GENEROUS', 'GENIAL', 'GENIUS', 'GENTILE', 'GENTLEMAN', 'GENUINE', 'GIANT', 'GIFTED', 'GIVEN-AWAY', 'GLAMOROUS',
            'GLAZING', 'GLORIOUS', 'GLOSSY', 'GOD', 'GOOD', 'GRACEFUL', 'GRATEFUL', 'GREAT', 'GREEN', 'GROWED', 'HANDSOME', 'HAPPY', 'HARD-WORKER', 'HEALTHY', 'HEAVENLY', 'HELPFUL', 'HERO',
            'HEROIC', 'HILARIOUS', 'HOLY', 'HONEST', 'HONORABLE', 'HONORED', 'HOOKER', 'HOPEY', 'HOSPITABLE', 'HOST', 'HOT', 'HUGE', 'HUMAN', 'HUMANITARY', 'HUMBLE', 'HUMOROUS', 'IDEAL',
            'ILLUSTRIOUS', 'IMAGINATIVE', 'IMMACULATE', 'IMMORTAL', 'IMPARENT', 'IMPAVITED', 'IMPECCABLE', 'IMPELLABLE', 'IMPONENT', 'IMPORTANT', 'IMPRESSIVE', 'INCORRUPT',
            'INCORRUPTIBLE', 'INCREDIBLE', 'INDEPENDENT', 'INDISPENSABLE', 'INEQUALABLE', 'INGENIOUS', 'INSPIRING', 'INSTRUCTED', 'INSUBORNABLE', 'INTACT', 'INTELECTUAL', 'INTELLIGENT', 'INTENSE',
            'INTERESTING', 'INTERVENTIVE', 'INTUITIVE', 'INVINCIBLE', 'IRRESISTIBLE', 'IRREVERENT', 'JEWELRY', 'JOYFUL', 'JUBILANT', 'KIND', 'KINDNESS', 'KNOWLEDGE',
            'LABORIOUS', 'LARGE', 'LAUDABLE', 'LAWFUL', 'LEADER', 'LIBERAL', 'LIKEABLE', 'LITERATE', 'LIVE', 'LOVELY', 'LOVING', 'MAESTRAL', 'MAGIC', 'MAGNANIMOUS', 'MAGNIFICENT',
            'MAJESTIC', 'MANLY', 'MASTERFUL', 'MATERNAL', 'MATURE', 'MAXIMUM', 'MELLOWY', 'MEMORABLE', 'MERITORIOUS', 'METICULOUS', 'METODIC', 'MINE', 'MINUTIOUS', 'MODERATE',
            'MODERATE', 'MODERN', 'MODEST', 'MOTIVATED', 'NATURAL', 'NATURIST', 'NEW', 'NICE', 'NOBLE', 'NORMAL', 'NUTRID', 'OBEDIENT', 'OBJECTIVE', 'OBSEQUISION', 'OBSERVATOR', 'OBSTINATED', 'ODD',
            'OFFICIOUS', 'OMNIPOTENT', 'OMNISCIENT', 'OPEN', 'OPERANT', 'OPPORTUNE', 'OPTIMIST', 'ORDER', 'ORGANIZED', 'ORIGINAL', 'PACIFIC', 'PARCIMONIOUS', 'PARTNER', 'PATIENT',
            'PEACEMAKER', 'PERFECT', 'PERSEVERANT', 'PERSPECTIVE', 'PERTINACIOUS', 'PHENOMENAL', 'PIONEER', 'PIOUS', 'PLAYFUL', 'PLEASANT', 'POLISHED', 'PONTUAL', 'POWERFUL', 'PRESTIGIOUS', 'PRETTY',
            'PREVENTED', 'PRIMOROUS', 'PRINCE', 'PRODIGY', 'PRODUCT', 'PROMINENT', 'PROTECTOR', 'PRUDENT', 'PUNISHER', 'PURE', 'QUALIFIED', 'QUIET', 'RADIANT', 'RATIONAL', 'READY', 'REALISTIC',
            'REASONABLE', 'RECEPTIVE', 'RECOGNIZED', 'REFINED', 'REFLECTED', 'RELAXED', 'RELIABLE', 'REMARKABLE', 'RENOMATED', 'RESILIENT', 'RESISTANT', 'RESOLUTED', 'RESOLVED', 'RESPECTED',
            'RESPECTFUL', 'RESPECTIVE', 'RESPLANDING', 'RESPONSIBLE', 'ROBUST', 'ROMANTIC', 'SAFE', 'SAPIENT', 'SCARULOSOUS', 'SEDUCTIVE', 'SENSATE', 'SENSATIONAL', 'SENSITIVE', 'SENTIMENTAL',
            'SERENE', 'SERIOUS', 'SERVICEABLE', 'SHIVERING', 'SINCERE', 'SINGLE', 'SKILLED', 'SKILLFUL', 'SKULL', 'SLENDER', 'SMELLY', 'SMILEY', 'SMILING', 'SOCIABLE', 'SOLICITOUS', 'SOLIDARY',
            'SOPHISTICATED', 'SPECIAL', 'SPECIALIST', 'SPECTACULAR', 'SPIRITUOUS', 'SPLENDID', 'SPLENDOROUS', 'SPONTANEOUS', 'STRAIGHT', 'STRONG', 'STUNNING', 'SUBLIME', 'SUBTLE', 'SUIT', 'SUITABLE',
            'SWEET', 'TALENTED', 'TEMPERANT', 'TENDER', 'TIRELESS', 'TITANIC', 'TOLERABLE', 'TOLERANT', 'TOUCHING', 'TRANQUILIZANT', 'TRANSCENDENT', 'TRANSCENDENTAL', 'TRANSIGENT', 'TRANSPARENT',
            'TRAQUESTED', 'TREATABLE ', 'TRIUMPHAL', 'TRIUMPHANT', 'TRUE', 'TRUSTWORTHY', 'TRUTHFUL', 'ULTRACORRECT', 'ULTRADIVINE', 'ULTRAFANTASTIC', 'ULTRAINDEPENDENT', 'ULTRAMODERN',
            'ULTRANATURAL', 'ULTRARRATIONAL', 'UNABALABLE', 'UNBEATABLE', 'UNDERSTANDING', 'UNEMPLOYED', 'UNIFIER', 'UNIQUE', 'UNO', 'UNSTOPABLE', 'UNSUBMITTED', 'URBAN',
            'VALENTOUS', 'VALIANT', 'VALID', 'VALUABLE', 'VANGUARDIST', 'VEHEMENT', 'VELOZ', 'VENERABLE', 'VENERATED', 'VENTUROUS', 'VERACIOUS', 'VERBOSE', 'VERSED', 'VERTIGINOUS', 'VIBRANT',
            'VICTORIOUS', 'VIGILANT', 'VIGOROUS', 'VIRTUOUS', 'VIRYL', 'VISIONARY', 'VITAL', 'VIVACIOUS', 'VIVID', 'VULTURE', 'WANTED', 'WARM', 'WARRIOR', 'WAVERING', 'WEIGHTED',
            'WINNER', 'WISE', 'WITTY', 'WONDERFUL', 'WORKER', 'WORTHY', 'YOUNG', 'YUMMY', 'ZEALOUS']

            #
            def palavra_secreta():
                self.janela = LabelFrame(self.tab)
                self.janela.configure(padx=15, pady=15, bg='MistyRose1')
                self.tab.add(self.janela, text='Hidden Words', underline=7)
                self.tab.select(self.janela)

                lst = ScrolledList(self.janela)
                lst.pack(side='left', expand=1, fill='both')

                for p in sorted(palavra_):
                    lst.insert(END, p)

                Button(self.janela, text='Close', command=self.janela.destroy, bg='red', fg='black').pack(anchor=SE)

            def palavra_secreta_():
                if self.janela is None:
                    return palavra_secreta()
                try:
                    self.tab.select(self.janela)
                except TclError:
                    return palavra_secreta()

            def instr():
                showinfo('Instructions', """
Hello May the peace and blessings of God be upon you and your entire family..
This game consists of earning the maximum points possible
in a few attempts, guessing which word has been defined (LETTER BY LETTER)..

For a better game experience:
    count how many letters have the
    supposed word identified by the symbols '_' 
    (refer to the letters of the word)
    and use the list of words that are hidden
    in the options menu (Secret Words)..
    Use them as a reference for your attempts!

May God Enlighten You In This Adventure..

Tip:
Living Rules;
""")

            def hello():
                showinfo('About', '''
Name: Game Guessing Word
Version: 0.4-012021
Designer & Programmer: Nurul GC
Company: ArtesGC, Inc.
''')

            def en_():
                if self.root is None:
                    return en()
                try:
                    self.tab.select(self.root)
                except TclError:
                    self.gc_.destroy()
                    return en()

            def jogo_level():
                if self.nivel.get() == 3:
                    self.n_tentativas.set(15)
                    self.pontos.set(0)
                    jogo()
                elif self.nivel.get() == 2:
                    self.n_tentativas.set(20)
                    self.pontos.set(0)
                    jogo()
                elif self.nivel.get() == 1:
                    self.n_tentativas.set(25)
                    self.pontos.set(0)
                    jogo()
                else:
                    showerror('Error!', 'Level Do Not Available..')

            def jogo():
                self.root.destroy()
                self.gc_ = LabelFrame(self.tab)
                self.tab.add(self.gc_, text='Guessing Word', underline=9)
                self.tab.select(self.gc_)
                self.gc_.configure(padx=25, pady=5, bg='MistyRose1')

                #
                self.rodada.set(0)
                palavra_l = len(palavra_)
                palavra = palavra_[randrange(palavra_l)]
                letra = ['_' for ltra in palavra]

                #
                def confirma(p):
                    self.rodada.set(abs(self.rodada.get() + 1))
                    posicao = 0

                    def novo():
                        self.gc_.destroy()
                        jogo()

                    #
                    if self.chute.get().upper() in palavra:
                        for ltra in palavra:
                            if self.chute.get().upper() == ltra:
                                self.pontos.set(abs(self.pontos.get() + 100))
                                letra[posicao] = self.chute.get().upper()
                                lr.configure(text=f'''Level: {self.nivel.get()} Attempt: {self.rodada.get()} of {self.n_tentativas.get()}

(^.^) Yeahii..
YOU ARE RIGHT {self.nome.get()}!
{letra}
Points {self.pontos.get()}''', fg='blue')
                            posicao += 1
                    else:
                        self.pontos.set(abs(self.pontos.get() - 50))
                        lr.configure(text=f'''Level: {self.nivel.get()} Attempt: {self.rodada.get()} of {self.n_tentativas.get()}

(O_O) Upss..
YOU ARE WRONG {self.nome.get()}!
Points {self.pontos.get()}''', fg='red')
                    #
                    acertou = '_' not in letra
                    if acertou:
                        lr.configure(text=f"""(^3^) Congratulations {self.nome.get()}
YOU WON..
{letra}

• Score
Level: {self.nivel.get()}
Attempt: {self.rodada.get()} of {self.n_tentativas.get()}
Points: {self.pontos.get()}""", fg='green')
                        b.configure(text='Play Again', command=novo, bg='blue', fg='white')
                        b2.grid(row=5, column=2, sticky=W)
                    elif self.rodada.get() == self.n_tentativas.get():
                        lr.configure(text=f"""(T.T) AM SORRY {self.nome.get()}
YOU HAVE EXHAUSTED ALL ATTEMPTS..
Hidden Word: {palavra}

• Score
Level: {self.nivel.get()}
Attempt: {self.rodada.get()} of {self.n_tentativas.get()}
Points: {self.pontos.get()}""", fg='red')
                        b.configure(text='Play Again', command=novo, bg='blue', fg='white')
                        b2.grid(row=5, column=2, sticky=W)

                #
                Label(self.gc_, text='🙇    🙈🙊    🤷    👀    🤓    😂', bg='MistyRose1', font='consolas 16').grid(row=0, columnspan=1)
                f_jogo = LabelFrame(self.gc_, text='P L A Y I N G', fg='#d513bc', font='consolas 10 bold', bg='MistyRose1', relief='groove')
                f_jogo.grid(row=1, column=0, pady=10)
                #
                Label(f_jogo, text=f'Hello {self.nome.get()} Try to Guess What Is the Secret Word\n{letra}', font='consolas 10 bold', bg='MistyRose1').grid(row=0, columnspan=3)
                Label(f_jogo, text='__________________________________________________\n', bg='MistyRose1').grid(row=1, columnspan=3)
                lr = Label(f_jogo, text='.  .  .  .  .', font='Consolas 10 bold', bg='white')
                lr.grid(row=2, columnspan=3)
                Label(f_jogo, text='__________________________________________________', bg='MistyRose1').grid(row=3, columnspan=3)

                Label(f_jogo, text='Enter the Letter', bg='MistyRose1', font='consolas 10 bold', underline=9).grid(row=4, column=0)
                e = ttk.Entry(f_jogo, textvariable=self.chute)
                e.grid(row=4, column=1, sticky=W)
                e.bind("<Return>", confirma)

                b = Button(f_jogo, text='Check', bg='cyan')
                b.grid(row=4, column=2, sticky=W)
                b.bind("<Button-1>", confirma)
                b2 = Button(f_jogo, text='End Game', command=self.gc.destroy, bg='red')

            #
            self.tab1.destroy()
            self.root = LabelFrame(self.tab)
            self.tab.add(self.root, text='Peace And Blessings of God be Upon You')
            self.tab.select(self.root)
            self.root.configure(padx=30, pady=15, bg='MistyRose1')
            self.gc.title('Guessing Word')

            #
            menu_pt = Menu(self.menu, tearoff=0, bg='MistyRose1', font='tahoma 8')
            menu_pt.add_command(label='New Game', command=en_, underline=4)
            menu_pt.add_command(label='Instructions', command=instr, underline=0)
            menu_pt.add_command(label='Secret Word', command=palavra_secreta_, underline=7)
            menu_pt.add_separator()
            menu_pt.add_command(label='Exit', command=self.gc.destroy, underline=0)
            detalhes = Menu(self.menu)
            detalhes.add_cascade(label='Options', menu=menu_pt, underline=0)
            detalhes.add_command(label='About', command=hello, underline=0)
            self.gc.configure(menu=detalhes)

            #
            l1 = Label(self.root, image=self.ft2, bg='#d513bc')
            l1.grid(row=0, column=0)

            f1 = LabelFrame(self.root, text='G A M E R', fg='#d513bc', font='consolas 8 bold', bg='MistyRose1')
            f1.grid(row=1, column=0, pady=10)
            Label(f1, text='Type Your Name', underline=10, font='consolas 10 bold', bg='MistyRose1').grid(row=0, column=0)
            enm = Entry(f1, textvar=self.nome, bd=2)
            enm.grid(row=0, column=1)

            Label(f1, text='Choose Your Level', underline=12, font='consolas 10 bold', bg='MistyRose1').grid(row=1, column=0)
            vl = [1, 2, 3]
            e1_ = ttk.Combobox(f1, textvariable=self.nivel, values=vl, width=17)
            e1_.grid(row=1, column=1)
            ToolTip(e1_, 'Level 1 - 25 attempts\nLevel 2 - 20 attempts\nLevel 3 - 15 attempts')

            Button(f1, text='Play', command=jogo_level, bg='cyan').grid(row=2, column=1, sticky=E)
            enm.focus()

        #
        self.tab1 = LabelFrame(self.tab)
        self.tab.add(self.tab1, text='Welcome')
        self.tab.select(self.tab1)
        self.tab1.configure(padx=30, pady=10, bg='MistyRose1')
        #
        Label(self.tab1, text="💻 GUESSING WORD 💻", font='Consolas 12 bold', fg='#d513bc', bg='MistyRose1').grid(row=0, column=0)
        Label(self.tab1, image=self.ft, bg='#d513bc').grid(row=1, column=0, pady=10)
        f = LabelFrame(self.tab1, bg='MistyRose1', )
        f.grid(row=2, column=0)
        Radiobutton(f, text='START ', font='arial 7 bold', command=en, indicatoron=False).grid(row=0, column=0, padx=5, pady=5)


if __name__ == '__main__':
    app = J3A7P6()
    app.gc.mainloop()
