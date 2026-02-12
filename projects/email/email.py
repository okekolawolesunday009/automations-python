import re
# What it matches:

# user@gmail.com

# first.last+tag@company.co.uk

# admin_123@test.org

# What it rejects:

# user@

# @gmail.com

# user@gmail

# user@@gmail.com



def check_email(test_email):
    pattern = r"^[a-zA-Z._%+]+([a-z0-9.]+)?@[a-zA-Z0-9]+\.[a-z]{2,}$"
    result = re.match(pattern, test_email)
    if result:
        print(f"✅ valid email: {test_email}")
    else:
        print(f"❌ in-valid email: {test_email}")

   

if __name__ == "__main__":
    test_email1 = "okekolawole@mysub.com"
    check_email(test_email1)
    print("-----------------------------")
    test_email2 = "okekolawole@@gmail.com"
    check_email(test_email2)
    print("-----------------------------")
    test_email2 = "okekolawole22@gmail.com"
    check_email(test_email2)
    print("-----------------------------")
    test_email2 = "1oke.kolawole@gmail.com"
    check_email(test_email2)
    print("-----------------------------")
    test_email2 = "oke.kolawole@"
    check_email(test_email2)
