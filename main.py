def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count    

def count_characters(text):
    characters_dic = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in characters_dic:
            characters_dic[char] += 1
        else:
            characters_dic[char] = 1
    return characters_dic

def get_path(path):
    with open(path, "r") as file:
        return file.read()

def sort_on(d):
    return d["num"]      

def sorted(dict):
    lista = []
    for item in dict:
        if item.isalpha():
            lista.append({"character" : item, "num" : dict[item]})    
            
    lista.sort(reverse=True, key=sort_on)            
    return lista

def main():
    book_path = "books/frankenstein.txt"
    contents = get_path(book_path)
    num_words = count_words(contents)  
    dict_char = count_characters(contents)
    sorted_list_dict_char = sorted(dict_char)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for index in sorted_list_dict_char:
        print(f"The {index["character"]} character was found {index["num"]} times")
    print("--- End report")    

main()        
