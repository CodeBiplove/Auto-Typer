import pyautogui
import time

# Define the string to send
text = """  A firewall is a network security device that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules.
  Firewalls have been a first line of defense in network security for over 25 years. They establish a barrier between secured and controlled internal networks that can be trusted and untrusted outside networks, such as the Internet.
A firewall can be hardware, software, or both. """

time.sleep(5)

typing_speed = 0.1  # Set the typing speed to 0.3 seconds per character for 40 words per minute

# Type each character in the string
for char in text:
    pyautogui.press(char)
    time.sleep(typing_speed)

print("Done")