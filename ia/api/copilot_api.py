import openai

class AssistantIA:
    def __init__(self, api_key):
        openai.api_key = api_key

    def handle_task(self, task_description):
        """
        Gère une tâche en utilisant l'API OpenAI pour générer du code.
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Remplacez par gpt-3.5-turbo si gpt-4 n'est pas disponible
            messages=[
                {"role": "system", "content": "Tu es un assistant IA qui génère du code."},
                {"role": "user", "content": task_description}
            ]
        )
        # Récupère le contenu généré
        return response['choices'][0]['message']['content']