# File: 1.6-chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("The program illustrates a chaotic function")
    x = eval(input("Enter the first number between 0 and 1: "))
    for i in range (10):
        x = 3.9 * x * (1-x)
        print(x)

main()
