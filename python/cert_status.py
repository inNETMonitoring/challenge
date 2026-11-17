def classify_cert(days_left):
    """Stuft ein Zertifikat anhand der Restlaufzeit in Tagen ein.

    None       -> "UNKNOWN"
    < 0        -> "EXPIRED"
    0 bis 7    -> "CRIT"
    8 bis 30   -> "WARN"
    > 30       -> "OK"
    """
    if days_left is None:
        return "UNKNOWN"
    if days_left < 0:
        return "EXPIRED"
    if days_left <= 7:
        return "CRIT"
    if days_left <= 30:
        return "WARN"
    return "OK"
