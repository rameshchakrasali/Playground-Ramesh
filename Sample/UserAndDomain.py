email_id = input("Enter your mail is: ")
List = email_id.split("@")
#print(List)
user_name = List[0]
domain_name=List[1]
print("User Name:",user_name)
print("Domain Name:",domain_name)

user_name = email_id[:email_id.index("@")]
domain_name = email_id[email_id.index(("@"))+1:]
print("User Name:",user_name)
print("Domain Name:",domain_name)