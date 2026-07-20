# str = "Tulsi"           # 'tulsi' or '''tulsi'''

# print(str[0])           # T
# print(str[-1])          # i
# print(str[1:4])
# print(str[ :5])
# print(str[::-1])        # reverse string -> isluT

# print(len(str))             # 5
# print(str.find("ls"))       # 2
# print(str.count("l"))       # 1
# print(str.startswith("tu")) # True if(tu -> False)
# print(str.endswith("si"))   # True if(Si -> False)


# Type Conversion
# s = "hello shnaya. shnaya"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())

# print("ha" * 3)
# print("py" in s)            # False
# print("el" in s)            # True

# CHECKING FUNCTION :

# s = "Python"
# sr = "  "
# print(s.isalpha())
# print(s.isdigit())
# print(s.isalnum())      
# print(sr.isspace())     # "  "
# print(s.islower())
# print(s.isupper())

# MEMBERSHIP OPERATOR :
# mo = "Python"
# print("Py" in mo)       # True
# print("om" in mo)       # False
# print("om" not in mo)     # True

''' 
    Strip() : remove both side space,
    lstrip() : remove left space,
    rstrip() : remove right space
'''
# sp = " hello "
# print(sp)
# print(sp.strip())
# print(sp.lstrip())
# print(sp.rstrip())

# REPLACE:
# re = "I love Python"
# print(re.replace("love","like"))     #I like Python
# print(re)                           #I love Python

# CONVERT STRING INTO LIST
# sl = "Python Java C++"
# print(sl.split())       # ['Python', 'Java', 'C++']

sl2 = "Python Java C++"
print(sl2.split(","))        # ['Python Java C++']

s3 = "A,bv,cd,efvg"
print(s3.split())