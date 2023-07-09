def get_month(number):
    months = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }
    try:
        return months[number]
    except KeyError as key_error:
        print(key_error, ", use only number from 1 to 12")
    except TypeError as type_error:
        print(type_error, ", use only number from 1 to 12")



months_name = get_month(9)
print(months_name)

