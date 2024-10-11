# main function
def main():
    # get the user's greeting
    greeter = input("Greeting: ").lower().strip()
    # check if the first word begins with 'hello'
    if greeter.startswith("hello"):
        print("$0")
    # check if the first letter begins with 'h'
    elif greeter[0] == "h":
        print("$20")
    # catch all clause to check all other inputs
    else:
        print("$100")
main()
