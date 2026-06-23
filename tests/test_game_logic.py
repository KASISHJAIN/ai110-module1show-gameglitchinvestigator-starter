from logic_utils import check_guess


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_for_high_guess():
    _, message = check_guess(60, 50)
    assert "LOWER" in message


def test_hint_for_low_guess():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message