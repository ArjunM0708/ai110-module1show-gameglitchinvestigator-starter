def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50  # TODO: Fixed bug — Normal was 1-100 and Hard was 1-50; swapped so Normal=1-50, Hard=1-100
    if difficulty == "Hard":
        return 1, 100  # TODO: Fixed bug — Hard was 1-50, now correctly uses the wider range 1-100
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    guess = int(guess)   # TODO: Fixed bug — both values cast to int to prevent broken string comparison when secret was passed as a string on even attempts
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📉 Go LOWER!"  # TODO: Fixed bug — hint was inverted, previously said "Go HIGHER!" when guess was too high
    else:
        return "Too Low", "📈 Go HIGHER!"  # TODO: Fixed bug — hint was inverted, previously said "Go LOWER!" when guess was too low


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number  # TODO: Fixed bug — was using attempt_number + 1, which shifted win points down by 10 unnecessarily
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return max(0, current_score - 5)  # TODO: Fixed bug — "Too High" on even attempts previously rewarded +5 points; now both wrong outcomes deduct 5, floored at 0

    return current_score
