import pyfiglet

# pseudocode

# ask the user to input their name
name = input("Please enter your name: ")

# ask the user to input their dream job
dream_job = input("Please enter your dream job: ")

# ask the user to input their birthday
birthday = input("Please enter your date of birth: ")

# print the inputted name in a fancy way
font_name = pyfiglet.Figlet(font='js_block_letters')
color_name = '\033[0;35m'
fancy_name = f"{color_name}{font_name.renderText(name)}"
print (fancy_name)

# print the inputted dream job in a fancy way
font_dream_job = pyfiglet.Figlet(font='slant')
color_dream_job = '\033[0;36m'
fancy_dream_job = f"{color_dream_job}{font_dream_job.renderText(dream_job)}"
print (fancy_dream_job)

# print the inputted birthday in a fancy way
font_birthday = pyfiglet.Figlet(font='bubble')
color_birthday = '\033[0;95m'
fancy_birthday = f"{color_birthday}{font_birthday.renderText(birthday)}"
print (fancy_birthday)

