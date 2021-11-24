star_input= int(input("please enter number of stars "))#allow to get vallues from the users 

for current_number_of_stars in range(star_input, 0, -1):
    string_to_print = current_number_of_stars * '*'
    "***"
    string_to_print += " " * 2 * (star_input - current_number_of_stars)
    "***      "
    string_to_print += current_number_of_stars * '*'
    "***      ***"
    print(string_to_print)