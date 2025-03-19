
import csv

class PatientRecord:

    def __init__(self, patient_id, full_name, sex, age, contact_number, patient_vaccination_status, animal_type, animal_vaccination_status, animal_ownership, injury_category, treatment_status):
        self.file_name = "ABTCare.csv"
        
        self._patient_id = patient_id
        self.full_name = full_name
        self.sex = sex
        self.age = age
        self.contact_number = contact_number
        self.patient_vaccination_status = patient_vaccination_status
        self.animal_type = animal_type
        self.animal_vaccination_status = animal_vaccination_status
        self.animal_ownership = animal_ownership
        self.injury_category = injury_category
        self.treatment_status = treatment_status
        

    def make_file(self):
        with open(self.file_name, mode="w", newline=" ") as file:
            file_writer = csv.writer(file)
            file_writer.writerow(["Patient ID", "Full Name", "Sex", "Age", "Contact Number", "PVS", "Animal Type", "AVS", "Animal Ownership", "Injury Category", "Treatment Status"])

    def get_patient_id(self):
        return self._patient_id
    
    def updateRecord(self):
        records = []
        record_found = False

        with open(self.file_name, mode="r") as file:
            file_reader = csv.reader(file)
            headers = next(file_reader)
            records.append(headers)

            for row in file_reader:
                if row[0] == self.get_patient_id():
                    record_found = True
                    row = [
                        self.get_patient_id(),
                        self.full_name,
                        self.sex,
                        self.age,
                        self.contact_number,
                        self.patient_vaccination_status,
                        self.animal_type,
                        self.animal_vaccination_status,
                        self.animal_ownership,
                        self.injury_category,
                        self.treatment_status
                    ]
                records.append(row)

        if not record_found:
            print(f"No record found for Patient ID: {self.get_patient_id()}")
            return

        with open(self.file_name, mode="w") as file:
            file_writer = csv.writer(file)
            file_writer.writerows(records)

        print(f"Record for Patient ID: {self.get_patient_id()} updated successfully.")
