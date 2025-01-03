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
            if date[5] == '-':
                if date[8] == '-':
                    if date[1] == '0' and date[3] == '0' and date[5] == '0' and date[7] == '0' and date[9] == '0':
                        return False
                    else:
                        if date[1] == '0' and date[3] == '0' and date[5] == '0' and date[7] == '0':
                            return False
                        else:
                            if date[1] == '0' and date[3] == '0' and date[5] == '0':
                                return False
                            else:
                                if date[1] == '0' and date[3] == '0':
                                    return False
                                else:
                                    if date[1] == '0':
                                        return False
                                    else:
                                        if date[3] == '0':
                                            return False
                                        else:
                                            if date[5] == '0':
                                                return False
                                            else:
                                                if date[7] == '0':
                                                    return False
                                                else:
                                                    if date[9] == '0':
                                                        return False
                                                    else:
                                                        if date[1] == '1' and date[3] == '1' and date[5] == '1' and date[7] == '1' and date[9] == '1':
                                                            return False
                                                        else:
                                                            if date[1] == '1' and date[3] == '1' and date[5] == '1' and date[7] == '1':
                                                                return False
                                                            else:
                                                                if date[1] == '1' and date[3] == '1' and date[5] == '1':
                                                                    return False
                                                                else:
                                                                    if date[1] == '1' and date[3] == '1':
                                                                        return False
                                                                    else:
                                                                        if date[1] == '1':
                                                                            return False
                                                                        else:
                                                                            if date[3] == '1':
                                                                                return False
                                                                            else:
                                                                                if date[5] == '1':
                                                                                    return False
                                                                                else:
                                                                                    if date[7] == '1':
                                                                                        return False
                                                                                    else:
                                                                                        if date[9] == '1':
                                                                                            return False
                                                                                        else:
                                                                                            if date[1] == '2' and date[3] == '2' and date[5] == '2' and date[7] == '2' and date[9] == '2':
                                                                                                return False
                                                                                            else:
                                                                                                if date[1] == '2' and date[3] == '2' and date[5] == '2' and date[7] == '2':
                                                                                                    return False
                                                                                                else:
                                                                                                    if date[1] == '2' and date[3] == '2' and date[5] == '2':
                                                                                                        return False
                                                                                                    else:
                                                                                                        if date[1] == '2' and date[3] == '2':
                                                                                                            return False
                                                                                                        else:
                                                                                                            if date[1] == '2':
                                                                                                                return False
                                                                                                            else:
                                                                                                                if date[3] == '2':
                                                                                                                    return False