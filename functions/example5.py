from unicodedata import category


def fine_library(days_late, category):
    if category == "A":
        if days_late <= 10:
            fine = 100 * days_late
        else:
            fine = (days_late * 100) * 2
        return fine
    elif category == "B":
        if days_late <= 10:
            fine = 50 * days_late
        else:
            fine = (days_late * 50) * 2
        return fine
    elif category == "C":
        if days_late <= 10:
            fine = 10 * days_late
        else:
            fine = (days_late * 10) * 2
        return fine


if __name__=="__main__":
    days_late = int(input("enter number days book were not returned"))
    category = input("enter your choice")
    book = fine_library(days_late, category)
    print(f"The fine is {book}") 

