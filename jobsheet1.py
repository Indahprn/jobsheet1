import random
from guess import Guess

jawaban= random.randint(1,10)

tebakan= int(input("tebak 1-10: "))

rslt= Guess(jawaban, tebakan)

if rslt.cek():
    print("jawaban kamu benar!")
else:
    print("jawaban kamu salah!")