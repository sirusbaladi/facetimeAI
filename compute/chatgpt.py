import openai

openai.api_key = ""


def chat_with_openai(messages):
    conversation = [
        {"role": "system", "content": "You a world-class therapist. Never say to seek \
         a therapist or cauncellor as you are the therapist. \
         Your purpose is to run a therapy session.  Go deep.\
          Unlock the inner motives and offer on how to help. \
         Don't just say what to do to the patient but help doing the things you suggest as a good therapist.\
Keep the answers short!"},
    ] + messages

    response = openai.ChatCompletion.create(
        model="gpt-4",
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
