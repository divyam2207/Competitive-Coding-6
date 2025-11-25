 """
Approach:
This solution uses a dictionary (`messageMap`) to track the last printed timestamp for each message.
Whenever a message arrives with a timestamp, the logger checks:
1. If the message has been printed before.
2. If it has been printed before, it checks if 10 seconds have passed since the last print.
    If 10 or more seconds have passed, the message can be printed again and the timestamp is updated.

The dictionary allows constant-time lookups and updates, making this approach efficient.

Time Complexity (TC):
- O(1) for each call to `could_print_message`. This is because dictionary lookups and updates are constant-time operations on average.

Space Complexity (SC):
- O(m), where `m` is the number of distinct messages. In the worst case, the dictionary will store a timestamp for every unique message.

"""

class Logger:
    """
    @param timestamp: Timestamp
    @param message: Message
    @return: Whether the log can be printed
    """
        # --- write your code here ---
    def __init__(self):
        self.messageMap = {} #message: timestamp

    def could_print_message(self, timestamp: int, message: str) -> bool:

        if message not in self.messageMap:
            self.messageMap[message] = timestamp
            return True
        
        if timestamp - self.messageMap[message] >= 10:
            self.messageMap[message] = timestamp
            return True
        else:
            return False