from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput import keyboard
import time

class Recorder:
    def __init__(self):
        self.recorded_inputs = []
        self.mouse_listener = MouseListener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        self.keyboard_listener = KeyboardListener(on_release=self.on_release)
    
    def on_move(self, x, y):
        pass

    def on_scroll(self, x, y, dx, dy):
        pass

    def on_click(self, x, y, button, pressed):
        if pressed:
            print(f"Mouse Click: {x}, {y}")
            self.recorded_inputs.append(f"Mouse Click: {x}, {y}\n")
    
    def on_release(self, key):  
        if key == keyboard.Key.esc:
            # Stop listener
            return False
    
    def save_inputs_to_file(self, filename="saved_mouse_clicks.txt"):
        with open(filename, "w") as file:
            for input_event in self.recorded_inputs:
                file.write(f"{input_event}")
            

    def start_recording(self):
        print("Recording of the mouse has started. Press the escape key to stop recording.")
        self.mouse_listener.start()
        with self.keyboard_listener as keyboard_listener:
            keyboard_listener.join()
        self.save_inputs_to_file()

class Playback:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_and_execute_coordinates(self):
        extracted_coordinates = []
        with open(self.file_path, "r") as file:
            contents = file.read().strip()
            contents = contents.replace(",", " ")
            contents = contents.split()
            print(contents) 
            coordinate = [int(num) for num in contents if num.isdigit()]
            
            for i in range(0, len(contents), 2):
                if i + 1 < len(contents):
                    x = contents[i]
                    y = contents[i + 1]
                    if x.isdigit() and y.isdigit():
                        extracted_coordinates.append([x, y])
                
            print(extracted_coordinates)
            print(type(extracted_coordinates))
                
    
class Manager:
    def __init__(self):
        self.recorder = Recorder()
        self.playback = Playback(file_path="saved_mouse_clicks.txt")
    
    def process_manager(self):
        try:
            get_step = int(input("Are you 1) recording or 2) playing the recording? \n"))
        except Exception as e:
            print("There has been an error. See: ", e)
            return
        
        if get_step == 1:
            self.recorder.start_recording()
        elif get_step == 2:
            self.playback.read_and_execute_coordinates()
        else:
            print("Please input the numbers 1 or 2. To record a series of mouse clicks, press 1. \n To play the recorded mouse clicks, press 2.")

def main():
    manager = Manager()
    manager.process_manager()

main()
