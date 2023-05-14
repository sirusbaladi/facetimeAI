import openai

openai.api_key = "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"


def chat_with_openai(messages):
    conversation = [
        {"role": "system", "content": "You are a helpful phone call assistant."},
    ] + messages

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    message = response['choices'][0]['message']['content']
    return message

def main():
    messages = []

    print("Welcome to the chat! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": f"{user_input}"})
        response = chat_with_openai(messages)

        print("AI:", response)
        messages.append({"role": "assistant", "content": f"{response}"})


if __name__ == "__main__":
    main()
