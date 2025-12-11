def get_formatted_name(first_name, middle_name, last_name):
    """return a full name, neatly formatted"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


#to make the function above to take an optional argument
def get_book_info(title, author, edition=''):
    """return a full name, neatlfy formatted"""
    if edition:
        book_info = f"{title} {author} {edition}"
    else:
        book_info = f"{title} {author}"
    return book_info.title()
book = get_book_info('Rich Dad', 'Robert Kiyosaki')
print(book)

book = get_book_info('the art of speaking', 'maddison grey', '7th edition')
print(book)