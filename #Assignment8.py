#Assignment8

import pickle


scores = [88, 92, 79, 93, 85]

with open('score.pkl','wb') as f:
    f_wr = pickle.dump(scores , f)

print("score loaded succesfully")

with open('score.pkl','rb') as fr:
    f_rd = pickle.load(fr)
    print(f_rd)

