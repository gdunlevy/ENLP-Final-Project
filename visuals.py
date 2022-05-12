import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#-------------Homographic Subtask 1 Results'-----------------------
sns.set(style='white')

d = {'Methods': ['Last Word','Synsets','CNN'],
                   'Accuracies': [54.5,73,82]}


df = pd.DataFrame(data=d)

#create grouped bar chart
sns.barplot(x='Methods', y='Accuracies',data=df,palette="PuBuGn_r")
plt.title('Homographic Subtask 1 Results', fontsize=16)

#add axis titles
plt.ylim(0, 100)
plt.xlabel('Methods')
plt.ylabel('Accuracies')
plt.show()
plt.close()


#-------------Homographic Subtask 2 Results'-----------------------
sns.set(style='white')

d = {'Methods': ['Last Word','GPT'],
                   'Accuracies': [14.9,42]}


df = pd.DataFrame(data=d)

#create grouped bar chart
sns.barplot(x='Methods', y='Accuracies',data=df,palette="PuBuGn_r")
plt.title('Homographic Subtask 2 Results', fontsize=16)

#add axis titles
plt.ylim(0, 100)
plt.xlabel('Methods')
plt.ylabel('Accuracies')
plt.show()
plt.close()


#-------------Heterographic Subtask 1 Results'-----------------------
sns.set(style='white')

d = {'Methods': ['CNN'],
                   'Accuracies': [75]}


df = pd.DataFrame(data=d)

#create grouped bar chart
sns.barplot(x='Methods', y='Accuracies',data=df,palette="Set2")
plt.title('Heterographic Subtask 1 Results', fontsize=16)

#add axis titles
plt.ylim(0, 100)
plt.xlabel('Methods')
plt.ylabel('Accuracies')
plt.show()
plt.close()



#-------------Heterographic Subtask 2 Results'-----------------------
sns.set(style='white')

d = {'Methods': ['Bert Full', 'Bert Second', 'GPT'],
                   'Accuracies': [53,58,78]}


df = pd.DataFrame(data=d)

#create grouped bar chart
sns.barplot(x='Methods', y='Accuracies',data=df,palette="Set2")
plt.title('Heterographic Subtask 2 Results', fontsize=16)

#add axis titles
plt.ylim(0, 100)
plt.xlabel('Methods')
plt.ylabel('Accuracies')
plt.show()
plt.close()


#-------------------------------------------------------

#set seaborn plotting aesthetics
sns.set(style='white')

d = {'Data': ['Subtask1 Homographic','Subtask2 Homographic','Subtask1 Heterographic','Subtask2 Heterographic'],
                   'Count': [2250,1780,1607,1271]}


df = pd.DataFrame(data=d)

#create grouped bar chart
sns.barplot(x='Data', y='Count', data=df, palette="Greens_d")
#sns.set(rc={'figure.figsize':(28,16)})
plt.title('How Many Puns per Dataset', fontsize=16)

#add axis titles

plt.xlabel('Puns')
plt.ylabel('Sentence Count')
plt.show()


plt.close()
