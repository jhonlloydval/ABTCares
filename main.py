from treatmentDatabase import TreatmentDatabase
from patientRecord import PatientRecord
import os

class Abtcare:
    def __init__(self):
        self.file_name = "ABTCare.csv"


    @staticmethod
    def clear_terminal():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def main_menu(self):
        while True:
            print("""
------------------ [ WELCOME TO ] ----------------------
|    █████╗ ██████╗ ████████╗ ██████╗                  |
|   ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝  ▗▄▖ ▗▄▄▖ ▗▄▄▄▖  |
|   ███████║██████╔╝   ██║   ██║      ▐▌ ▐▌▐▌ ▐▌▐▌     |
|   ██╔══██║██╔══██╗   ██║   ██║      ▐▛▀▜▌▐▛▀▚▖▐▛▀▀▘  | 
|   ██║  ██║██████╔╝   ██║   ╚██████╗ ▐▌ ▐▌▐▌ ▐▌▐▙▄▄▖  |
|   ╚═╝  ╚═╝╚═════╝    ╚═╝    ╚══════════════════════  |
|------------------------------------------------------|      
|Animal Bite Treatment Case Reporting Management System|
--------------------------------------------------------

[1] READ RECORD
[2] ADD RECORD
[3] EDIT RECORD
[4] DELETE RECORD
[5] SEARCH RECORD
              
""")
            choice = input("Enter the number of the function to use ('x' to exit): ").lower().strip()
            
            if choice == "x":
                print("Management system terminated.")
                exit()

            elif choice == "1":
                self.clear_terminal()
                print("""
══════════════════════════
|  ▗▄▄▖ ▗▄▄▄▖ ▗▄▖ ▗▄▄▄   |
|  ▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌  █  |
|  ▐▛▀▚▖▐▛▀▀▘▐▛▀▜▌▐▌  █  |
|  ▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌▐▙▄▄▀  |
|        RECORDS         |
══════════════════════════
""")
                read_record = TreatmentDatabase()
                read_record.readRecord()
                self.clear_terminal()

            elif choice == "2":
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
                add_record = TreatmentDatabase()
                add_record.appendRecord()
                self.clear_terminal()

            elif choice == "3":
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
                edit_record = TreatmentDatabase()
                edit_record.editRecord()
                self.clear_terminal()
            
            elif choice == "4":
                self.clear_terminal()
                print("""
════════════════════════════════════                    
|  ▗▄▄▄ ▗▄▄▄▖▗▖   ▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖  |
|  ▐▌  █▐▌   ▐▌   ▐▌     █  ▐▌     |
|  ▐▌  █▐▛▀▀▘▐▌   ▐▛▀▀▘  █  ▐▛▀▀▘  |
|  ▐▙▄▄▀▐▙▄▄▖▐▙▄▄▖▐▙▄▄▖  █  ▐▙▄▄▖  |
|             RECORDS              |
════════════════════════════════════                              
""")
                delete_record = TreatmentDatabase()
                delete_record.deleteRecord()
                self.clear_terminal()

            elif choice == "5":
                self.clear_terminal()
                search_record = TreatmentDatabase()
                search_record.searchRecord()
                self.clear_terminal()


            else:
                print("Enter the correct number of your choice.")
                input("\nPress enter to try again.")
                self.clear_terminal()
            
            
start = Abtcare()
start.main_menu()


