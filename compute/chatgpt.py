import openai

openai.api_key = "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"


def chat_with_openai(messages):
    conversation = [
        {"role": "system", "content": "You are a professional therapist, I want you to psychologically analyze whatever I say. To introduce yourself, say the following: Hello! I am your personal therapist, what would you like to talk about? KEEP THE ANSWER SHORT"},
    ] + messages

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0,
        max_tokens=40,
    )

    message = response['choices'][0]['message']['content']
    return message

def main(user_input):
    # 'Today was a sad day. My mom forgot it was my birthday and I wish I was never born.'
    messages = []

    if user_input != "":
        print(user_input)
        print("------------sent to GPT------------")
        messages.append({"role": "user", "content": f"{user_input}"})
        response = chat_with_openai(messages)

        with open('gpt.txt', 'w') as f:
            f.write(response)

        messages.append({"role": "assistant", "content": f"{response}"})
        user_input = ""

if __name__ == "__main__":
    main()
