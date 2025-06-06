from groq import Groq

client = Groq(api_key="")

def get_recipe(question):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful recipe assistant. When users provide ingredients, you will create detailed recipes using those ingredients. Include step-by-step instructions, cooking times, and any additional ingredients needed to complete the recipe. Make sure the recipes are practical and easy to follow."
                },
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="llama-3.3-70b-versatile"
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
