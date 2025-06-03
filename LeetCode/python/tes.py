import random
import string

def base62_encode(number: float) -> str:
    chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
    base = len(chars)

    # Convert the float to a large integer
    number = int(number * 1e12)  # or adjust the multiplier for longer/shorter codes, we call it entropy, the more it is, the longer generation time it takes
    print(number)
    if number == 0:
        return chars[0]

    encoded = ''
    while number > 0:
        number, remainder = divmod(number, base)
        encoded = chars[remainder] + encoded

    return encoded


input_url = "https://www.example.com/some/very/long/url"
random_number = random.random()
print('random_number', random_number)
short_code_encoded = base62_encode(random_number)
short_code = short_code_encoded[:8]

print("Short code:", short_code)
