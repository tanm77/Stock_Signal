def are_close(val1, val2):
    """
    Determines whether the 2 parameter values are close to each other
    The closeness is subjective and can be changed in this function

    :Parameters:
        val1, val2: Two values to be compared for being close

    :Returns:
        Boolean whether the two values are close to each other or not
    """

    CLOSE_THRESHOLD = 0.2 / 100  # 0.2%
    return abs(val2 / val1 - 1) <= CLOSE_THRESHOLD


def bullish_belt_hold(candle):
    """
    Determines whether the candle is a bullish belt hold candlestick pattern

    :Parameters:
        candle: Series object containing candle data

    :Returns:
        Boolean whether the candle is a bullish belt hold or not
    """

    return are_close(candle['Open'], candle['Low'])
