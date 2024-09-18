
def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    lab1=True
    i=0
    j=len(word)-1
    while i< (len(word)/2) :
        if word[i] != word[j-i]:
            lab1=False
            break
        i +=1
    return lab1
    pass

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    if number_val< 0:
       flist=[]
    else:
        flist=[0]
        flist.append(1)
        flist.append(flist[0]+flist[1])
        i=len(flist)-1
       
        while flist[i] < number_val:
            flist.append(flist[i]+flist[i-1])          
            i +=1
        flist.pop()
    return flist
    pass


def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    str1=str1.lower()
    str2=str2.lower()
    n =str1.find(str2)
    count=0
    while n>=0:
        count+=1
        n=str1.find(str2, n+len(str2))
        print(n)
    return(count)
    pass

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    if len(list1)!=len(list2):
        sum_list=[]
    else:
        n=len(list1)
        i=0
        sum_list=[]
        while i<n:
            sum_list.append(list1[i]+list2[i])
            i+=1
    return sum_list


def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = None
    while True:
        try:
            password = input("Please enter your password: ")
            if isValidPassword(password):
                break
            
        except Exception as e:
            print("Please enter valid password: ")
    return password

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    valid =True
    if len(password) < 8: 
        valid=False
    fu=False
    for s in password:
        if s.isupper():
            fu=True
            break
    fl=False
    for s in password:
        if s.islower():
            fl=True
            break
    fn=False
    for s in password:
        if s.isdigit():
            fn=True
            break
    valid= valid and fu and fl and fn
    return valid
    pass



