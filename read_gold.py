



gold_answers = []
predicted_answers = []

with open('semeval2017_task7/data/test/subtask2-homographic-test.gold') as f:
    line_g = f.readlines()
    print(line_g)
f.close()



with open('semeval2017_task7/data/test/subtask2-homographic_predicted.txt') as f:
    line_p = f.readlines()
    #print(line_p)
f.close()

print(len(line_g))
print(len(line_p))

count = 0  
for i in range(len(line_p)):
    if str(line_p[i]) in line_g: 
        count +=1



print(count, ' out of ', len(line_g), ' are correct')

#'hom_2250\thom_2250_8\n'
#'hom_2250\thom_2250_8\n'
