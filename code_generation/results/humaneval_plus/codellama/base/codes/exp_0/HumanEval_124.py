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
    else:
        if date[2] == '-':
            date = date.replace('-', '/')
        if date[5] == '-':
            date = date.replace('-', '/')
        if date[8] == '-':
            date = date.replace('-', '/')
        if date[1] == '/' and date[4] == '/' and date[7] == '/':
            if date[0] == '0' and date[3] == '0' and date[6] == '0':
                return False
            else:
                if date[0] == '0':
                    date = date.replace('0', '')
                if date[3] == '0':
                    date = date.replace('0', '')
                if date[6] == '0':
                    date = date.replace('0', '')
                if date[1] == '1' and date[4] == '1' and date[7] == '1':
                    if int(date[2]) < 1 or int(date[2]) > 31:
                        return False
                    elif int(date[5]) < 1 or int(date[5]) > 31:
                        return False
                    elif int(date[8]) < 1 or int(date[8]) > 31:
                        return False
                    else:
                        return True
                elif date[1] == '2' and date[4] == '2' and date[7] == '2':
                    if int(date[2]) < 1 or int(date[2]) > 29:
                        return False
                    elif int(date[5]) < 1 or int(date[5]) > 29:
                        return False
                    elif int(date[8]) < 1 or int(date[8]) > 29:
                        return False
                    else:
                        return True
                elif date[1] == '3' and date[4] == '3' and date[7] == '3':
                    if int(date[2]) < 1 or int(date[2]) > 31:
                        return False
                    elif int(date[5]) < 1 or int(date[5]) > 31:
                        return False
                    elif int(date[8]) < 1 or int(date[8]) > 31:
                        return False
                    else:
                        return True
                elif date[1] == '4' and date[4] == '4' and date[7] == '4':
                    if int(date[2]) < 1 or int(date[2]) > 30:
                        return False
                    elif int(date[5]) < 1 or int(date[5]) > 30:
                        return False
                    elif int(date[8]) < 1 or int(date[8]) > 30:
                        return False
                    else:
                        return True
                elif date[1] == '5' and date[4] == '5' and date[7] == '5':
                    if int(date[2]) < 1 or int(date[2]) > 31:
                        return False
                    elif int(date[5]) < 1 or int(date[5]) > 31:
                        return False
                    elif int(date[8]) < 1 or int(date[8]) > 31:
                        return False
                    else:
                        return True
                elif date[1] == '6' and date[4] == '6' and date[7] == '6':
                    if int(date[2]) < 1 or int(date[2]) > 30:
                        return False
                    elif int(date[5]) < 1 or int(date[5]) > 30:
                        return False
                    elif int(date[8]) < 1 or int(date[8]) > 30:
                        return False
                    else:
                        return True
                elif date[1] == '7' and date[4] == '7' and date[7] == '7':
                    if int(date[2