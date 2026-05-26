#Print student result
def stu_res():
    stu_name=input('enter student name: ')
    stu_age=int(input('enter student age: '))
    stu_percentage=float(input('enter student percentage: '))

    if stu_percentage>=35:
        print('the student is pass')
    else: 
        print('the student failed')

    print('the percentage obtained is:',stu_percentage,'%')

#stu_res()


#student marks analyzer

def marks_analyzer():
    marks=[]
    for mark in range(5):
        mark=int(input('enter marks value: '))
        marks.append(mark)
    print(marks)
    def high_mark():
        return max(marks)
    
    def low_mark():
        return min(marks)
    
    def avg_mark():
        return sum(marks)/len(marks)
    
    highest_marks=high_mark()
    print('the highest marks is: ',highest_marks)
    
    lowest_mark=low_mark()
    print('the lowest marks is: ',lowest_mark)
    
    average_mark=avg_mark()
    print('the average marks is: ',average_mark)
marks_analyzer()


