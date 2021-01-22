import random
from flask import Flask, request

app = Flask(__name__)


nombre_de_vie = 0
nombre_aletoire_choisi = random.randint(1, 100)
print(nombre_aletoire_choisi)
list_tentative_done = []


import datetime
now = datetime.datetime.now()
print ("La date courante est : ")
print (now.strftime("%A %d/%m/%Y %H:%M:%S"))





def render(string_validite: str):
    html = f"<html>" \
           f"<body>" \
           f"<p><FONT color='#ff0000' size='6'>❤ ️</FONT><FONT size='6'>  = {nombre_de_vie} ️</FONT></p>" \
           "<p><FONT size='6'> _______________________</FONT></p>" \
           f"<p><FONT size='6'>  nombre essayé :</FONT></p>" \
           f"<p><FONT size='6'>  {string_validite} </FONT></p>"
    if len(list_tentative_done) == 0:
        html += f"<p> liste vide </p>"
    else:
        html += f"<ul>"
        for i in list_tentative_done:
            html += f"<li><FONT size='6'> {i} </FONT></li>"
        html += f"</ul>"
    html += "<p><FONT size='6'> _______________________</FONT></p>" \
            f"<p><FONT size='6'> ↓ essayer de nouveau ↓ </FONT></p>" \
            f"<form action='/submit' method='get'><input type= 'number' id= 'tentacles'  name= 'tentacles'  min= {1}  max= {100}>" \
            f"<input class= 'favorite styled' type='submit' value='essayer'></form>   " \
            f"<style type='text/css'>" \
            ".styled {" \
            "border: 0;"\
            "line-height: 2.5;"\
            "padding: -1.5 20px;"\
            "font-size: 1.5rem;"\
            "text-align: center;"\
            "color: #fff;"\
            "text-shadow: 1px 1px 1px #000;"\
            "border-radius: 15px;"\
            "background-color: #1EA4E5;"\
            "background-image: linear-gradient(to top left,"\
                                                     " rgba(0, 0, 0, .2),"\
                                                     "rgba(0, 0, 0, .2) 30%,"\
                                                     "rgba(0, 0, 0, 0));"\
            "box-shadow: inset 2px 2px 3px rgba(255, 255, 255, .6),"\
                "inset -2px -2px 3px rgba(0, 0, 0, .6);"\
            "}"\
            ".styled:hover {"\
            "background-color: #1D81B2;"\
            "}"\
            ".styled:active {"\
            "box-shadow: inset -2px -2px 3px rgba(255, 255, 255, .6),"\
                "inset 2px 2px 3px rgba(0, 0, 0, .6);"\
            "}"\
            f"</style>" \
            f"<form action='/relance' method='get'>" \
            f"<input type='submit' class= 'favorite styled' value='relancer'>" \
            f"</div>" \
            f"</form>" \
            f"<form action='/life' method='get'>" \
            f"<input type='submit' class= 'favorite styled' value='activer 10 ❤'>" \
            f"</div>" \
            f"</form>" \
            f"<p><FONT size='1'> {now} </FONT></p>" \
            f"</body>" \
            f"</html>"
    return html

@app.route('/life')
def life():
    global nombre_de_vie
    empty_array = []
    nombre_de_vie = 10
    return render(empty_array)


def reinitialiser():
    global nombre_aletoire_choisi, list_tentative_done, nombre_de_vie
    nombre_aletoire_choisi = random.randint(1, 100)
    list_tentative_done = []
    nombre_de_vie = 0



@app.route('/relance')
def relance():
    reinitialiser()
    empty_array = []
    return render(empty_array)


@app.route('/')
def init():
    empty_array = []
    return render(empty_array)


def calcul_validite(chiffre_propose: int, nombre_de_vie: int):
    string_retour_methode = ""

    if nombre_aletoire_choisi < chiffre_propose:
        string_retour_methode = 'trop grand 🔺'
    elif nombre_aletoire_choisi > chiffre_propose:
        string_retour_methode = 'trop petit 🔻'
    elif nombre_aletoire_choisi == chiffre_propose:
        string_retour_methode = "Gagné 👍"
    else:
        raise ArithmeticError
    return string_retour_methode

nombre_de_vie == 0




@app.route('/submit')
def submit():
    global nombre_de_vie

    if request.args.get("tentacles") == None or request.args.get("tentacles") == '':
        error = "il y a une erreur"
        return render(error)
    else:
        argument_tentative_propose = int(request.args.get("tentacles"))

    element_trouve_dans_la_liste = False
    for t in list_tentative_done:
        if not element_trouve_dans_la_liste:
            if t == argument_tentative_propose:
                element_trouve_dans_la_liste = True

    if not element_trouve_dans_la_liste:
        list_tentative_done.append(argument_tentative_propose)

    nombre_de_vie -= 1

    if element_trouve_dans_la_liste == True:
        string_validite = "⚠️ deja demandé ⚠️"
    else:
        string_validite = calcul_validite(argument_tentative_propose, nombre_de_vie)

    if nombre_de_vie == 0:
        string_validite = "perdu !"
        reinitialiser()

    else:
        pass
    return render(string_validite)




# print(request.args)
# age = request.args.get("age")
# return f"Bonjour {name} vous avez {age} ans"

app.run(host="localhost", port=8080)
