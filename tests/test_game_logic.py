from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix: hint messages must point the player in the right direction ---

def test_too_high_message_says_go_lower():
    # A guess above the secret should tell the player to go LOWER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_too_low_message_says_go_higher():
    # A guess below the secret should tell the player to go HIGHER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# --- Negative inputs ---

def test_negative_guess_is_too_low():
    # -1 is below any positive secret, so it must be "Too Low" -> go HIGHER
    outcome, message = check_guess(-1, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_negative_guess_below_negative_secret():
    # Even with a negative secret, a smaller guess is still "Too Low"
    outcome, message = check_guess(-100, -10)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# --- Outside the guessing range (range 1..100) ---

def test_guess_above_range_is_too_high():
    # 150 is above the secret and above the range -> "Too High" -> go LOWER
    outcome, message = check_guess(150, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_below_range_is_too_low():
    # 0 is below the range and below the secret -> "Too Low" -> go HIGHER
    outcome, message = check_guess(0, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# --- Inside the guessing range ---

def test_in_range_guess_too_high():
    outcome, message = check_guess(75, 30)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_in_range_guess_too_low():
    outcome, message = check_guess(10, 30)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# --- Correct answer at range boundaries ---

def test_correct_answer():
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_correct_answer_at_lower_bound():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"


def test_correct_answer_at_upper_bound():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"
