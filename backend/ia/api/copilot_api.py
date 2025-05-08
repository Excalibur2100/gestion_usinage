from openai import OpenAI
import os

# Initialise le client avec la clé API OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generer_code(prompt: str, model="gpt-3.5-turbo") -> str:
    """
    Envoie un prompt à l'IA et retourne la réponse.
    """
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Tu es un assistant développeur Python expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Erreur lors de l'appel OpenAI : {e}"
