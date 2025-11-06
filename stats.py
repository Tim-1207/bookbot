def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def counting_characters(text):
    small = text.lower()
    counts = {}  
    for char in small:
        if char not in counts:
            counts[char] = 1   
        else:
            counts[char] +=1 
    return counts

def sort_in(d):
    return d["num"]

def sort_on(unsorted_list):
    sorted_list = []
    for element in unsorted_list:
        sorted_list.append({"char": element, "num": unsorted_list[element]}) 
    sorted_list.sort(reverse=True, key=sort_in)
    return sorted_list

