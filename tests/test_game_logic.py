from logic_utils import check_guess

def test_winning_guess():
    result, message = check_guess(50, 50)
    assert result == "Win"
    assert "Correct" in message

def test_guess_too_high():
    result, message = check_guess(60, 50)
    assert result == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    result, message = check_guess(40, 50)
    assert result == "Too Low"
    assert "HIGHER" in message


def test_hint_messages_match_direction_regression():
    high_result, high_message = check_guess(75, 50)
    low_result, low_message = check_guess(25, 50)

    assert high_result == "Too High"
    assert "LOWER" in high_message
    assert low_result == "Too Low"
    assert "HIGHER" in low_message


def test_numeric_string_secret_comparison_regression():
    # Regression guard for the bug where secret could become a string.
    result, message = check_guess(9, "50")
    assert result == "Too Low"
    assert "HIGHER" in message
