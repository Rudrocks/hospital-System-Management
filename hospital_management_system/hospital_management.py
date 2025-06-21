# hospital_management.py

patients = []
appointments = []
bills = []

# Function to add a new patient
def add_patient():
    print("\n🩺 Add Patient")
    pid = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")

    patient = {
        "id": pid,
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease
    }
    patients.append(patient)
    print("✅ Patient added successfully!")

# Function to view all patients
def view_patients():
    print("\n📋 Patient Records")
    if not patients:
        print("No patients found.")
    else:
        for p in patients:
            print(f"{p['id']} - {p['name']}, Age: {p['age']}, Disease: {p['disease']}")

# Function to schedule an appointment
def schedule_appointment():
    print("\n📅 Schedule Appointment")
    pid = input("Enter Patient ID: ")
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Date (dd-mm-yyyy): ")

    found = any(p['id'] == pid for p in patients)
    if not found:
        print("❌ Patient ID not found. Add the patient first.")
        return

    appointment = {
        "pid": pid,
        "doctor": doctor,
        "date": date
    }
    appointments.append(appointment)
    print("✅ Appointment scheduled.")

# Function to view appointments
def view_appointments():
    print("\n📆 Appointments")
    if not appointments:
        print("No appointments found.")
    else:
        for a in appointments:
            print(f"Patient ID: {a['pid']} with Dr. {a['doctor']} on {a['date']}")

# Function to generate bill
def generate_bill():
    print("\n💵 Generate Bill")
    pid = input("Enter Patient ID: ")
    consultation = float(input("Consultation Fee: ₹"))
    medicine = float(input("Medicine Fee: ₹"))
    tests = float(input("Test Charges: ₹"))
    total = consultation + medicine + tests

    bill = {
        "pid": pid,
        "consultation": consultation,
        "medicine": medicine,
        "tests": tests,
        "total": total
    }
    bills.append(bill)
    print(f"✅ Bill generated. Total: ₹{total:.2f}")

# Function to view bills
def view_bills():
    print("\n🧾 Bills")
    if not bills:
        print("No bills generated.")
    else:
        for b in bills:
            print(f"Patient ID: {b['pid']} | Total: ₹{b['total']:.2f}")

# Main Menu
def menu():
    while True:
        print("\n========= HOSPITAL MANAGEMENT SYSTEM =========")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Schedule Appointment")
        print("4. View Appointments")
        print("5. Generate Bill")
        print("6. View Bills")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            schedule_appointment()
        elif choice == '4':
            view_appointments()
        elif choice == '5':
            generate_bill()
        elif choice == '6':
            view_bills()
        elif choice == '7':
            print("👋 Exiting... Thank you!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

# Start the program
if __name__ == "__main__":
    menu()
