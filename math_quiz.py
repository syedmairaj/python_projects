#math quizz by python
from tqdm import tqdm
import time

print("Welcome to mathify!")
time.sleep(3)

print("Generating questions")
time.sleep(3)

for i in tqdm (range (100), desc="Loading..."):
	pass
time.sleep(3)

attemps = 0

while attemps < 3:
    input_q1 = int(input('What is 50+50: '))

    if input_q1 == 100:
        print('Congratulations you have answered correctly .')
        break
    else:
        print('Incorrect answer. Please try again.')
        attemps += 1
        continue
#Made by SyedAyaanAliKhan