



gold_answers = []
predicted_answers = []

with open('semeval2017_task7/data/test/subtask1-homographic-test.gold') as f:
    line_g = f.readlines()
f.close()



with open('semeval2017_task7/data/test/subtask1-homographic-test_predicted.txt') as f:
    line_p = f.readlines()
f.close()

print(len(line_g))
print(len(line_p))

count = 0  
for i in range(len(line_p)):
    if line_g[i] == line_p[i]: 
        count +=1


print(count, ' out of ', len(line_g), ' are correct')