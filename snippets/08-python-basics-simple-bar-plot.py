# simple vertical bar plot example
import matplotlib.pyplot as plt
import pandas as pd

# creating 2 lists containing example data
events = ["Being Chased by a Bear",
         "Encountering Shark",
         "Teams Notification Sound"]
anxiety_level = [5,15,100]

# plot section
plt.figure(figsize=(6,4))
plt.bar(events,anxiety_level)
plt.xticks(fontsize=9) 
plt.ylabel("Anxiety Level", size=12)
plt.title("Things by Anxiety Level", size=15)
plt.show()