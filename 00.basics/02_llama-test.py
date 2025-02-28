import ollama

prompt = "Explain functioning of UN assembly"

role = "user"

messages = [{
    'role': role,
    'content': prompt,
}]

stream = ollama.chat(model='llama3.2', messages=messages, stream=True)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
