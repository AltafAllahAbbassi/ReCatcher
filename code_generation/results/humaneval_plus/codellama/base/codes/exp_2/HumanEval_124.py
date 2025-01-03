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
    if date == "":
        return False
    else:
        if date[2] == "-":
            if date[5] == "-":
                if date[0] == "0" and date[1] == "0":
                    return False
                else:
                    if int(date[0]) < 1 or int(date[0]) > 12:
                        return False
                    elif int(date[1]) < 1 or int(date[1]) > 31:
                        return False
                    elif int(date[2]) < 1 or int(date[2]) > 31:
                        return False
                    elif int(date[3]) < 1 or int(date[3]) > 31:
                        return False
                    elif int(date[4]) < 1 or int(date[4]) > 31:
                        return False
                    elif int(date[5]) < 1 or int(date[5]) > 31:
                        return False
                    elif int(date[6]) < 1 or int(date[6]) > 31:
                        return False
                    elif int(date[7]) < 1 or int(date[7]) > 31:
                        return False
                    elif int(date[8]) < 1 or int(date[8]) > 31:
                        return False
                    elif int(date[9]) < 1 or int(date[9]) > 31:
                        return False
                    elif int(date[10]) < 1 or int(date[10]) > 31:
                        return False
                    elif int(date[11]) < 1 or int(date[11]) > 31:
                        return False
                    elif int(date[12]) < 1 or int(date[12]) > 31:
                        return False
                    elif int(date[13]) < 1 or int(date[13]) > 31:
                        return False
                    elif int(date[14]) < 1 or int(date[14]) > 31:
                        return False
                    elif int(date[15]) < 1 or int(date[15]) > 31:
                        return False
                    elif int(date[16]) < 1 or int(date[16]) > 31:
                        return False
                    elif int(date[17]) < 1 or int(date[17]) > 31:
                        return False
                    elif int(date[18]) < 1 or int(date[18]) > 31:
                        return False
                    elif int(date[19]) < 1 or int(date[19]) > 31:
                        return False
                    elif int(date[20]) < 1 or int(date[20]) > 31:
                        return False
                    elif int(date[21]) < 1 or int(date[21]) > 31:
                        return False
                    elif int(date[22]) < 1 or int(date[22]) > 31:
                        return False
                    elif int(date[23]) < 1 or int(date[23]) > 31:
                        return False
                    elif int(date[24]) < 1 or int(date[24]) > 31:
                        return False
                    elif int(date[25]) < 1 or int(date[25]) > 31:
                        return False
                    elif int(date[26]) < 1 or int(date[26]) > 31:
                        return False
                    elif int(date[27]) < 1 or int(date[27]) > 31:
                        return False
                    elif int(date[28]) < 1 or int(date[28]) > 31:
                        return False
                    elif int(date[29]) < 1 or int(date[29]) > 31:
                        return False
                    elif int(date[30]) < 1 or int(date[30