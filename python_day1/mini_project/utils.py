def display_users(users):

    for user in users:

        print("-" * 40)

        print("Name :", user.get("name"))
        print("Email:", user.get("email"))

        address = user.get("address", {})

        print("City :", address.get("city"))