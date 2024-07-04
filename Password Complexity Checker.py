def length_checker(x):
    #checking the basic length of password (8 characters minimum)
    if 8<=len(x):
        if len(x)<=128: #checking if password is not too long (128 characters maximum)
            return "STRONG"
        else: #feedback for user
            return "password is TOO LONG! It should be of atmost 128 characters."
    else: #feedback for user
        return "password is TOO SHORT! It should be of atleast 8 characters."

def commonpwd_checker(x):
    from passwordlib.commonly_used import is_commonly_used
    #checking password strength based on a pre-defined password dictionary containing a list of commonly-used passwords
    if is_commonly_used(x):
        return "password is WEAK! It is easily guessable."
    else:
        return "STRONG"

def numeric_checker(x):
    if x.isnumeric(): #checking if all chars in password are numbers
        return "password is WEAK! Every character cannot be a number."
    else:
        #checking the number of occurences of numbers in the password 
        n_count = 0
        for _ in x:
            for i in range(0,10):
                if _==str(i):
                    n_count+=1         
        if n_count>=3: 
            return "STRONG"
        else: #feedback for user 
            return "password is WEAK! Add atleast 3 numbers in the password."

def special_checker(x):
    spl = ' !@#$%^&*()_-+=~`|/?><.:;{}[]' #characters like ',",\ have not been included as per basic/common password security measures and input sanitization
    
    #checking the number of occurences of special chars in the password
    s_count = 0
    for _ in x:
        for j in spl:
            if _==j:
                s_count+=1
    if s_count>=2:
        return "STRONG"
    else: #feedback for user 
        return "password is WEAK! Add atleast 2 special characters."
    
def upperalpha_checker(x):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    #checking if all characters are uppercase alphabets
    if x.isupper():
        return "password is WEAK! Every alphabet cannot be in uppercase"
    else:
        #checking for number of occurences of uppercase alphabets
        u_count = 0
        for _ in x:
            for j in alpha.upper():
                if _==j:
                    u_count+=1
        if u_count>=2:
            return "STRONG"
        else: #feedback for user 
            return "password is WEAK! Add atleast 2 uppercase alphabets."
        
def loweralpha_checker(x):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    #checking if all chars are lowercase alphabets

    if x.islower():
        return "password is WEAK! Every alphabet cannot be in lowercase"
    else:
        #checking for number of occurences of lowercase alphabets
        l_count = 0
        for _ in x:
            for k in alpha:
                if _==k:
                    l_count+=1
        if l_count>=2:
            return "STRONG"
        else: #feedback for user 
            return "password is WEAK! Add atleast 2 lowercase alphabets."
        
def password_checker(x):
    if type(x)==str: #checking for data type of password for further detailed error handling (if required)
        if length_checker(x)=="STRONG": #length check
            if commonpwd_checker(x)=="STRONG": #dictionary check
                if special_checker(x)=="STRONG": #special characters check
                    if numeric_checker(x)=="STRONG": #numbers check
                        if upperalpha_checker(x)=="STRONG": #uppercase chars check
                            if loweralpha_checker(x)=="STRONG": #lowercase chars check
                                print("password is STRONG!")
                            else:
                                print(loweralpha_checker(x))
                        else:
                            print(upperalpha_checker(x))
                    else:
                        print(numeric_checker(x))
                else:
                    print(special_checker(x))
            else:
                print(commonpwd_checker(x))
        else:
            print(length_checker(x))
    else:
        print("Invalid data type!")

#Small intro and usage instructions
print("This is a Password Complexity Checker. Enter your password* after the arrow(->).")

#Instructions for user to follow
print("Before checking your password, ensure that your password has/is:\n")
print("- Atleast 8 characters long and atmost 128 characters")
print("- Atleast 3 numbers")
print("- Atleast 2 special**,lowercase and uppercase alphabets")
print("- Unique and not so common")

#Important messages for the user
print("\n*This tool only works for PASSWORDS, and does NOT work for PASSPHRASES.")
print("**For security reasons, characters like \',\",\\ are not been considered.")

pswd = str(input("\n\n-> ")) #user input 
password_checker(pswd)
