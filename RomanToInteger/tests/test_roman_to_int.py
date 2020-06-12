from Solution import Solution

solution = Solution()

def test_empty_string_returns_zero():
    input_str = ""
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 0

def test_single_roman_chars_v_returns_integer():
    input_str = "V"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 5

def test_single_roman_chars_x_returns_integer():
    input_str = "X"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 10

def test_single_roman_chars_l_returns_integer():
    input_str = "L"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 50

def test_single_roman_chars_c_returns_integer():
    input_str = "C"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 100

def test_single_roman_chars_d_returns_integer():
    input_str = "D"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 500

def test_single_roman_chars_M_returns_integer():
    input_str = "M"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 1000

def test_non_existent_roman_chars_returns_zero():
    input_str = "A"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 0

def test_normal_roman_chars_returns_integer():
    input_str = "III"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 3

def test_I_before_V_returns_4():
    input_str = "IV"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 4

def test_I_before_V_returns_9():
    input_str = "IX"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 9

def test_X_before_L_returns_40():
    input_str = "XL"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 40

def test_X_before_L_returns_90():
    input_str = "XC"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 90

def test_C_before_D_returns_400():
    input_str = "CD"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 400

def test_C_before_M_returns_900():
    input_str = "CM"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 900

def test_combinations_returns_99():
    input_str = "XCIX"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 99

def test_combinations_returns_3999():
    input_str = "MMMCMXCIX"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 3999

def test_combinations_specials_returns_3999():
    input_str = "XCIV"
    actual_output = solution.romanToInt(input_str)
    assert actual_output == 94