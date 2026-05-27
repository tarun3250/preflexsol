from api_service import fetch_users
from utils import display_users


def main():

    users = fetch_users()

    if users:
        display_users(users)

    else:
        print("No users available")


if __name__ == "__main__":
    main()