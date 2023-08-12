COLOUR_CODES = {"ALIZARIN CRIMSON": "#e32636", "AQUA": "#00ffff", "ANTIQUEWHITE1": "#ffefdb", "AUREOLIN": "fdee00",
                "BABY BLUE": "#89cff0", "BAKER-MILLER PINK": "#ff91af", "BARN RED": "#7c0a02", "BITTER LIME": "bfff00",
                "BRIGHT LILAC": "#d891ef", "CADETBLUE": "#5f9ea0"}
is_valid_input = False
while not is_valid_input:
    try:
        color_name = input("Enter color name: ").upper()
        if color_name == "":
            break
        color_code = COLOUR_CODES[color_name]
        print(f"{color_name.upper()}'s color_code is {color_code}")
    except KeyError:
        print("Invalid color name")

