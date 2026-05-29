class Hospital:
    hopital_name = 'Fathiam Hospital'
    h_address = 'Near Vet hospital, Kannur road, Kozhikode'
    h_facility = ['Causuality', 'Emergency', 'in patianet service']
    h_deparments =['genaral medicine','Pediatrician','gynocology','Orthology']
    h_patianet_ID ='P'
    h_docotrs_id = 'D'
    h_nurse_id = 'N'

    def __init__(self, h_id,name,age,depart = 'genaral medicine'):
        self.hosp_id =h_id
        self.name =name
        self.age =age
        self.depart = depart

    def show_hosp (self):
        print(f'............ {self.hopital_name}................')
        print(f'............ {self.h_address}...................')
        print(f'{self.hosp_id} : {self.name}  {self.age}  {self.depart}')

class Doctor(Hospital):
    doc_id = 1
    def __init__(self):
        self.doctors = []
    
    def add_doctors(self,name,age,depart):
        self.hosp_id = self.h_docotrs_id + Doctor.doc_id
        Doctor.doc_id+=1 
        dr = Hospital(self.hosp_id,name,age,depart)
        self.doctors.append(dr)
        print('Doctor add successfully')

    def show_all_doctors (self):
         if not self.students:
            print("No Student found")
         return
    
         for user in self.students:
            user.display_details()
   
    def find_student(self,student_id):
      for user in self.students:
         if user.std_id == student_id:
            return user
      return None
   
    def get_atribute(self,student_id, atribute):
      user = self.find_student(student_id)
      if user:
         a = getattr(user,atribute,'atribute not found')
         print(f"{atribute} :{a}")
      else:
         print('Student not found')

    def update_atribute (self, student_id,atribute,value):
      user =self.find_student(student_id)
      if user:
         setattr(user, atribute,value)
         print(f"{atribute} update successfully")
      else:
         print('User not found')

    def delete_atribute(self,student_id,atribute):
      user = self.find_student(student_id)
      if user:
         if hasattr(user,atribute):
            delattr(user,atribute)
            print(f'{atribute} delete sucessfully')
         else:
            print(f'{atribute} not found')
      else:
         print('Student not found')
