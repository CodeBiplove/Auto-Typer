import pyautogui
import time
import os

# Define the string to send
text = """
**Speaker Note:**  
This makes it possible to have the Domain Hosted from the outside environment such as the Stamford College Public Web, online classes, or public web application while at the same time having other disputed applications such as emails for the staffs or student records . For instance, when the hackers mounted a ransomware attack in 2020, hosting the public servers in DMZ might have helped to deter the cyber criminals from gaining access into the internal network. Implementing reserved IP address on servers makes it possible to monitor with other tools such as PRTG reliably during audit or when identifying threats. Further, NAT as a security feature hides internal IPs, this is not an easy target for the attackers, as was observed in the mid-2020 attack."""

time.sleep(5)

typing_speed = 0 # Set the typing speed to 0.3 seconds per character for 40 words per minute

# Type each character in the string
for char in text:
    pyautogui.press(char)
    time.sleep(typing_speed)

print("Done")
