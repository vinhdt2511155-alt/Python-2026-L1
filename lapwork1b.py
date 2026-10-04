#
def input_stinfor(numberofstudent):
    student_info={}
    for i in range(numberofstudent):
        print('enter information of student',str(i+1));
        id = input('enter id of the student: ');
        name = input('enter name of the student: ');
        DoB = input('enter date of birth of the student:');
        student_info[i]={'st'+str(i+1):{'ID':id,'Name':name,'DoB':DoB}};
    return student_info;
def input_crinfo(numberofcourse,student_info):
    course_info={}
    for i in range(numberofcourse):
        print("enter information of course ", str(i+1));
        id=input('enter id of the course: ');
        name=input('enter name of the course: ');
        course_info[i]={'course'+str(i+1):{'ID':id,'Name':name},'student':student_info};
        print("mark for student in this course: ")
    
    return course_info;
def input_mark(course_info,numberofstudent,numberofcourse):
    for i in range(numberofcourse):
        for k in range(numberofstudent):
            print("enter mark for ", course_info[i]['student'][k])
            mark=int(input('enter mark '))
            course_info[i]['student'][k]['mark']= mark;
    return course_info;
def list_course(numberofcourse, course_info):
    for i in range(numberofcourse):
        print('course '+str(i+1), course_info[i]['course'+str(i+1)]);
def list_student(numberofstudent, student_info):
    for i in range(numberofstudent):
        print('student '+str(i+1), student_info[i]['st'+str(i+1)]);
def show_mark(course_info,numberofstudent):
    for i in range(numberofstudent):
        print('mark of student '+str(i+1),course_info['student'][i])
numberofstudent = int(input("enter number of student: "));
numberofcourse = int(input("enter number of course: "));
student_info=input_stinfor(numberofstudent);
course_info=input_crinfo(numberofcourse, student_info);
info=input_mark(course_info,numberofstudent,numberofcourse);        
list_of_stuinfo=list_student(numberofstudent,student_info);
list_of_coinfo=list_course(numberofcourse, course_info);
show_mark_of_stuinfo=show_mark(course_info[0],numberofstudent);