def format_name(f_name, l_name):
    return (f_name + " " + l_name).title()

output = format_name("bugrahan", "gokce")
print(output)

print("---------")

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_1("hello")
print(function_2(output))