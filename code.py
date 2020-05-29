import time
from selenium import webdriver

keys = {
    "3": {
        "c": "q",
        "C": "2",
        "d": "w",
        "D": "3",
        "e": "e",
        "f": "r",
        "F": "5",
        "g": "t",
        "G": "6",
        "a": "y",
        "A": "7",
        "b": "u",
        "-": ""
    },
    "4": {
        "c": "i",
        "C": "9",
        "d": "o",
        "D": "0",
        "e": "p",
        "f": "z",
        "F": "s",
        "g": "x",
        "G": "d",
        "a": "c",
        "A": "f",
        "b": "v",
        "-": ""
    },
    "5": {
        "c": "b",
        "C": "h",
        "d": "n",
        "D": "j",
        "e": "m",
        "f": ",",
        "F": "l",
        "g": ".",
        "G1": ";",
        "a": "/",
        "A": "'",
        "-": ""
    }
}

# Initialize
driver = webdriver.Chrome()
driver.get("https://www.onlinepianist.com/virtual-piano")
time.sleep(8)
body = driver.find_element_by_tag_name("body")


# Display in the website
def display(string):
    driver.execute_script("document.getElementById('buttonGap3').setAttribute('style', 'height: 40px;text-align: center;font-size: 3rem;color: white;padding-top: 3rem;')")
    driver.execute_script("document.getElementById('buttonGap3').innerHTML = '" + string + "'")


# Send the song as keyboard keys
def play(octave3, octave4, octave5, sleepTime):
    for (i, j, k) in zip(octave3, octave4, octave5):
        if i == '-' and j == '-' and k == '-':
            time.sleep(sleepTime)
        body.send_keys(keys['3'][i], keys['4'][j], keys['5'][k])


print("Checking...")
display("Checking...")
for _ in range(3):
    body.send_keys(keys['4']['c'])
    time.sleep(0.5)

time.sleep(4)


print("Playing --> Harry potter hedwig theme")
display("Playing --> Harry potter hedwig theme")
# Harry Potter Hedwig Theme
HPoctave5 = "------------------------d---c-------------------------------------------------------------------------------------------d---f-------e---D-----------D-----d-C---------------------------------------d-----------d-----------D-------d---C-----------------d-C---------------d-----------------------d-----------d-----------f-------e---D-----------D-----d-C-----------------------------------------"
HPoctave4 = "d---g-----A-a---g-----------------------a-----------g-----A-a---F-------G---d-------------------d---g-----A-a---g-------------------------------b---------------C-------A---g-------------------A-----------A-----------A-----------------------a---A-----------C-------d-----------------------A-----------A-----------A-----------------------b---------------C-------A---g-------------------------"
HPoctave3 = "-" * len(HPoctave4)
# Play the song
play(HPoctave3, HPoctave4, HPoctave5, 0.075)

time.sleep(3)

print("Playing --> Bella Ciao")
display("Playing --> Bella Ciao")
# Bella Ciao
BCoctave3 = "b---------------b---------------b-------------------------------------------------------------------------------------------------"
BCoctave4 = "--e-F-g-e---------e-F-g-e---------e-F-g---F-e-g---F-e-b---b---b-b-a-b-------------b-a---b-------b-a-g-F---b---F---g---e-----------"
BCoctave5 = "----------------------------------------------------------------------c-c-------c-----c-------------------------------------------"
# Play the song
play(BCoctave3, BCoctave4, BCoctave5, 0.1)

driver.close()
