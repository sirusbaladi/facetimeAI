import time

cumulative = []
previous_content = ''
current_content = ''
last_change_time = time.time()

while True:
    with open('output.txt', 'r') as f:
        current_content = f.read()

    # Check if the content is different from the previous content
    if current_content != previous_content:
        previous_content = current_content  # Update previous_content
        last_change_time = time.time()  # Update the time of the last change
        cumulative.append(current_content)
        #print("".join(cumulative))

    # If the content hasn't changed for 3 or more seconds
    elif time.time() - last_change_time >= 5: #TODO: change to lower, experiment.
        # print('No difference')
        last_change_time = time.time()  # Update the time of the last change
        print("".join(cumulative))
        print("------------sent to GPT------------")
        cumulative = []

    time.sleep(1) # TODO: change to lower, experiment.
