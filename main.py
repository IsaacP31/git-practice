# Advanced Infrastructure Control Script with Logging

def show_menu():
    print("\n" + "="*40)
    print("      INFRASTRUCTURE MANAGEMENT MENU    ")
    print("="*40)
    print("1. Check System Resources")
    print("2. Run Simulated Docker Container 🐳")
    print("3. View System Logs 📄")
    print("4. Exit System")
    print("="*40)

# 🚀 NEW: Function to write logs to a real file
def register_log(event_description):
    with open("system_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[LOG] {event_description}\n")
    print("-> Event successfully saved to system_log.txt")

def run_console():
    developer_name = input("Enter your developer name: ")
    print(f"\nWelcome, Engineer {developer_name}. System online.")
    register_log(f"Engineer {developer_name} logged into the system.")
    
    while True:
        show_menu()
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            ram = int(input("\nEnter available RAM in GB: "))
            status = ""
            if ram >= 32:
                status = "EXCELLENT. Ready for heavy virtualization."
            elif ram >= 16:
                status = "GOOD. Standard environment."
            else:
                status = "WARNING. Limited resources."
            
            print(f"Status: {status}")
            # Saving the action
            register_log(f"Resource check executed. RAM: {ram}GB. Status: {status}")
                
        elif choice == "2":
            print("\n[DOCKER] Starting container...")
            print("[DOCKER] Status: Running successfully on port 8080.")
            register_log("Docker container simulated on port 8080.")
            
        # 🚀 NEW: Option to read the file from Python
        elif choice == "3":
            print("\n--- SHOWING SYSTEM LOGS ---")
            try:
                with open("system_log.txt", "r", encoding="utf-8") as file:
                    print(file.read())
            except FileNotFoundError:
                print("No logs recorded yet.")
                
        elif choice == "4":
            print(f"\nShutting down system. Goodbye, Engineer {developer_name}!")
            register_log(f"Engineer {developer_name} logged out.")
            break
            
        else:
            print("\nInvalid option. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    run_console()