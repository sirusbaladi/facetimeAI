import time
import chatgpt

cumulative = []
previous_content = ''
current_content = ''
last_change_time = time.time()
isRepeated = False

while True:
    with open('output.txt', 'r') as f:
        current_content = f.read()

    # Check if the content is different from the previous content
    if current_content != previous_content:
        previous_content = current_content  # Update previous_content
        last_change_time = time.time()  # Update the time of the last change
        cumulative.append(current_content)

    # If the content hasn't changed for 3 or more seconds
    elif time.time() - last_change_time >= 1: #TODO: change to lower, experiment.
        last_change_time = time.time()  # Update the time of the last change


        chatgpt.main("".join(cumulative))


        cumulative = []

    time.sleep(0.3) # TODO: change to lower, experiment.
