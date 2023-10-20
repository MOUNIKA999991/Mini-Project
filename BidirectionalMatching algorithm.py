class BidirectionalMatcher:
    def __init__(self, info_list):
        self.info_list = info_list
    def get_all_substrings(self, input_string):
        substrings = set()
        for i in range(len(input_string)):
            for j in range(i + 1, len(input_string) + 1):
                substrings.add(input_string[i:j])
        return sorted(substrings, key=len, reverse=True)
    def match(self, password):
        substring_list = self.get_all_substrings(password)
        for substring in substring_list:
            for i, info in enumerate(self.info_list):
                if substring.lower() == info.lower():  
                    return f"[{i}]", len(password)  
        return "No match", len(password)  
info_list = []
name = input("Enter name: ")
birthdate = input("Enter birthdate: ")
identity_number = input("Enter identity number: ")
email = input("Enter email: ")
telephone = input("Enter telephone number: ")
info_list.extend([name, birthdate, identity_number, email, telephone])
matcher = BidirectionalMatcher(info_list)
password = input("Enter a password: ")
result_tag, result_length = matcher.match(password)
print("Tag:", result_tag)
print("Complete Length of Password:", result_length)
