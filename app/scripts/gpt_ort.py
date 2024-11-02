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
    geographische_lage: str = Field(description="Geographische Lage")

class NSC(BaseModel):
    name: str = Field(description="Name der Person")
    schauplatz: str = Field()
    rolle: str = Field()
    beschreibung: str = Field()
    plotansatz: str = Field()

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
        for i in parsed_output:
            print(i)
        # Validiere die strukturierte Ausgabe mit Pydantic
        ortschaft = Ortschaft(**parsed_output)
        print("Ausgabe nach Joke:",ortschaft)
        print(type(ortschaft))
        return ortschaft
    except json.JSONDecodeError:
        return f"Fehler beim Parsen der Antwort: {response_with_backticks}"
    except ValueError as e:
        return f"Validierungsfehler: {e}"

def get_NSC(prompt, model=llm_model):
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
        #print("Typ:",type(parsed_output))
        #print("Ausgabe vor Joke",parsed_output)
        #for i in parsed_output:
        #    print(i)
        # Validiere die strukturierte Ausgabe mit Pydantic
        ortschaft = NSC(**parsed_output)
        #print("Ausgabe nach Joke:",ortschaft)
        #print(type(ortschaft))
        return ortschaft
    except json.JSONDecodeError:
        return f"Fehler beim Parsen der Antwort: {response_with_backticks}"
    except ValueError as e:
        return f"Validierungsfehler: {e}"


def ort_erzeugen(typ, geo, gross, zustand):
    # Hier kommt der Code für das Skript
    print("Typ:", typ)
    print("Geographie:",geo)
    print("Größe:", gross)
    print("Zustand:", zustand)

    if gross == "Klein":
        gebäude = 1
    if gross == "Mittel":
        gebäude = 2
    if gross == "Groß":
        gebäude = 3

    if geo == "Wald":
        gebäude = 1
    if geo == "Ebene":
        gebäude = 2
    if geo == "Gewässer":
        gebäude = 3
    if geo == "Wüste":
        gebäude = 3
    if geo == "Gebirge":
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
    Ezeuge aus dem Fantasy Rollenspiel "Das Schwarze Auge" eine {typ} mit {gebäude} besonderen Gebäuden die von Abenteurern aufgesucht werden können. 
    
    Gebe deine Antwort als Python Dictionary zurück. Ausgabe ohne Einleitung, ohne Erläuterung, nur Code. Ohne die Einleitung "```python" und den Abschluss "```".
    Berücksichtige beim erzeugen der Values hierbei das Gesamtbild: {bild}. 

    Antworte im JSON-Format mit folgenden keys:

    "name": Name der Ortschaft.
    "geographische_lage": Beschreibung geographischen Lage mitdem Fokus auf: "{geo}"
    "beschreibung_des_ortes": Gesamtbild und Zustand der Ortschaft.
    "bevölkerung_und_gesellschaft": Beschreibung der sozialen Strukturen der dort lebenden Menschen.
    "gerüchte_und_legenden": Eine Möglichkeit für einen Plot bzw. eine Quest für die Helden.
    "quests_und_interaktionsmöglichkeiten": Eine Möglichkeit für Quests unter Berücksichtugung des Gesamtbildes mit einer Belohnung in Form von: {belohnung}
    "gefahren_und_bedrohungen": {bedrohung}
    "anzahl_der_wirtshäuser": Anzahl der Wirtshäuser.
    "wirtshäuser": Eine Liste der Namen der Wirtshäuser.
    "besonderen_orte": Eine Liste der besonderen Orte, die wiederum folgende Keys beinahlten: "name", "ortstyp" und "beschreibung".
    """

    antwort = get_completion(prompt)
    

    return(antwort)

def schauplätze_erzeugen():
    prompt = f"""
    ANWEISUNG MIT ÜBERGABEPARAMETERN

    Gebe deine Antwort als Python Dictionary zurück. Ausgabe ohne Einleitung, ohne Erläuterung, nur Code. Ohne die Einleitung "```python" und den Abschluss "```".

    Antworte im JSON-Format mit folgendesn keys:
    "name": Schauplatzname.

    """

    antwort = get_completion(prompt)

    return(antwort)

def nsc_erzeugen(geo, beschreibung, gesellschaft, legenden, quests, gefahren, schauplatz):
    prompt = f"""
    "Erzeuge aus dem Fantasy Rollensiel "Das Schwarze Auge" einen Nichtspieler Charaktere aus der folgenden Ortschaft: {beschreibung}

    Gebe deine Antwort als Python Dictionary zurück. Ausgabe ohne Einleitung, ohne Erläuterung, nur Code. Ohne die Einleitung "```python" und den Abschluss "```".
    Berücksichtige beim erzeugen der Values hierbei das die Beschreibung für die Bevölkerung und Gesellschaft, falls diese nicht "None" ist: {gesellschaft}. 

    Antworte im JSON-Format mit folgenden keys:

    "schauplatz": {schauplatz}
    "name": Name der Person.
    "rolle": Welche Rolle nimmt der Charakter in der Ortschaft ein. 
    "beschreibung": Beschreibung der Person.
    "plotansatz": Erfinde einen kreativen Plot, der den Helden ermöglicht daran anzuknüpfen und diesem nachzugehen.
    
    """

    #antwort = 2
    antwort = get_NSC(prompt)

    return(antwort)
