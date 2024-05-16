from picamera import PiCamera
from time import sleep

def read_counter():
    try:
        with open('counter.txt', 'r') as f:
            counter = int(f.read())
    except FileNotFoundError:
        counter = 1  # Set initial counter value if file not found
    return counter

def update_counter(counter):
    with open('counter.txt', 'w') as f:
        f.write(str(counter + 1))

def main():
    counter = read_counter()
    update_counter(counter)
    camera = PiCamera()
    
    filename = f'SSI/home{counter}.h264'
    
    camera.start_recording(filename)
    sleep(5)
    camera.stop_recording()

if __name__ == "__main__":
    main()