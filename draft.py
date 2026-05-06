def display(biggest_number):
    print(f"The biggest of 3 nos is: {biggest_number}")

def get_input():
    a=input("Enter value of a: ")
    b=input("Enter value of b: ")
    c=input("Enter value of c: ")
    return a,b,c

def calculate_max(a,b,c):
    if (a>b and a>c):
        return a
    if b>a and b>c:
        return b
    else:
        return c
    
def main():
    a,b,c=get_input()
    biggest_number=calculate_max(a,b,c)
    display(biggest_number)

main()