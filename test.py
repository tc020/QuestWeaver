#Du hast die Rolle als Spielleiter in der Fanatsiewelt Aventurien aus dem Rollenspielsystem Das Schwarze Auge. Beschreibe eine Taverne mit einem Wirt und mindestens 3 Gästen. Beschreibe jede Figur in 5 Stichpunkten und gebe jeder Figur einen Hintergrund. Gebe mindestens zwei Figuren einen Plot, an den die Helden anknüpfen können, wenn sie sie ansprechen.

#Beschreibe den Plot von Gast 1 detaillierter und füge Elemente hinzu, die für die Helden eine Herausforderung darstellen. 

#Beschreibe Punkt 6 detaillierter und gebe konkrete Beispiele für die Rätsel.

#Modifiziere deine Antwort mit mehr Gefahr und Dark Fantasy Elementen

#Gebe weitere Möglichkeiten mit denen die Helden bei Morwenna auf weitere Abenteuer gehen könnten.

from langchain.output_parsers import ResponseSchema
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
import datetime
import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

llm_model = "gpt-4o-mini"


def get_completion(prompt, model=llm_model):
    messages = [{"role": "user", "content": prompt}] #messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message["content"]


# --------------- Szenario festlegen -----------------------

print("1. Wald")
print("2. Stadt")
print("3. Wald")
print("4. Sumpf")

szenario = input("Wähle ein Szenario (1-4) aus oder lege selbst eins fest: ")

anzahlGast = 3

anweisung1 = """
Du hast die Rolle als Spielleiter in der Fanatsiewelt Aventurien aus dem Rollenspielsystem Das Schwarze Auge.
"""

anweisung2 = f"""{anweisung1}
Beschreibe einen {szenario} mit einem Wirt und mindestens {anzahlGast} Gästen. Beschreibe jede Figur in 5 Stichpunkten und gebe jeder Figur einen Hintergrund. Gebe mindestens zwei Figuren einen Plot, an den die Helden anknüpfen können, wenn sie sie ansprechen.
"""
antwort ="Platzhalter"
#antwort = get_completion(anweisung2)

print(szenario)

#witz = get_completion(prompt1)

#print(witz)
