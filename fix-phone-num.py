import pytest

def fix_phone_num(phone_num_to_fix):
    # 1. First, check if it's 11 digits and handle the country code
    if len(phone_num_to_fix) == 11:
        # The phone number is of length 11, so check if it has the "1" country code.
        if phone_num_to_fix[0] != "1":
            # The country code wasn't a "1", so the number is invalid.
            raise ValueError(f"phone numbers of length 11 must begin with a 1, got \"{phone_num_to_fix}\"")
        # Strip off the country code "1" from the beginning.
        # Resulting string should be of length 10 to work with formatting code below.
        phone_num_to_fix = phone_num_to_fix[1:]

    # 2. Now check if the remaining string is exactly 10 digits
    if len(phone_num_to_fix) != 10:
        raise ValueError(f"phone number must be length 10; got \"{phone_num_to_fix}\" which is of length {len(phone_num_to_fix)}")
    
    # 3. Ensure it only contains numbers
    if not phone_num_to_fix.isdigit():
        raise ValueError(f"phone number must only contain digits; got \"{phone_num_to_fix}\"")

    # 4. Format the 10-digit string: split the parts, then recombine and return
    area_code = phone_num_to_fix[0:3]  # 512 (first three digits)
    three_part = phone_num_to_fix[3:6]  # 555 (next three digits)
    four_part = phone_num_to_fix[6:]  # 8823 (last four digits)

    fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part

    return fixed_num


# --- TESTS ---
def test_fix_phone_num():
    assert fix_phone_num("5125558823") == '(512) 555 8823'

def test_fix_phone_num2():
    assert fix_phone_num("5554429876") == '(555) 442 9876'

def test_fix_phone_num3():
    assert fix_phone_num("3216543333") == '(321) 654 3333'

def test_short_num_error():
    with pytest.raises(ValueError):
        fix_phone_num("51")

def test_long_num_error():
    with pytest.raises(ValueError):
        fix_phone_num("01234567890")

# Adding a test specifically for the new 11-digit fix!
def test_country_code():
    assert fix_phone_num("15125558823") == '(512) 555 8823'
