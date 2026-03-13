import pytest


def fix_phone_num(phone_num_to_fix):
  # can only handle numbers that are exactly 10 digits long
  if len(phone_num_to_fix) != 10:
    raise ValueError("Phone number must be exactly 10 characters long")

  # can only handle numeric digits
  if not phone_num_to_fix.isdigit():
    raise ValueError("Phone number must contain only numeric digits")

  # given "5125558823". Split the parts, then recombine and return
  area_code = phone_num_to_fix[0:3]  # 512 (first three digits)
  three_part = phone_num_to_fix[3:6]  # 555 (next three digits)
  four_part = phone_num_to_fix[6:]  # 8823 (last four digits)

  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part

  return fixed_num


def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5554429876") == '(555) 442 9876'
  assert fix_phone_num("3216543333") == '(321) 654 3333'


def test_raises_error_on_badly_formatted_phone_inputs():
  with pytest.raises(ValueError):
    fix_phone_num("555-442-98761")

  with pytest.raises(ValueError):
    fix_phone_num("(3213) 654 3333")


def test_raises_value_error_on_non_digit_inputs():
  with pytest.raises(ValueError):
    fix_phone_num("334dfdee45")

  with pytest.raises(ValueError):
    fix_phone_num("abcdefghij")
