"""  1. Create a Student class with attributes:
   - name
   - age
   - course
   Create 3 objects and display their details."""

# class Qis:
#     qis = ''' 
#  _______ _________ _______    _______  _______  _______  ______   _______  _______          
# (  ___  )\__   __/(  ____ \  (  ___  )(  ____ \(  ___  )(  __  \ (  ___  )(       )|\     /|
# | (   ) |   ) (   | (    \/  | (   ) || (    \/| (   ) || (  \  )| (   ) || () () |( \   / )
# | |   | |   | |   | (_____   | (___) || |      | (___) || |   ) || (___) || || || | \ (_) / 
# | |   | |   | |   (_____  )  |  ___  || |      |  ___  || |   | ||  ___  || |(_)| |  \   /  
# | | /\| |   | |         ) |  | (   ) || |      | (   ) || |   ) || (   ) || |   | |   ) (   
# | (_\ \ |___) (___/\____) |  | )   ( || (____/\| )   ( || (__/  )| )   ( || )   ( |   | |   
# (____\/_)\_______/\_______)  |/     \|(_______/|/     \|(______/ |/     \||/     \|   \_/   
#                                                                                              '''
#     Institute = "QIS acadamy"
#     address= 'YMCA cross road, Kozhikode'
#     batch = {'9:00':0,'11:00':0,'14:00':0,'16:00':0}
#     subject =['Python','Java','Embad']
#     faculty ={'Python':'Sree','Java':'Divya','Embad':'swapna'}
#     staff = {'pricipal':'Rubina','Office':'Anjana','attend':'Devika'}

#     def flag_set(self):
#         flag = input ('For continue press \'y\' for exit press \'n\' :')
#         flag = flag.lower()
#         if flag == 'y':
#             return True
#         else:
#             self.close_code = 1
#             return False

# class Student(Qis):
#     std_id= 1
    
#     def __init__(self, name):
#         self.name = name
#         Std_admission(self.name)
#         Doc_maintain(self.name)

#     def show_details(self):
#         print(self.qis)
#         print(f"................{self.Institute}..................")
#         print(f"................{self.address}..................")
#         print(f"Student Name :{self.name}, course : {self.sub}")
#         print(f"Student ID :{self.user_id}, Faculty : {self.teacher}")
#         print(f'Your class timming is :{self.time} plus two hours')
#         print(f"...................................................")
#         for x, y in self.staff.items():
#             print(x ,':', y)
#         print(f".................For Office use...........................")
#         print(f'Age :{self.s_age}, Sex :{self.s_sex}')
#         print(f'Qalification :{self.s_edu}, Joining Date {self.join_date}')
#         print(f'Address :{self.s_address1} ,{self.s_address2},{self.s_pincode}')
#         print(f'Contact :✉️{self.s_email} ,📞{self.s_phone},💬{self.s_whatsup}')


# class Std_admission(Student):
#     close_code = 0

#     def __init__(self, name):
#         super().__init__(name)
#         self.info_col()

#     def info_col (self):
#         print(self.qis)
#         self.s_age = int(input('Please enter your age:'))
#         self.s_address1 = input('Please enter your house name:')
#         self.s_address2 = input('Please enter your place:')
#         self.s_pincode = int(input('Please enter your pin code:'))
#         self.s_email = input('Please enter email address:')
#         self.s_phone = input('Please enter phone number:')
#         self.s_whatsup = input('Please enter whatsup number:')
#         self.s_sex = input('Please enter gender:')
#         self.s_edu = input('Please enter education qualification:')
#         print(self.qis)
        
#         s_flag= True
#         while s_flag:
#             s_sub = input(f'Which course you looking for {self.subject} :')
#             s_sub = s_sub.capitalize()
#             if s_sub in self.subject:
#                 self.sub = s_sub
#                 self.user_id = 'CLT' + self.sub[:2] + str(Student.std_id)
#                 Student.std_id+=1
#                 self.teacher = self.faculty[s_sub]
#                 s_flag= False
#             else:
#                 print(f'The Course you selected is not available in {self.subject}')
#                 print('If you want select agan try again')
#                 s_flag = self.flag_set()
        
#         if self.close_code == 0:
#             s_flag= True
#             while s_flag:
#                 s_time = input(f'Which batch you looking for {self.batch} :')
#                 if s_time in self.batch:
#                     if self.batch[s_time] > 9:
#                         print ('Batch slot is not available, select new batch timmings')
#                     else:
#                         Student.batch[s_time] += 1
#                         self.time = s_time
#                         from datetime import date
#                         self.join_date =date.today().strftime(" %d-%m-%y")
#                         print(f'Admission sucessful')
#                         s_flag= False
#                 else:
#                     print('Invaled. If you want select agan try again')
#                     s_flag = self.flag_set()
        
# class Doc_maintain(Student):
#     import csv
#     def __init__(self):
#         self.std_add_doc()
            

#     def std_doc_head(self):
#         import csv
#         with open (r'\\127.0.0.1\qis\qisstudents.csv', 'w', newline="") as f:
#             std_doc = csv.writer(f)
#             std_doc.writerow(['Std_id','Join Date','batch', 'Name','Age','Sex','Qualification','Address','pincode','E mail','Phone Number','Whats up','Course','Faculty',])  

#     def std_add_doc(self):
#         import csv
#         with open (r'\\127.0.0.1\qis\qisstudents.csv', 'a', newline="") as f:
#             std_doc = csv.writer(f)
#             std_doc.writerow([self.user_id,
#                               self.join_date,
#                               self.time,
#                               self.name,
#                               self.s_age,
#                               self.s_sex,
#                               self.s_edu,
#                               self.s_address1 +',' + self.s_address2,
#                               self.s_pincode,
#                               self.s_email,
#                               self.s_phone,
#                               self.s_whatsup,
#                               self.sub,
#                               self.teacher])


