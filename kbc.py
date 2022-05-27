question_list = [
"How many continents are there?",
"What is the capital of India?",
"NG mei kaun se course padhaya jaata hai?",
]

options_list = [
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

answer_list = [3, 4, 1]
fifty_list=[["nine","seven"],["delhi","bhopal"],["software engineering","tourism"]]
sol_list=[2,1,1]  
lifelinecount = 0
def lifeline(index):  
    global lifelinecount
    j=0 
    if(lifelinecount==0): 
        while j<len(fifty_list[index]):
            print(j+1,fifty_list[index][j])
            j=j+1
        user_ans = int(input('.....'))
        lifelinecount+=1
        if user_ans==sol_list[index]:
            return True
        else:
            return False
    else:
        print('you Already used 5050')
        return "no"
def option(index):
    j=0
    while j<len(options_list[index]):
        print(j+1,options_list[index][j])
        j=j+1
    user_ans = int(input('.....'))
    if user_ans==answer_list[index]:
        return True
    if user_ans == 5050:
        return(lifeline(index))
    else:
        return False
def que():
    index=0
    while index<len(question_list):
        print("Q.",index+1,question_list[index],"?")
        result=option(index)
        if result == "no":
            index-=1
        elif result==True:
            print("congralution")
        else:
            print("you Losse !")
            break 
        index+=1
def main():
    que()
main() 
