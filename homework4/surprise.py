# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″", #18
        "Magnitude": 0.03, #2
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″", #-13
        "Magnitude": 0.42, #4
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "-16° 42′ 58″", #-36
        "Magnitude": -1.46, #1
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "-08° 12′ 06″", #-28
        "Magnitude": 0.12, #3
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″", #69
        "Magnitude": 1.97, #6
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def printing(dict):
    for key in dict.keys():
        print(f"{key}")

printing(targets)

def printing_2(dict):
    for key, value in dict.items():
        print(f"{key} = {value["Spectral Type"]}")

printing_2(targets)
        
def mag_func(dict):
    for key, value in dict.items():
        if value["Magnitude"] > 0.1:
            print(f"{key} has a magnitude greater than 0.1")

mag_func(targets)

targets["Fomalhaut"] = {"RA": "22h 59m 05.9s", "Dec": "-29° 29′ 05.1″", "Magnitude": 1.18, "Spectral Type": "A4V"}

def whose_the_closest_of_them_all(dict):
    tracker_1 = 2
    tracker_2 = 70
    condensed_list = []
    for key, value in dict.items():
        x = abs((int(value["Dec"][0:3])-20))
        if  value["Magnitude"] < tracker_1:
            tracker_1 = value["Magnitude"]
            tracker_2 = x
            tracker_3 = tracker_1+tracker_2
            condensed_list.append(tracker_3)
            if tracker_3 == min(condensed_list):
                y = key
    return y

# print(type(targets["Vega"]["Dec"][0:3]))
print(whose_the_closest_of_them_all(targets))    

# My favorite constellation is the Coma Berencies constellation.