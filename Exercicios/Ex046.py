import emoji
from time import sleep
for i in range(10,-1,-1):
    print(f'\033[1;35m{i}\033[m')
    sleep(1)
sleep(0.2)
print(emoji.emojize(':fireworks:'*4))
