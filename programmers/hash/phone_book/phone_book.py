def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        lenI = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][0:lenI]: return False
    return True