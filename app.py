def num_to_en(num):
    twenty = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
              8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
              14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
            90: "ninety"}
    thousands = {0: "", 1: "thousand", 2: "million", 3: "billion", 4: "trillion", 5: "quadrillion", 6: "quintillion",
                 7: "sextillion", 8: "septillion", 9: "octillion", 10: "nonillion", 11: "decillion",
                 12: "undecillion", 13: "duodecillion", 14: "tredecillion", 15: "quattuordecillion",
                 16: "quindecillion", 17: "sexdecillion", 18: "septendecillion", 19: "octodecillion",
                 20: "novemdecillion", 21: "vigintillion"}

    output = ""
    if num[0] == "-":
        output += "minus "
    num = abs(int(num))
    num_len = len(str(num))
    scale = (num_len - 1) // 3  # 1 less than number length so that 4 - 6 digit lengths return 1 etc.
    scale_temp = scale  # to hold the original scale in memory
    d = "-"
    rem = num_len % 3  # remainder if highest quantity is not in hundreds but in units or tens

    def hundreds(x):
        h = "hundred"
        concat = ""
        last_two = x % 100
        if len(str(x)) == 3:  # hundreds
            concat += twenty[x // 100] + " " + h
        if 100 <= x <= 999 and x % 100 != 0:
            if concat != "":
                concat += " and "
        if x % 100 < 20:  # less than twenty
            concat += str(twenty[x % 100])
        elif x % 10 == 0:  # even tens
            concat += str(tens[last_two])
        else:  # everything else
            # is there a better way to obtain the tens without units?
            concat += tens[last_two - (last_two % 10)] + d + twenty[last_two % 10]
        return concat

    if num == 0:
        output += "Zero"
    else:
        for i in range(scale):
            if rem != 0:
                # consider simplifying
                output += hundreds(int(str(num)[:rem])) + " " + thousands[scale] + ", "
                # num = str(num)[rem:]
                num = ("0" * (3 - rem)) + str(num)
                rem = 0
            else:
                # consider simplifying
                current_three = int(str(num)[(scale_temp - scale) * 3:((scale_temp - scale) * 3) + 3])
                if str(current_three) != "0":
                    output += hundreds(current_three) + " " + thousands[scale] + ", "
            scale -= 1
        if int(num) % 1000 < 100:
            output = output[:-2]  # only to remove comma in case of no hundreds
            output += " and "
            output += hundreds(int(num) % 1000)
        else:
            output += hundreds(int(num) % 1000)

    output.strip()
    print(output.capitalize())


num_to_en(input("Enter integer up to 66 digits long: "))

# Old method. Couldn't get it to work
# quantity = num / (10 ** (scale*3))
# print(quantity, scale, num)
# quantity_string = f"{quantity:0f}"
# print(quantity_string)
# if quantity % 100 < 20:
#     output += twenty[int(str(quantity)[-2:])]
#     (tens[i[-2]] + "-" + ones[i[-1]])

#     quantity[-3:]

# Assert? to catch errors? Number too long or number decimal or not number
# "ands" can be simplified
# "and if no hundreds and remove last comma

# elif len(str(num))
# hundreds if output != "" or "minus": output += "and"

# integer method of extracting last digit -> n1s[i % 10])
# print(n10s[i[-2]] + "-" + ones[i[-1]])
