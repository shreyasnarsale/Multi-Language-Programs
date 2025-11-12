# ---------------- Event Processing System using Queue ---------------- #

from collections import deque

class EventProcessingSystem:
    def __init__(self):
        self.event_queue = deque()   # Queue to store events

    # 1. Add an Event
    def add_event(self, event):
        self.event_queue.append(event)
        print(f"Event '{event}' added to the queue.")

    # 2. Process the Next Event
    def process_event(self):
        if not self.event_queue:
            print("No events to process.")
        else:
            event = self.event_queue.popleft()
            print(f"Processing event: {event}")

    # 3. Display Pending Events
    def display_events(self):
        if not self.event_queue:
            print("No pending events.")
        else:
            print("Pending Events:", list(self.event_queue))

    # 4. Cancel an Event
    def cancel_event(self, event):
        if event in self.event_queue:
            self.event_queue.remove(event)
            print(f"Event '{event}' canceled.")
        else:
            print(f"Event '{event}' not found or already processed.")


# ---------------- Main Program ---------------- #
if __name__ == "__main__":
    system = EventProcessingSystem()

    while True:
        print("\n--- Event Processing System ---")
        print("1. Add an Event")
        print("2. Process Next Event")
        print("3. Display Pending Events")
        print("4. Cancel an Event")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            event = input("Enter event name: ")
            system.add_event(event)

        elif choice == "2":
            system.process_event()

        elif choice == "3":
            system.display_events()

        elif choice == "4":
            event = input("Enter event name to cancel: ")
            system.cancel_event(event)

        elif choice == "5":
            print("Exiting Event Processing System. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
