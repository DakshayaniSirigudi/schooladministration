#####"PROJECT OF SCHOOL ADMINISTRATION"#####

import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer=writerow("Name","Age","Contactnumber","Email ID")
            
        writer.writerow(info_list)
        
     #if __name__ =='__main__':
      #   main()

def main():
        condition=True
        student_num=1
         
        while(condition):
             student_info=input("Enter student information for student number 1 in the following format (Name Age Contactnumber EmailId\n")
             print("entered information:")
             print(student_info)

        ##SPLIT##
             student_info_list=student_info.split(" ")
             print("Entered split up information is\n ")
             print(student_info_list)
             print("\nEntered split up information is -\nName:{}\n Age:{}\n Contactnumber:{}\n EmailId:{}".format(student_info_list[0],
                                                    student_info_list[1],student_info_list[2],student_info_list[3]))
             Choice_check=input("Is the entered information is correct?(yes/no):")
             if Choice_check=='yes':
                         write_into_csv(student_info_list)
                      
                         condition_check==input("Enter (yes/no) if you want to enter information for another student")
                         if condition_check=="yes":
                                       condition=True
                                       student_num=student_num+1
                         elif condition_check=="no":
                                        condition=False
                         elif choice_check=="no":
                                         print("\nPlease re-enter the values!")
                      

if __name__ =='__main__':
           main() 
                                 
