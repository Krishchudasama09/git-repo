class StudyMaterialApp:
    def __init__(self):
        self.materials = {}

    def add_material(self, subject, material):
        if subject in self.materials:
            self.materials[subject].append(material)
        else:
            self.materials[subject] = [material]
        print(f"Material added under '{subject}'!")

    def view_materials(self):
        if not self.materials:
            print("No materials available.")
        else:
            for subject, materials in self.materials.items():
                print(f"\nSubject: {subject}")
                for idx, material in enumerate(materials, 1):
                    print(f"{idx}. {material}")

    def delete_material(self, subject, material_index):
        if subject in self.materials and 0 < material_index <= len(self.materials[subject]):
            deleted_material = self.materials[subject].pop(material_index - 1)
            print(f"Material '{deleted_material}' deleted from '{subject}'.")
        else:
            print("Invalid subject or index.")

    def run(self):
        while True:
            print("\n--- Study Material App ---")
            print("1. Add Material")
            print("2. View Materials")
            print("3. Delete Material")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice == '1':
                subject = input("Enter the subject: ")
                material = input("Enter the material details: ")
                self.add_material(subject, material)

            elif choice == '2':
                self.view_materials()

            elif choice == '3':
                subject = input("Enter the subject: ")
                material_index = int(input(f"Enter the index of material to delete under '{subject}': "))
                self.delete_material(subject, material_index)

            elif choice == '4':
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = StudyMaterialApp()
    app.run()
