def most_frequent(string):
   
    frequency = {}

    
    for letter in string:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1

    
    frequency_list = list(frequency.items())

   
    def sort_by_count(item):
        return item[1]

    frequency_list.sort(key=sort_by_count, reverse=True)

    
    for letter, count in frequency_list:
        print(letter, ':', count)



input_string = input("Enter a string: ")
most_frequent(input_string)







