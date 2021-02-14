
coverAll = 0


def Main():
    while(True):
        i = input("""
Choose your lesson:
1. Introduction to Pointers
2. The Null Pointer
3. Pointers and Arrays
4. Pointers and Const
5. Pointers to Pointers
6. Cover it all!
0. Exit

""")
        if i == "1":
            Intro()
        elif i == "2":
            print("""
Sorry, only the Introduction has been implemented. We'll get to this another time!""")
        elif i == "3":
            print("""
Sorry, only the Introduction has been implemented. We'll get to this another time!""")
        elif i == "4":
            print("""
Sorry, only the Introduction has been implemented. We'll get to this another time!""")
        elif i == "5":
            print("""
Sorry, only the Introduction has been implemented. We'll get to this another time!""")
        elif i == "6":
            print("""
Sorry, only the Introduction has been implemented. We'll get to this another time!""")
        elif i == "0":
            break
        else:
            print("""
Unexpected input. Please try again.""")
    close = input("""
Thank you for visiting! Press Enter to exit.""")


def Intro():
    print("""
Pointers are among the most consistently confusing topics for new programmers. Even so,
they don’t have to be! Once you get some practice you’ll see just how uncomplicated they
really are and can work on implementing them into your own programs.

    Pointers: are objects whose values are the addresses of another object in memory.

How are they used?
Pointers can be initialized using the following syntax:

    (Type) (Star) (Variable Name) = &(What You're Pointing To);
    int      *    ptr             = &x;
    int* p = &y;

The “address-of” operator, ‘&,’ gets the address of the variable.
Note that the star can be anywhere between the type and variable name.

""")
    c = input("Press Enter to continue...")
    p1 = True
    while p1:
        prob1 = input("""
int main()
{
short s = 7;
int i = 3;
int* ptr = &i;
short z = 7;
/* Create a pointer to short z */
}

Fill in the comment with a pointer to short z. While the star may go anywhere between
the type and the pointer name, please put the pointer immediately following the type.
For example, "int* ptr" instead or "int *ptr".

""")
        p1_1 = prob1.split()
        if p1_1[0] == "short*" and p1_1[1] != "z" and p1_1[2] == "=" and p1_1[3] == "&z;":
            p1 = False
        else:
            print("""
Incorrect. Try again!
""")

    print("""
Nice job! You just initialized a C++ pointer!
""")


Main()
