def conversation():
    print("Do you like coding in python? Answer yes or no")
    answer = input()
    if answer == "yes":
        print("that's good - the united states needs more coders!!")
    else:
        print("Perhaps you will change your mind ")
    print("Goodbye")

def main():
    print("welcome to my conversation program")
    conversation()
    print("thanks for chatting with me")

if __name__ == "__main__":
    main()
