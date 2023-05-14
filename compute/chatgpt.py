import openai

openai.api_key = "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"


def chat_with_openai(messages):
    conversation = [
        {"role": "system", "content": "You a world-class therapist. Great advisor. \
         You will answer like a professional therapist who cares about the patients.\
         You have empathy and all the qualities that a great therapist has.\
         Feel free to ask questions, give advice, or so on if that's what a therapist would do.\
         Keep the answers short."},
    ] + messages

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,
        max_tokens=100,
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
