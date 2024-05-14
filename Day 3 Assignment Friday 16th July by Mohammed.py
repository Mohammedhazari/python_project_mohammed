#Day 3- Friday 16th July Assignment 
name = input("Please enter your name: ")
print(f"Welcome {name}!")
print("\nPlease enter all your subject names: ")
subject_1 = input("Subject 1: ")
subject_2 = input("Subject 2: ")
subject_3 = input("Subject 3: ")
subject_4 = input("Subject 4: ")
subject_5 = input("Subject 5: ")
# subject_6 = input("Subject 6: ")


print("\nEnter marks for semester 1: ") 

marks_sub_1_sem_1 = int(input(f"Marks for {subject_1} in Semester 1: "))
marks_sub_2_sem_1 = int(input(f"Marks for {subject_2} in Semester 1: "))
marks_sub_3_sem_1 = int(input(f"Marks for {subject_3} in Semester 1: "))
marks_sub_4_sem_1 = int(input(f"Marks for {subject_4} in Semester 1: "))
marks_sub_5_sem_1 = int(input(f"Marks for {subject_5} in Semester 1: ")) 

total_sem1 = marks_sub_1_sem_1+marks_sub_2_sem_1+marks_sub_3_sem_1+marks_sub_4_sem_1+marks_sub_5_sem_1
ave_sem1 = total_sem1/5
percentage_sem1 = str(total_sem1/500*100)


print("\nEnter marks for semester 2: ") 

marks_sub_1_sem_2 = int(input(f"Marks for {subject_1} in Semester 2: "))
marks_sub_2_sem_2 = int(input(f"Marks for {subject_2} in Semester 2: "))
marks_sub_3_sem_2 = int(input(f"Marks for {subject_3} in Semester 2: "))
marks_sub_4_sem_2 = int(input(f"Marks for {subject_4} in Semester 2: "))
marks_sub_5_sem_2 = int(input(f"Marks for {subject_5} in Semester 2: ")) 

total_sem2 = marks_sub_1_sem_2+marks_sub_2_sem_2+marks_sub_3_sem_2+marks_sub_4_sem_2+marks_sub_5_sem_2
ave_sem2 = total_sem2/5
percentage_sem2 = str(total_sem2/500*100)



print("\nEnter marks for semester 3: ") 

marks_sub_1_sem_3 = int(input(f"Marks for {subject_1} in Semester 3: "))
marks_sub_2_sem_3 = int(input(f"Marks for {subject_2} in Semester 3: "))
marks_sub_3_sem_3 = int(input(f"Marks for {subject_3} in Semester 3: "))
marks_sub_4_sem_3 = int(input(f"Marks for {subject_4} in Semester 3: "))
marks_sub_5_sem_3 = int(input(f"Marks for {subject_5} in Semester 3: "))
total_sem3 = marks_sub_1_sem_3+marks_sub_2_sem_3+marks_sub_3_sem_3+marks_sub_4_sem_3+marks_sub_5_sem_3
ave_sem3 = total_sem3/5
percentage_sem3 = str(total_sem3/500*100) 

print("\nEnter marks for semester 4: ") 

marks_sub_1_sem_4 = int(input(f"Marks for {subject_1} in Semester 4: "))
marks_sub_2_sem_4 = int(input(f"Marks for {subject_2} in Semester 4: "))
marks_sub_3_sem_4 = int(input(f"Marks for {subject_3} in Semester 4: "))
marks_sub_4_sem_4 = int(input(f"Marks for {subject_4} in Semester 4: "))
marks_sub_5_sem_4 = int(input(f"Marks for {subject_5} in Semester 4: "))
total_sem4 = marks_sub_1_sem_4+marks_sub_2_sem_4+marks_sub_3_sem_4+marks_sub_4_sem_4+marks_sub_5_sem_4
ave_sem4 = total_sem4/5
percentage_sem4 = str(total_sem4/500*100) 

print("\nEnter marks for semester 5: ") 

marks_sub_1_sem_5 = int(input(f"Marks for {subject_1} in Semester 5: "))
marks_sub_2_sem_5 = int(input(f"Marks for {subject_2} in Semester 5: "))
marks_sub_3_sem_5 = int(input(f"Marks for {subject_3} in Semester 5: "))
marks_sub_4_sem_5 = int(input(f"Marks for {subject_4} in Semester 5: "))
marks_sub_5_sem_5 = int(input(f"Marks for {subject_5} in Semester 5: "))
total_sem5 = marks_sub_1_sem_5+marks_sub_2_sem_5+marks_sub_3_sem_5+marks_sub_4_sem_5+marks_sub_5_sem_5
ave_sem5 = total_sem5/5
percentage_sem5 = str(total_sem5/500*100)


print("\nEnter marks for semester 6: ") 

marks_sub_1_sem_6 = int(input(f"Marks for {subject_1} in Semester 6: "))
marks_sub_2_sem_6 = int(input(f"Marks for {subject_2} in Semester 6: "))
marks_sub_3_sem_6 = int(input(f"Marks for {subject_3} in Semester 6: "))
marks_sub_4_sem_6 = int(input(f"Marks for {subject_4} in Semester 6: "))
marks_sub_5_sem_6 = int(input(f"Marks for {subject_5} in Semester 6: "))
total_sem6 = marks_sub_1_sem_6+marks_sub_2_sem_6+marks_sub_3_sem_6+marks_sub_4_sem_6+marks_sub_5_sem_6
ave_sem6 = total_sem6/5
percentage_sem6 = str(total_sem6/500*100)

#Overall Results
overall_total = total_sem1+total_sem2+total_sem3+total_sem4+total_sem5+total_sem6
overall_average = overall_total/30
overall_percentage = overall_total/3000 * 100
 

print(f"\nSemester 1 Results:\nTotal: {total_sem1}\nAverage Mark: {ave_sem1}\nPercentage: {percentage_sem1}%") 

print(f"\nSemester 2 Results:\nTotal: {total_sem2}\nAverage Mark: {ave_sem2}\nPercentage: {percentage_sem2}%") 

print(f"\nSemester 3 Results:\nTotal: {total_sem3}\nAverage Mark: {ave_sem3}\nPercentage: {percentage_sem3}%") 

print(f"\nSemester 4 Results:\nTotal: {total_sem4}\nAverage Mark: {ave_sem4}\nPercentage: {percentage_sem4}%") 

print(f"\nSemester 5 Results:\nTotal: {total_sem5}\nAverage Mark: {ave_sem5}\nPercentage: {percentage_sem5}%") 

print(f"\nSemester 6 Results:\nTotal: {total_sem6}\nAverage Mark: {ave_sem6}\nPercentage: {percentage_sem6}%")

print(f"\nOverall Results:\nTotal: {overall_total}\nAverage Mark: {overall_average}\nPercentage: {overall_percentage}%")

print("\nHOPE YOU LIKED IT - BY MOHAMMED")