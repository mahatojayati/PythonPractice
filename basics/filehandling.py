'''with open("Hobbies.docx", "w") as file:
    file.write("My hobbies include reading, hiking, and painting.")
    content = file.read()
    print(content)'''
# The above code will raise an error because the file is opened in write mode ('w').
# To read the content, we should open the file in read mode ('r').
# Correcting the code to read the content after writing
with open("Hobbies.docx", "w") as file:
    file.write("My hobbies include reading, hiking, and painting.")
with open("Hobbies.docx", "r") as file:
    content = file.read()
    print(content)
with open("Hobbies.docx", "a") as file:
    file.write("Adding more notes!\n")
    print("Content appended successfully.")
with open("Hobbies.docx", "r") as file:
    content = file.read()
    print(content)
    


    
