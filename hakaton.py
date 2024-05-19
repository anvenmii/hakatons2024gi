encoding='utf-8'

print("Prieks tevi redzēt mūsu beta projektā! Lūdzu, reģistrējieties, lai turpinātu.")

usernamess = []

def uservards(username):
    usernamess.append(username)
    print(f"User {username} registered successfully!")

username = input("Enter your username: ")
uservards(username)
print("Hi, " + username)
sajuta = input("Kā tevi iet? Man iet: ")
if sajuta.lower() == "labi" or sajuta.lower() == "izcili":
    print('Prieks to dzirdēt')
else:
    print('Ceru, ka viss būs kārtībā')

class Zagadki:
    def __init__(self, question, pareizi):
        self.question = question
        self.pareizi = pareizi
        self.user_answer = None

    def asking(self):
        print(self.question)
        self.user_answer = input("Atbilde: ")
        if self.user_answer.lower() == self.pareizi.lower():
            print("Pareizi!")
            return True
        else:
            print("Nepareizi. Pareizā atbilde ir:", self.pareizi)
            return False


tautas_mīkla = [
    ("Ausis ir, galvas nav.", "Spainis"),
    ("Koka kāja, dzelzs galva. ", "Circis"),
    ("Zaļas malas, melns viducis ", "Ceļš un ceļmala"),
    ("Zelta puķe krāsnī zied. ", "Uguns"),
    ("Dzīvs neiet, nomiris iet.  ", "Laiva"),
    ("Jo vairāk ēd, jo vairāk atliek. ", "Rieksts"),
    ("Balta gala, dzeltena āda. ", "Sīpols"),
    ("Balta zoss, zaļi spārni.  ", "Bērzs"),
    ("Miesu aped, sirdi aizsviež.  ", "Ķiršu oga"),
    ("Viens stāv, divi simti karājas.  ", "Ābele un āboli"),
    ("Mežā un mājā vienā vārdā.  ", "Ieva"),
    ("Citam kalpo, pats sevi tērē. ", "Svece"),
    ("Siers jūras dibenā.  ", "Saule"),
    ("Brīžam jauns, brīžam vecs.  ", "Mēness")
]

def start_miklasgame():
    for idx, (question, answer) in enumerate(tautas_mīkla, start=1):
        print(f"tautas_mīkla {idx}:")
        zagadka = Zagadki(question, answer)
        zagadka.asking()

class MultipleChoice:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.prompt)
        for idx, option in enumerate(self.options, start=1):
            print(f"{idx}. {option}")

    def parbaude(self, atbildeliet):
        return self.options[atbildeliet - 1] == self.correct_answer

def run_quiz(questions):
    score = 0
    for question in questions:
        question.display_question()
        user_answer = int(input("Tava atbilde: "))  
        if question.parbaude(user_answer):
            print("Pareizi!")
            score += 1
        else:
            print("Nepareizi! ")
        
    print(f" Tu atbildēji pareizi uz {score} no {len(questions)} jautājumiem.")
    if score == 10:  
        print("Izcili ;3 ")
    else:
        print("Studying is cool")


question1 = MultipleChoice("How to say 'Hi' in Latvian?", ["Lapsa", "Ata", "Sveiki"], "Sveiki")
question2 = MultipleChoice("How to say 'Thanks' in Latvian?", ["Lūdzu", "Paldies", "Kaķis"], "Paldies")
question3 = MultipleChoice("How to say 'Fox' in Latvian?", ["Lapsa", "Galds", "Putns"], "Lapsa")
question4 = MultipleChoice("How to say 'Water' in Latvian?", ["Gaisma", "Koks", "Ūdens"], "Ūdens")
question5 = MultipleChoice("How to say 'Sun' in Latvian?", ["Paldies", "Zvaigzne", "Saule"], "Saule")
question6 = MultipleChoice("How to say 'Table' in Latvian?", ["Krēsls", "Dators", "Galds"], "Galds")
question7 = MultipleChoice("How to say 'Flower' in Latvian?", ["Flower", "Fruit", "Tree"], "Puķe")
question8 = MultipleChoice("How to say 'Bird' in Latvian?", ["Saule", "Suns", "Putns"], "Putns")
question9 = MultipleChoice("How to say 'House' in Latvian?", ["Ēka", "Ceļš", "Māja"], "Māja")
question10 = MultipleChoice("How to say 'Tree' in Latvian?", ["Akmens", "Koks", "Metāls"], "Koks")

questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]

while True:
    print(username + ", Šodien mēs varam piedāvāt tev nokārtot Multichoise (ievadi '1')")
    print("Mīklas(2)")
    print('Tomēr, ja vēlies iziet (3) ')
    start_game_panelka = input('Jūsu izvēle (ievadiet numuru): ')
    if start_game_panelka == '1':
        print('Forši🌎')
        run_quiz(questions)
    
    if start_game_panelka == '2':
        print('Forši🧩')
        start_miklasgame()
        
    elif start_game_panelka == '3':
        print("Atā!")
        break
    else:
        print('Nesaprotu')
