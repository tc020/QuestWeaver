#Du hast die Rolle als Spielleiter in der Fanatsiewelt Aventurien aus dem Rollenspielsystem Das Schwarze Auge. Beschreibe eine Taverne mit einem Wirt und mindestens 3 Gästen. Beschreibe jede Figur in 5 Stichpunkten und gebe jeder Figur einen Hintergrund. Gebe mindestens zwei Figuren einen Plot, an den die Helden anknüpfen können, wenn sie sie ansprechen.

#Beschreibe den Plot von Gast 1 detaillierter und füge Elemente hinzu, die für die Helden eine Herausforderung darstellen. 

#Beschreibe Punkt 6 detaillierter und gebe konkrete Beispiele für die Rätsel.

#Modifiziere deine Antwort mit mehr Gefahr und Dark Fantasy Elementen

#Gebe weitere Möglichkeiten mit denen die Helden bei Morwenna auf weitere Abenteuer gehen könnten.

#QuestWeaver

from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
import ast
import os
import openai


from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

llm_model = "gpt-4o-mini"


def get_completion(prompt, model=llm_model):
    messages = [{"role": "system", "content": prompt}] #messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message["content"]



# --------------- Szenario konfigurieren -----------------------

def ort_erzeugen(typ, gross, zustand):
    # Hier kommt der Code für das Skript
    print("Das Skript wird ausgeführt.")
    print("Typ:", typ)
    print("Größe:", gross)
    print("Zustand:", zustand)

    anweisung1 = """
    Du hast die Rolle als Spielleiter in der Fanatsiewelt Aventurien aus dem Rollenspielsystem Das Schwarze Auge. 
    """ #Rollenspielsystem eigentlich egal. Austesten ob das Auswirkungen auf die Quests hat

    anweisung2 = f"""
    Beschreibe eine {typ} mit mindestens drei (ausser wenn {gross} = klein, dann nur 1) wichtigen Gebäuden die regelmäßig von Abenteurern aufgesucht werden. 
    Die Ortschaft ist in einem {zustand} Zustand. 
    
    Gebe deine Antwort als Python Dictionary zurück. Ausgabe ohne Einleitung, ohne Erläuterung, nur Code. Ohne die Einleitung "```python" und den Abschluss "```".
    
    Trage folgende Keys mit den dazugehörigen Values nach dem Doppelpunkt ein:

    "Name": Name der Ortschaft.
    "Zustand": Zustand der Ortschaft.
    "Anzahl der Wirtshäuser": Anzahl der Wirtshäuser.
    "Wirtshäuser": Eine Liste der Namen der Wirtshäuser.
    "Besonderen Orte": Eine Liste der besonderen Orte, die wiederum den Namen und eine kurze Bescjreibung enthalten.
    "Besondere Personen": Eine Liste der besonderen Personen mit ihren Namen, ihrer Rolle, eine kurze Beschreibung und an welchen besonderen Orten diese anzutreffen sind.
    """

    antwort = get_completion(anweisung2)

    return(antwort)


typ = "Dorf"
gross = "Klein"
zustand = "Niedergang"
ort_obj = ort_erzeugen(typ, gross, zustand)
ort_info = ast.literal_eval(ort_obj)
print("########################################")
print(type(ort_info))
print("------------1")
print(ort_info)
print("------------2")
ort_name = ort_info["Name"]
ort_zustand = ort_info["Zustand"]
print("Der Ortname lautet:",ort_name,"und befindet sich in folgendem Zustand:",ort_zustand)


