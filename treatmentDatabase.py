import csv
import os
from patientRecord import PatientRecord

class TreatmentDatabase:
    def __init__(self):
        self.file_name = "ABTcare.csv"
        self.patient_id = 1

        try:
            with open(self.file_name, 'r') as file:
                reader = csv.reader(file)
                records = list(reader)
                if len(records) > 1:
                    last_record = records[-1]
                    last_patient_id = last_record[0]
                    self.patient_id = int(last_patient_id[1:]) + 1
        except FileNotFoundError:
            patient_record = PatientRecord("", "", "", "", "", "", "", "", "", "", "", "")
            patient_record.make_file()


    @staticmethod
    def clear_terminal():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def readRecord(self):
        try:
            with open(self.file_name, mode="r") as file:
                reader = csv.reader(file)
                records = list(reader)
                if not records:
                    print("No records found.")
                    input("\nPress enter to exit.")
                    return
                headers = records[0]
                print(", ".join(headers))

                for row in records[1:]:
                    print(", ".join(row))

        except FileNotFoundError:
            print("Not records found. File does not exist.")

        input("\nPress enter to exit.")

    def appendRecord(self):
        print("Add new patient record.\n")

        while True:
            full_name = input("Enter Full Name ('x' to exit): ").strip()
            if full_name.lower() == "x":
                return
            elif not full_name:
                print("Please enter a valid name.")
                continue
            break

        while True:
            sex = input("Enter Sex (male/female/intersex): ").lower().strip()
            if sex not in ["male", "female", "intersex"]:
                print("Please enter valid sex.")
                continue
            break

        while True:
            try:
                age = int(input("Enter Age: ").strip())
                if age < 1:
                    print("Please enter a valid age.")
                    continue
            except ValueError:
                print("Please enter a valid number of age.")
                continue
            break

        while True:
            contact_number = input("Enter Contact Number: ").strip() 
            if len(contact_number) != 11 or not contact_number.isdigit():
                print("Please enter a valid 11-digit contact number.")
                continue
            break

        while True:
            patient_vaccination_status = input("Enter Patient's Pre-Exposure Prophylaxis status from the past 2 years (yes/no): ").lower().strip()
            if patient_vaccination_status not in ["yes", "no"]:
                print("Please enter if PreP was administered by only 'yes' or 'no'.")
                continue
            break

        while True:
            animal_type = input("Enter Animal Type (cat/dog/rodent/others): ").lower().strip() 
            if animal_type not in ["cat", "dog", "rodent", "others"]:
                print("Please enter a valid animal type.")
                continue
            break

        while True:
            animal_vaccination_status = input("Enter Animal Vaccination Status (yes/no/unknown): ").lower().strip()
            if animal_vaccination_status not in ["yes", "no", "unknown"]:
                print("Please enter a valid vaccination status.")
                continue
            break

        while True:
            animal_ownership = input("Enter Animal Ownership (owned/stray/unknown): ").lower().strip()
            if animal_ownership not in ["owned", "stray", "unknown"]:
                print("Please enter a animal ownership status.")        
                continue
            break

        while True:
            injury_type = input("Enter Injury Type (bite/scratch/both/none): ").lower().strip()
            if injury_type not in ["bite", "scratch", "both", "none"]:
                print("Please enter valid animal injury type.")  
                continue
            
            while True:
                bleeding = input("Did the patient experience bleeding? (yes/no): ").lower().strip()
                if bleeding not in ["yes", "no"]:
                    print("Please enter 'yes' or 'no'.")
                    continue
                break

            if injury_type == "none":
                injury_category = "1"
            elif injury_type == "scratch" and bleeding == "no":
                injury_category = "2"
            elif injury_type == "scratch" and bleeding == "yes":
                injury_category = "3"
            else:
                injury_category = "3"
            break

        while True:
            treatment_status = input("Enter Treatment Status (ongoing/completed): ").lower().strip()
            if treatment_status not in ["ongoing", "completed"]:
                print("Please enter valid treatment status from the choices.")
                continue
            break

        patient_id = f"P{self.patient_id:05d}"
        self.patient_id += 1

        new_record = [patient_id, full_name, sex, str(age), contact_number, patient_vaccination_status,
                    animal_type, animal_vaccination_status, animal_ownership, injury_category, treatment_status]

        try:
            with open(self.file_name, mode="r") as file:
                has_data = len(file.readline()) > 0
        except FileNotFoundError:
            has_data = False

        with open(self.file_name, mode="a") as file:
            writer = csv.writer(file)

            if not has_data:
                writer.writerow(["Patient ID", "Full Name", "Sex", "Age", "Contact Number", 
                            "PVS", "Animal Type", "AVS", "Animal Ownership", "Injury Category", 
                            "Treatment Status"])
            writer.writerow(new_record)

        print("\nPatient record successfully added.")
    
        while True:
            again = input("\nDo you want to add another record? (yes/no): ").lower().strip()
            if again == "yes":
                self.clear_terminal()
                print("""
    ═════════════════════════════════════
    |   ▗▄▖ ▗▄▄▖ ▗▄▄▖ ▗▄▄▄▖▗▖  ▗▖▗▄▄▄   |
    |  ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌   ▐▛▚▖▐▌▐▌  █  |
    |  ▐▛▀▜▌▐▛▀▘ ▐▛▀▘ ▐▛▀▀▘▐▌ ▝▜▌▐▌  █  |
    |  ▐▌ ▐▌▐▌   ▐▌   ▐▙▄▄▖▐▌  ▐▌▐▙▄▄▀  |
    |             RECORDS               |
    ═════════════════════════════════════      
    """)
                self.appendRecord()
                break
            elif again == "no":
                input("Press enter to return to main menu.")
                break
            else:
                print("Please enter 'yes' or 'no'.")

    def editRecord(self):
        print("Edit patient record ('x' to exit).\n")
        while True:
            edit_id = input("Enter the patient ID to be edited: ")
            if edit_id.lower() == "x":
                return
            
            new_records = []
            found = False
                
            try:
                with open(self.file_name, mode="r") as file:
                    reader = csv.reader(file)
                    records = list(reader)
                    
                    for record in records:
                        if edit_id == record[0]:
                            found = True
                            print("\n══════════════════════════════════════════════════════")
                            print(f"Record found:\nPatient ID, Full Name, Sex, Age, Contact Number, PVS, Animal Type, AVS, Category, Treatment Status")
                            print(", ".join(record))
                            new_records = record[:]
                            break

                if not found:
                        print(f"Patient ID {edit_id} not found. Please try again.")
                        continue
                
            except FileNotFoundError:
                print("No records found. File does not exist.")
                return
            
            print("══════════════════════════════════════════════════════")
            print("\nPress enter if no changes are to be made.")        

            new_full_name = input("Enter the new full name: ").strip() or new_records[1] 
            if not new_full_name:
                new_full_name = new_records[1]
            
            while True:
                new_sex = input("Enter New Sex (male/female/intersex): ").lower().strip() or new_records[2]
                if new_sex in ["male", "female", "intersex"]:
                    break
                print("Please enter valid sex.")

            while True:
                try: 
                    new_age = input("Enter New Age: ").strip() or new_records[3]
                    new_age = int(new_age)
                    if new_age >= 1:
                        break
                    print("Please enter a valid age.")
                except ValueError:
                    print("Please enter a valid number for age.")

            while True:
                new_contact_number = input("Enter New Contact Number: ").strip() or new_records[4]
                if len(new_contact_number) == 11 and new_contact_number.isdigit():
                    break
                print("Please enter a valid 11-digit contact number.")
            
            while True:
                new_patient_vaccination_status = input("Enter New Patient's Pre-Exposure Prophylaxis status from the past 2 years (PreP) (yes/no): ").lower().strip() or new_records[5]
                if new_patient_vaccination_status in ["yes", "no"]:
                    break
                print("Please enter only 'yes' or 'no'")

            while True:
                new_animal_type = input("Enter New Animal Type (cat/dog/rodent/others): ").lower().strip() or new_records[6]
                if new_animal_type in ["dog", "cat", "rodent", "others"]:
                    break
                print("Please enter a valid animal type.")

            while True:
                new_animal_vaccination_status = input("Enter New Animal Vaccination Status (yes/no/unknown): ").lower().strip() or new_records[7]
                if new_animal_vaccination_status in ["yes", "no", "unknown"]:
                    break
                print("Please enter a valid vaccination status.")

            while True:
                new_animal_ownership = input("Enter New Animal Ownership (owned/stray/unknown): ").lower() or new_records[8]
                if new_animal_ownership in ["owned", "stray", "unknown"]:
                    break
                print("Please enter a valid animal ownership status.")        

            while True:
                new_injury_type = input("Enter New Injury Type (bite/scratch/both/none): ").lower().strip() or new_records[9]

                if new_injury_type == new_records[9]:
                    new_injury_category = new_records[9]
                    break

                if new_injury_type in ["bite", "scratch", "both", "none"]:
                    while True:
                        bleeding = input("Did the patient experience bleeding? (yes/no): ").lower().strip()
                        if bleeding in ["yes", "no"]:
                            break
                        print("Please enter 'yes' or 'no'.")

                    if new_injury_type == "none":
                        new_injury_category = "1"
                    elif new_injury_type == "scratch" and bleeding == "no":
                        new_injury_category = "2"
                    else:
                        new_injury_category = "3"

                    break  

                print("Please enter a valid injury type.")

            while True:
                new_treatment_status = input("Enter Treatment Status (ongoing/completed): ").lower().strip() or new_records[10]
                if new_treatment_status in ["ongoing", "completed"]:
                    break
                print("Please enter a valid treatment status.")

            edit_record = PatientRecord(edit_id, new_full_name, new_sex, new_age, new_contact_number, new_patient_vaccination_status, new_animal_type, new_animal_vaccination_status, new_animal_ownership, new_injury_category, new_treatment_status)
            edit_record.updateRecord()
            
            while True:
                again = input("\nDo you want to edit another record? (yes/no): ").lower().strip()
                if again == "yes":
                    self.clear_terminal()
                    print("""
══════════════════════════
|  ▗▄▄▄▖▗▄▄▄ ▗▄▄▄▖▗▄▄▄▖  |
|  ▐▌   ▐▌  █  █    █    |
|  ▐▛▀▀▘▐▌  █  █    █    |
|  ▐▙▄▄▖▐▙▄▄▀▗▄█▄▖  █    |
|        RECORDS         |
══════════════════════════
    """)
                    self.editRecord()
                    break
                elif again == "no":
                    input("Press enter to return to main menu.")
                    return
                else:
                    print("Please enter 'yes' or 'no'.")

    def deleteRecord(self):
        print("Delete patient record ('x' to exit).\n")

        records = []
        record_found = False
        patient_data = None
        patient_id = input("Please enter the Patient ID to be deleted: ")
        if patient_id.lower() == "x":
            return
        try:
            with open(self.file_name, mode="r") as file:
                reader = csv.reader(file)
                records = list(reader)
                if not records:
                    print("No records found.")
                    return
                headers = records[0]

                for row in records[1:]:
                    if row[0] == patient_id:
                        record_found = True
                        patient_data = row
                        break

        except FileNotFoundError:
            print("No records found. File does not exist.")
            return

        if not record_found:
            print(f"No record found for Patient ID: {patient_id}")
            input("Press enter to exit.")
            return

        # Display record in the desired format
        print("\n══════════════════════════════════════════════════════")
        print("Record found:")
        print(", ".join(headers))
        print(", ".join(patient_data))
        print("══════════════════════════════════════════════════════")

        confirm = input("\nAre you sure you want to delete this record? (yes/no): ").lower().strip()
        if confirm != "yes":
            print("Deletion canceled.")
            input("Press enter to return to main menu.")
            return

        # Remove the record
        updated_records = [headers] + [row for row in records[1:] if row[0] != patient_id]

        with open(self.file_name, mode="w") as file:
            writer = csv.writer(file)
            writer.writerows(updated_records)

        print(f"\nRecord for Patient ID: {patient_id} deleted successfully.")

        while True:
            again = input("\nDo you want to delete another record? (yes/no): ").lower().strip()
            if again == "yes":
                self.clear_terminal()
                print("""
════════════════════════════════════                    
|  ▗▄▄▄ ▗▄▄▄▖▗▖   ▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖  |
|  ▐▌  █▐▌   ▐▌   ▐▌     █  ▐▌     |
|  ▐▌  █▐▛▀▀▘▐▌   ▐▛▀▀▘  █  ▐▛▀▀▘  |
|  ▐▙▄▄▀▐▙▄▄▖▐▙▄▄▖▐▙▄▄▖  █  ▐▙▄▄▖  |
|             RECORDS              |
════════════════════════════════════                              
"""
                )
                self.deleteRecord()
                break
            elif again == "no":
                input("Press enter to return to main menu.")
                break
            else:
                print("Please enter 'yes' or 'no'.")


       
        

    def searchRecord(self):
        while True:
            self.clear_terminal()
            print("""
════════════════════════════════════                    
|   ▗▄▄▖▗▄▄▄▖ ▗▄▖ ▗▄▄▖  ▗▄▄▖▗▖ ▗▖  |
|  ▐▌   ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌ ▐▌  |
|   ▝▀▚▖▐▛▀▀▘▐▛▀▜▌▐▛▀▚▖▐▌   ▐▛▀▜▌  |
|  ▗▄▄▞▘▐▙▄▄▖▐▌ ▐▌▐▌ ▐▌▝▚▄▄▖▐▌ ▐▌  | 
|             RECORDS              |
════════════════════════════════════   

SEARCH OPTIONS:                      
[1] Search by any data
[2] Search by specific field                
""")
            search_type = input("Please enter the number of your choice ('x' to exit): ").strip()
            if search_type.lower() == 'x':
                return
            try:
                with open(self.file_name, "r") as file:
                    reader = csv.reader(file)
                    records = list(reader)

                    if not records:
                        print("No records found.")
                        return
                    
                    headers = records[0]

                    if search_type == "1":
                        find = input("Enter data to find (case sensitive): ").strip()
                        print("")
                        print("══════════════════════════════════════════════════════")
                        print(", ".join(headers))
                        found = False
                        for row in records[1:]:
                            if find in row:
                                print(", ".join(row))
                                found = True
                        if not found:
                            print(f"No records found matching: {find}")
                        print("══════════════════════════════════════════════════════")
                        input("\nPress enter to leave.")
                        self.clear_terminal()


                    elif search_type == "2":
                        print("\nAVAILABLE FIELDS:")
                        for i,field in enumerate(headers):
                            print(f"[{i + 1}] {field}")

                        while True:
                            try:
                                field_choice = int(input("\nEnter the number of your choice: ").strip())
                                if not 1 <= field_choice <= len(headers):
                                    print("Invalid field number. Please try again.")
                                    continue
                                break
                            except ValueError:
                                print("Please enter a valid number.")

                        field_index = field_choice - 1
                        print(" ")
                        print("══════════════════════════════════════════════════════")
                        print(f"{headers[field_index]}:")
                        
                        if field_index == 0:
                            for i,row in enumerate(records[1:], start=1):
                                print(f"{i}. Patient ID: {row[0]}")
                        else:
                            for i,row in enumerate(records[1:], start=1):
                                print(f"{i}. Patient ID: {row[0]} | {headers[field_index]}: {row[field_index]}")
                        print("══════════════════════════════════════════════════════")
                        input("\nPress enter to leave.")
                        self.clear_terminal()

                    else:
                        print("Please enter the right number of your choice.")
            except FileNotFoundError:
                print("No records found. File does not exist.")

# TO BE ADDED | SUGGESTIONS
# sa add record, if mag 'x' sa lahat ng input, pd mag leave
# sa search, pd mo indicate if minor or adult
# are you sure you want to delete patiend]t id: tas show ung row