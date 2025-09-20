class AutomaticDoor:
    def __init__(self):
        self.door_opened = False  # Initially door is closed

    def __enter__(self):
        print("A person is standing in front of the door.")
        detected = input("Enter the detected object (type 'person' if it's a person): ")

        if detected.lower() == "person":
            print("Sensor has detected a person...")
            print("Door is opening...")
            self.door_opened = True
        else:
            print("Sensor could not detect a person.")
            print("Door remains closed.")

        return self

    def person_enters(self):
        if self.door_opened:
            print("The person has entered the room.")
        else:
            print("Cannot enter — door is closed.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.door_opened:
            print("No one detected by the sensor now...")
            print("Door is closing...")
        else:
            print("Exit: No need to close the door — it was never opened.")


door = AutomaticDoor()
door.__enter__()
door.person_enters()
door.__exit__(None, None, None)
