import openai

openai.api_key = "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"


def chat_with_openai(messages):
    conversation = [
        {"role": "system", "content": "You a world-class therapist. Feel free to ask questions, give advice, or so on if that's what a therapist would do.\
         Only when I say goodbye or thank you, end the conversation by saying byeee! in a very friendly way, otherwise, do not end the conversation. Avoid suggesting seeing a therapist. Keep your answers short, less than 50 words" },
    ] + messages

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=1
    )

    message = response['choices'][0]['message']['content']
    return message

def main(user_input):
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
