from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Controller
from pynput.mouse import Button, Controller
from pynput import keyboard
import threading
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
        while True:
            if key == keyboard.Key.esc:
                print("Escape key pressed!")
                return False
    
    
    def save_inputs_to_file(self, filename="saved_mouse_clicks.txt"):
        with open(filename, "w") as file:
            for input_event in self.recorded_inputs:
                file.write(f"{input_event}")
            

    def start_recording(self):
        self.mouse_listener.start()
        with self.keyboard_listener as keyboard_listener:
            keyboard_listener.join()
        self.save_inputs_to_file()

class Playback:
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    def start_listener(self):
        with self.keyboard_listener as keyboard_listener:
            keyboard_listener.join()
            
    def extract_coordinates(self):
        mouse = Controller()
        self.start_listener()
        with open(self.file_path, "r") as file:
            contents = file.read().strip()
            contents = contents.replace(",", " ")
            contents = contents.split()
            
            for i in range(0, len(contents), 2):
                if i + 1 < len(contents):
                    x = contents[i]
                    y = contents[i + 1]
                    if x.isdigit() and y.isdigit():
                        mouse.position = (int(x), int(y))
                        mouse.click(Button.left, 1)
                        time.sleep(0.4)

               
class Manager:
    def __init__(self):
        self.recorder = Recorder()
        self.playback = Playback(file_path="saved_mouse_clicks.txt")
        
        
    
    def process_manager(self):
        try:
            get_step = int(input("1) Record Mouse Clicks \n2) Play Recorded Mouse Clicks \n0) Exit\n"))
        except Exception as e:
            print("There has been an error. See: ", e)
            return
        
        if get_step == 1:
            print("Mouse click recording has started! Press the Escape key to stop.")
            self.recorder.start_recording()
            print("The recording has been saved to saved_mouse_clicks.txt\nTo play this recording, restart this program and select","2.")
        elif get_step == 2:
            print("Before, the thread count is:",threading.active_count())
            t1 = threading.Thread(target = self.playback.extract_coordinates)
            t2 = threading.Thread(target= self.recorder.on_release(key=0))
            t1.start() and t2.run()
            if t2.is_alive():
                print("it's alive!")
            else:
                print("It's dead..")
            print("Afterwards, the thread count is:",threading.active_count())
            
        elif get_step == 0:
            quit()
        else:
            print("Please input the numbers 1 or 2. To record a series of mouse clicks, press 1. \nTo play the recorded mouse clicks, press 2.")

def main():
    manager = Manager()
    manager.process_manager()

if __name__ == "__main__":
    main()