def classify_cert(days_left):
    """Stuft ein Zertifikat anhand der Restlaufzeit in Tagen ein.

    None       -> "UNKNOWN"
    < 0        -> "EXPIRED"
    0 bis 7    -> "CRIT"
    8 bis 30   -> "WARN"
    > 30       -> "OK"
    """
    raise NotImplementedError("TODO: implementieren")
