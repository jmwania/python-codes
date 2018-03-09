def find_page_number(pages):
    wrong_pages = []
    last_page = 0

    for page_num in pages:
        if page_num == last_page+1:
            last_page+=1
        else:
            wrong_pages.append(page_num)
    return wrong_pages
print (find_page_number([4,1,2,3,4,26,5,6]))