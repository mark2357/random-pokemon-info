'''contains helper function returns the id from the given url'''
def get_request_id_from_url(url):
    '''returns the id from the given url (id may not be number)'''
    split_url = url.split('/')
    id_number = split_url[len(split_url) - 1]

    if id_number == '':
        # can occur when url ends in '/'
        id_number = split_url[len(split_url) - 2]

    return id_number
