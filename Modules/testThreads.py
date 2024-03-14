import threading
import time

def input_thread():
    global input_received
    input_received = False
    while not input_received:
        print("Waiting for input...")
        time.sleep(10)  # 10 second Wait time
        if not input_received:
            print("No input received within 10 seconds.")

# Start the input thread
input_received = False
input_thread = threading.Thread(target=input_thread)
input_thread.start()

# Main loop to capture input
while True:
    user_input = input("Enter something: ")
    input_received = True
    print(f"Input received: {user_input}")
    if (user_input=='q'):
        quit()
