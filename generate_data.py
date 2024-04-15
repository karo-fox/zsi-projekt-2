import random

for i in range(20):
    with open(f"./in/in{i:02}.txt", "w") as file:
        file.write(str(random.randint(0, 100)))