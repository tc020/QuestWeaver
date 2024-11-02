import os
import openai
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseModel, Field
import json

# Lade API-Schlüssel aus der .env-Datei
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

# LLM-Modell festlegen
llm_model = "gpt-4o-mini"

# Definiere die erwartete strukturierte Ausgabe mit Pydantic
class Ortschaft(BaseModel):
    name: str = Field(description="Name der Ortschaft")
    beschreibung_des_ortes: str = Field(description="Gesamtbild und Zustand der Ortschaft.")
    bevölkerung_und_gesellschaft: str = Field(description="Beschreibung der sozialen Strukturen der dort lebenden Menschen.")
    gerüchte_und_legenden: str = Field(description="Eine Möglichkeit für einen Plot bzw. eine Quest für die Helden.")
    quests_und_interaktionsmöglichkeiten: str = Field(description="Eine Möglichkeit für Quests unter Berücksichtugung des Gesamtbildes mit einer Belohnung in Form von: Ideele Werten oder Dienstleistungen.")
    gefahren_und_bedrohungen: str = Field(description="Eine Bedrohung unter denen die Menschen leiden und von denen sie befreit werden möchten.")
    anzahl_der_wirtshäuser: int = Field(description="Anzahl der Wirtshäuser.")
    wirtshäuser: list = Field(description="Eine Liste der Namen der Wirtshäuser.")
    besonderen_orte: list = Field(description="Eine Liste der besonderen Orte, die wiederum den Namen, den Orts-Typ und eine kurze Beschreibung enthalten.")
    besondere_personen: list = Field(description="Eine Liste der besonderen Personen mit ihren Namen, ihrer Rolle, eine kurze Beschreibung, einen Plotansatz und an welchen besonderen Orten diese anzutreffen sind.")
    bemerkung: str = Field(description="Ort von Co-Meister erzeugt.")

# Funktion zur Verarbeitung des Prompts und zur Rückgabe der strukturierten Ausgabe
def get_completion(prompt, model=llm_model):
    messages = [{"role": "system", "content": prompt}]
    
    # Anfrage an das OpenAI-Modell senden
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
    )
    
    # Extrahiere die Antwort
    response_with_backticks = response.choices[0].message["content"]

    # Versuche die Antwort als JSON zu parsen
    try:
        # Entferne die Backticks und "json"
        #print("Unbearbeitet:",response_with_backticks)
        #clean_response = response_with_backticks.strip('```json').strip('```')
        parsed_output = json.loads(response_with_backticks)
        print("Typ:",type(parsed_output))
        print("Ausgabe vor Joke",parsed_output)
        # Validiere die strukturierte Ausgabe mit Pydantic
        ortschaft = Ortschaft(**parsed_output)
        print("Ausgabe nach Joke:",ortschaft)
        print(type(ortschaft))
        return ortschaft
    except json.JSONDecodeError:
        return f"Fehler beim Parsen der Antwort: {response_with_backticks}"
    except ValueError as e:
        return f"Validierungsfehler: {e}"

#################################################################################################################################################################

def ort_erzeugen(typ, gross, zustand):
    # Hier kommt der Code für das Skript
    print("Das Skript wird ausgeführt.")
    print("Typ:", typ)
    print("Größe:", gross)
    print("Zustand:", zustand)

    if gross == "Klein":
        gebäude = 1
    if gross == "Mittel":
        gebäude = 2
    if gross == "Groß":
        gebäude = 3

    if zustand == "Blühend":
        bild = "Blühende Ortschaft mit motivierten, positiven und sehr freundlichen Menschen."
        belohnung = "Golddukaten oder ein Artefakt"
        bedrohung = "Ein dunkles Geheimnis magischer Natur die die Menschen versuchen geheim zu halten aus eigennützigen Motiven."
    if zustand == "Neutral":
        bild = "Normale Ortschaft. Die Menschen sind zufrieden mit dem was sie besitzen."
        belohnung = "Dienstleistungen"
        bedrohung = "Eine magische Bedrohung unter die die Menschen spüren, aber nicht sonderlich darunter leiden."
    if zustand == "Niedergang":
        bild = "Überwiegend herrscht Armut und verfallene Gebäuden überall. Die Menschen haben resigniert oder sind Fremden gegenüber negativ eingestellt. Die Kriminialität ist ebenfalls sehr hoch."
        belohnung = "Ideele Werte um den hiesigen Menschen zu helfen."
        bedrohung = "Eine Bedrohung unter denen die Menschen leiden und von denen sie befreit werden möchten."

    print("Anzahl Gebäude:",gebäude)

    prompt = f"""
    Ezeuge aus der Fantasy Rollenspiel "Das Schwarze Auge" eine {typ} mit {gebäude} besonderen Gebäuden die von Abenteurern aufgesucht werden können. 
    
    Gebe deine Antwort als Python Dictionary zurück. Ausgabe ohne Einleitung, ohne Erläuterung, nur Code. Ohne die Einleitung "```python" und den Abschluss "```".
    Berücksichtige beim erzeugen er Values hierbei das Gesamtbild: {bild}. 

    Antworte im JSON-Format mit folgendesn keys:

    "name": Name der Ortschaft.
    "beschreibung_des_ortes": Gesamtbild und Zustand der Ortschaft.
    "bevölkerung_und_gesellschaft": Beschreibung der sozialen Strukturen der dort lebenden Menschen.
    "gerüchte_und_legenden": Eine Möglichkeit für einen Plot bzw. eine Quest für die Helden.
    "quests_und_interaktionsmöglichkeiten": Eine Möglichkeit für Quests unter Berücksichtugung des Gesamtbildes mit einer Belohnung in Form von: {belohnung}
    "gefahren_und_bedrohungen": {bedrohung}
    "anzahl_der_wirtshäuser": Anzahl der Wirtshäuser.
    "wirtshäuser": Eine Liste der Namen der Wirtshäuser.
    "besonderen_orte": Eine Liste der besonderen Orte, die wiederum den Namen, den Orts-Typ und eine kurze Beschreibung enthalten.
    "besondere_personen": Eine Liste von 2 besonderen Personen mit den Keys "name", "rolle", "beschreibung", "plotansatz" und an welchem "besonderen_ort" diese anzutreffen sind.
    "bemerkung": "Ort von Co-Meister erzeugt."
    """

    antwort = get_completion(prompt)
    

    return(antwort)

typ = "Dorf"
gross = "Klein"
zustand = "Niedergang"
ort_obj = ort_erzeugen(typ, gross, zustand)
# Aufruf der Funktion mit dem Prompt

print(ort_obj)
print("FINSISH")
print(type(ort_obj))
print("Name der Ortschaft:",ort_obj.name)
print("Gerüchte und Legenden:",ort_obj.gerüchte_und_legenden)
print("Besondere Personen:",ort_obj.besondere_personen)
for i in ort_obj.besondere_personen:
    print("Besondere Person:",i["name"])
print("Bemerkung:",ort_obj.bemerkung)
