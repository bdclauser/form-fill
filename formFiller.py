#! python3
# formFiller.py - Automatically fills in a form.
# use mouseNow,py to get coords to fields.

import pyautogui
import time

# Set the coordinatoes for the computer
nameField = ()
submitButton = ()
submitButtonColor = ()
submitAnotherLink = ()

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet',
                'robocop': 4, 'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'cyrstal ball', 'robocop': 1,
                'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}, ]

# Give a chance to kill the script.
for person in formData:
    print('>>> 5-SECOND PAUSE TO LET THE USER PRESS CTRL-C <<<')
    time.sleep(5)

# TODO: Wait until form page loads.
pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')

# move to first field
print('Entering %s info...' % (person['name']))
pyautogui.write(['\t', '\t'])

# TODO: Fill out name field.
pyautogui.write(person['name'] + '\t')

# TODO: Fill out fear field
pyautogui.write(person['fear'] + '\t')

# TODO: select wizard power
if person['source'] == 'wand':
    pyautogui.write(['down', '\t'], 0.5)
elif person['source'] == 'amulet':
    pyautogui.write(['down', 'down', '\t'], 0.5)
elif person['source'] == 'crystal ball':
    pyautogui.write(['down', 'down', 'down', '\t'], 0.5)
elif person['source'] == 'money':
    pyautogui.write(['down', 'down', 'down', 'down', '\t'], 0.5)

# TODO: choose action movie likert
if person['robocop'] == 1:
    pyautogui.write(['', '\t'], 0.5)
elif person['robocop'] == 2:
    pyautogui.write(['right', '\t'], 0.5)
elif person['robocop'] == 3:
    pyautogui.write(['right', 'right', '\t'], 0.5)
elif person['robocop'] == 4:
    pyautogui.write(['right', 'right', 'right', '\t'], 0.5)
elif person['robocop'] == 5:
    pyautogui.write(['right', 'right', 'right', 'right', '\t'], 0.5)

# TODO: add additional comment
pyautogui.write(person['comments'] + '\t')

# TODO: click Submit button
time.sleep(0.5)  # Wait for button to activate.
pyautogui.press('enter')

# TODO: wait for form page to load.
print('Submitted form.')
time.sleep(5)

# TODO: click submit another response link.
pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
