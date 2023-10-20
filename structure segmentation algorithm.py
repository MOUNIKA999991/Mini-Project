def get_info_list():
    info_list = []
    name = input("Enter your name: ")
    info_list += get_name_list(name)
    birthdate = input("Enter your birthdate (YYYYMMDD): ")
    info_list += get_birthday_list(birthdate)
    identity_number = input("Enter your identity number: ")
    info_list += get_id_list(identity_number)
    email = input("Enter your email address: ")
    info_list += get_email_list(email)
    telephone = input("Enter your telephone number (e.g., 1234567890): ")
    info_list += get_tel_list(telephone)
    return info_list
def get_name_list(name):
    name_list = []
    name_parts = name.split()
    if len(name_parts) > 0:
        first_letter = name_parts[0][0]
        name_list.append(first_letter)
    return name_list
def get_birthday_list(birthdate):
    if len(birthdate) <= 10:
        birthday = birthdate[0:]
        return [birthday[0:4], birthday[4:6], birthday[6:]]
    return []
def get_id_list(identity_card):
    if len(identity_card) >= 14:
        return [identity_card[0:]]
    return []
def get_email_list(email):
    at_index = email.find('@')
    dot_index = email.find('.')
    if at_index != -1 and dot_index != -1:
        return [email[:at_index], email[at_index+1:dot_index]]
    return []
def get_tel_list(telephone):
    if len(telephone) >= 10:
        return [telephone[:3], telephone[3:7], telephone[7:]]
    return []
if __name__ == "__main__":
    info_list = get_info_list()
    print("Segmented Information:")
    print(info_list)

