course = "Python for Beginners"
print("First character: " , course[0])
print("Last Character: ", course[-1])
print("clone/print all characters: ", course[:])
print("Range: ", course[0:3])
print("Exclude first character and print till end: ", course[1:])
print("Reverse: ", course[::-1])

#String fuctions
print("Length: ", len(course))
print("LowerCase: ", course.lower())
print("UpperCase: ", course.upper())
print("Find: ", course.find("y"))
print("Replace", course.replace("P", "J"))
print("Find and print", "for" in course) #returns boolen

print("Formatted: " , f"{course} is interesting" )


