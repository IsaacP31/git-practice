# Interactive automation script in Python

def welcome_message():
    print("=========================================")
    print("  SYSTEM INFRASTRUCTURE INITIALIZED      ")
    print("=========================================")

def run_system_check():
    # 🚀 Asking the user for input (Variables)
    user_name = input("Enter your developer name: ")
    print(f"\nWelcome back, Engineer {user_name}!")
    
    # Simulating a server resource check
    print("Checking system resources...")
    ram_available = int(input("Enter available RAM in GB (e.g., 16 or 32): "))
    
    # 🚀 Using Conditionals (if/else) to take decisions
    if ram_available >= 32:
        print("Status: EXCELLENT. You have enough power to run heavy Docker containers! 🐳")
    elif ram_available >= 16:
        print("Status: GOOD. Standard environment ready for development.")
    else:
        print("Status: WARNING. Resources might be limited for heavy virtualization.")

if __name__ == "__main__":
    welcome_message()
    run_system_check()