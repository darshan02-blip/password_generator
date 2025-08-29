def get_user_input():
    while True:
        try:
            length = int(input("🔑 Enter desired password length: "))
            if length < 4:
                print("⚠ Password length should be at least 4!")
                continue
            break
        except ValueError:
            print("⚠ Please enter a valid number!")

    print("\nChoose password complexity:")
    print("1️⃣ Low (only lowercase letters)")
    print("2️⃣ Medium (letters + numbers)")
    print("3️⃣ High (letters + numbers + symbols)")

    choice = input("👉 Enter choice (1-3): ")

    complexity_map = {"1": "low", "2": "medium", "3": "high"}
    complexity = complexity_map.get(choice, "medium")

    return length, complexity
