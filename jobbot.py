from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
from pynput import mouse
from pynput import keyboard
import time


recorded_inputs = []

### From here to the next comment is preamble to utilize pynput mouse and keyboard. See pynput documentaion
def on_move(x, y):
    pass

def on_scroll(x, y, dx, dy):
    pass

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse Click: {x}, {y}")
        recorded_inputs.append(f"Mouse Click: {x}, {y}\n")
        
def on_release(key):  
    if key == keyboard.Key.esc:
        # Stop listener
        return False    
####

def save_inputs_to_file():
    filename = ("saved_mouse_clicks.txt")
    if filename:
        with open(filename, "w") as file:
            for input_event in recorded_inputs:
                file.write(f"{input_event}")
            file.close()
            
def read_and_execute_coordinates(file_path):
    recorded_inputs = []
    with open(file_path, "r") as file:
            for contents in file:
                contents = contents.strip()
                recorded_inputs.append((contents))
                print(contents)
                    

    
    # def extract_coordinates(recorded_inputs):
        # for item in recorded_inputs:
            # parts = recorded_inputs.split(': ')[1].split(', ')
            # x = int(parts[0])
            # y = int(parts[1])
            # return x, y
        # print("x",x, "y", y)
    # extract_coordinates(recorded_inputs)
                
def process_manager():
    try:
        get_step = int(input("Are you 1) recording or 2) playing the recording? \n"))
    except Exception as e: print("There has been an error. See: ",e)
    
    if get_step == 1:
        print("Recording of the mouse has started. Press the escape key to stop recording.")
        while True:
            try:
                #Start mouse listener
                listener = mouse.Listener(
                on_move=on_move,
                on_click=on_click,
                on_scroll=on_scroll)
                listener.start()
                
                #Start keyboard listener. This is so it can know when you hit "esc" to end recording.
                with keyboard.Listener(
                on_release=on_release) as keyboard_listener:
                    keyboard_listener.join()
                on_release(0) #0 becomes variable "key" in the on_release function. The value "0" doesn't mean anything here.
            except Exception as e: print("There has been an error. See: ",e)
            finally:
                save_inputs_to_file()
                return False
            
    if get_step == 2:
        try:
            read_and_execute_coordinates(file_path="saved_mouse_clicks.txt")
            #This block is a repeat of above step 1. This is to ensure execution of the macro can be stopped by pressing "esc"
            with keyboard.Listener(                     ##
            on_release=on_release) as keyboard_listener:##
                keyboard_listener.join()                ##
            on_release(0)                               ##
        except Exception as e: print("There has been an error. See: ",e)
    else:
        print("Please input the numbers 1 or 2. To record a series of mouse clicks, press 1. \n To play the recorded mouse clicks, press 2.")

def main():
    process_manager()
    
main()