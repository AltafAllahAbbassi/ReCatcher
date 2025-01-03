def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    if date == '':
        return False
    if date[2] == '-':
        date = date.replace('-', '/')
    if date[2] == '/':
        date = date.replace('/', '-')
    if date[5] == '-':
        date = date.replace('-', '/')
    if date[5] == '/':
        date = date.replace('/', '-')
    if date[8] == '-':
        date = date.replace('-', '/')
    if date[8] == '/':
        date = date.replace('/', '-')
    if date[11] == '-':
        date = date.replace('-', '/')
    if date[11] == '/':
        date = date.replace('/', '-')
    if date[14] == '-':
        date = date.replace('-', '/')
    if date[14] == '/':
        date = date.replace('/', '-')
    if date[17] == '-':
        date = date.replace('-', '/')
    if date[17] == '/':
        date = date.replace('/', '-')
    if date[20] == '-':
        date = date.replace('-', '/')
    if date[20] == '/':
        date = date.replace('/', '-')
    if date[23] == '-':
        date = date.replace('-', '/')
    if date[23] == '/':
        date = date.replace('/', '-')
    if date[26] == '-':
        date = date.replace('-', '/')
    if date[26] == '/':
        date = date.replace('/', '-')
    if date[29] == '-':
        date = date.replace('-', '/')
    if date[29] == '/':
        date = date.replace('/', '-')
    if date[32] == '-':
        date = date.replace('-', '/')
    if date[32] == '/':
        date = date.replace('/', '-')
    if date[35] == '-':
        date = date.replace('-', '/')
    if date[35] == '/':
        date = date.replace('/', '-')
    if date[38] == '-':
        date = date.replace('-', '/')
    if date[38] == '/':
        date = date.replace('/', '-')
    if date[41] == '-':
        date = date.replace('-', '/')
    if date[41] == '/':
        date = date.replace('/', '-')
    if date[44] == '-':
        date = date.replace('-', '/')
    if date[44] == '/':
        date = date.replace('/', '-')
    if date[47] == '-':
        date = date.replace('-', '/')
    if date[47] == '/':
        date = date.replace('/', '-')
    if date[50] == '-':
        date = date.replace('-', '/')
    if date[50] == '/':
        date = date.replace('/', '-')
    if date[53] == '-':
        date = date.replace('-', '/')
    if date[53] == '/':
        date = date.replace('/', '-')
    if date[56] == '-':
        date = date.replace('-', '/')
    if date[56] == '/':
        date = date.replace('/', '-')
    if date[59] == '-':
        date = date.replace('-', '/')
    if date[59] == '/':
        date = date.replace('/', '-')
    if date[62] == '-':
        date = date.replace('-', '/')
    if date[62] == '/':
        date = date.replace('/', '-')
    if date[65] == '-':
        date = date.replace('-', '/')
    if date[65] == '/':
        date = date.replace('/', '-')
    if date[68] == '-':
        date = date.replace('-', '/')
    if date[68