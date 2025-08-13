# def toPalindrome(user):
#     var1 = user
#     original = ""
#     for i in var1:
#         if i.isalnum():
#             original += i.lower()

#     if original == original[::-1]:
#         return "true"
#     else:
#         return "false"

# user ="Anne, I vote more cars race Rome-to-Vienna"
# print(toPalindrome(user))


# Input: s = "A man, a plan, a canal: Panama"

# Output: True (after processing, it becomes "amanaplanacanalpanama")


def check_pelindrome(n):
    val = n
    original = ""
    for i in val:
        if i.isalnum():
           original += i.lower()

    if original == original[::-1]:
        return original
    else:
        return False

n= "A man, a plan, a canal: Panama"
print(check_pelindrome(n))

