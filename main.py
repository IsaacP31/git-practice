# Advanced Infrastructure Control Script

def show_menu():
    print("\n" + "="*40)
    print("      INFRASTRUCTURE MANAGEMENT MENU    ")
    print("="*40)
    print("1. Check System Resources")
    print("2. Run Simulated Docker Container 🐳")
    print("3. Exit System")
    print("="*40)

def run_console():
    developer_name = input("Enter your developer name: ")
    print(f"\nWelcome, Engineer {developer_name}. System online.")
    
    # 🚀 NEW: The Infinite Loop keeps the program running
    while True:
        show_menu()
        choice = input("Select an option (1-3): ")
        
        if choice == "1":
            ram = int(input("\nEnter available RAM in GB: "))
            if ram >= 32:
                print("Status: EXCELLENT. Ready for heavy virtualization.")
            elif ram >= 16:
                print("Status: GOOD. Standard environment.")
            else:
                print("Status: WARNING. Limited resources.")
                
        elif choice == "2":
            print("\n[DOCKER] Starting container...")
            print("[DOCKER] Status: Running successfully on port 8080.")
            
        elif choice == "3":
            print(f"\nShutting down system. Goodbye, Engineer {developer_name}!")
            break  # 🚀 NEW: This breaks the loop and closes the program
            
        else:
            print("\nInvalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    run_console()