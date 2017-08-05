

def main():
    address = raw_input()

    try:
        user, domain = address.split("@")

        if len(user) == 5 and user.islower() and domain == "hogwarts.com":
            print "Yes"
        else:
            print "No"

    except:
        print "No"


if __name__ == "__main__":
    main()

    
