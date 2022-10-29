def toWords(n):
    units = ["", "one", "two", "three", "four","five","six","seven","eight", "nine"]
    ten_units = ["ten","eleven","twelve","thirteen","fourteen","quarter","sixteen","seventeen","eighteen","nineteen"]
    
    n_units = n % 10
    
    if n < 10:
        return units[n_units]
    elif 10 <= n < 20:
        return ten_units[n_units]
    elif 20 <= n < 30:
        return f"twenty {units[n_units]}"
    elif n == 30:
        return "half"


def sufMinutes(m):
    number = toWords(m)
    
    if number == "quarter" or number == "half":
        return number
    elif number == "one":
        return f"{number} minute"
    else:
        return f"{number} minutes"


def timeInWords(h, m):
    if m == 0:
        return f"{toWords(h)} o' clock"
    elif 1 <= m <= 30:
        return f"{sufMinutes(m)} past {toWords(h)}"
    elif 30 < m:
        return f"{sufMinutes(60 - m)} to {toWords(h + 1)}"
   
    
print(timeInWords(5, 47))
print(timeInWords(3, 00))
print(timeInWords(7, 15))