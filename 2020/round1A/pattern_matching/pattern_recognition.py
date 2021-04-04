def get_rid_of_stars(string):
    # Given a string of format *asd*asdasd*asd get rid of all the stars within this string
    return_string = ""
    for char in string :
        if char !="*" : return_string+=char
    return return_string


def func(word_list):
    beg, mid, end = "", "", ""
    for word in word_list:
        if word =="" or word=="*" or word =="**" or word =="***":
            pass
        elif word[0] =='*' == word[-1]:
            print("case *....* activated")
            for char in word[1:-1]: 
                if char!= "*" : mid+=char




        elif word[0] == "*" != word[-1]:
            print("case *.... activated")
            # Traverse through the string dividing it into 2 parts(possibly 2 parts, possibly no divison) : *....* and *......
          



            





        elif word[0] !="*" == word[-1]:
            print("case ....* activated")
            # Traverse through the string dividing it into 2 parts(possibly 2 parts, possibly no divison) : ....* and *......*



    return beg+mid+end

#cases=int(input())
file_name = "test1.txt"
file_handle = open(file_name)  
cases = int(next(file_handle))

for case in range(1,cases+1):
    nr_of_words = int(next(file_handle))
    word_list = []
    for i in range(nr_of_words):
        word = next(file_handle).split()[0]
        word_list.append(word)
    answer = func(word_list)
    print(f"Case #{case}: {answer}")
file_handle.close()