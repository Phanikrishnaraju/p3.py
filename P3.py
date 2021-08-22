W= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    for key in d:
        print(key," = ",d[key])
        
most_frequent(W)
