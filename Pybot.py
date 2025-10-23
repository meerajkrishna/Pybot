import os
import openai
import gradio as gr

# ✅ Use environment variable instead of hardcoding the API key
# Run this in your terminal before starting the app:
# export OPENAI_API_KEY="your_api_key_here"
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{"role": "system", "content": "You are a Python programming expert."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

demo = gr.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="Real Estate Pro",
    description="A simple chatbot built with OpenAI GPT and Gradio."
)

if __name__ == "__main__":
    demo.launch(share=True)
