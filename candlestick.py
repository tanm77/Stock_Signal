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


def has_short_upper_shadow(candle):
    """
    Determines whether the candle has a short upper shadow

    :Parameters:
        candle: Series object containing candle data

    :Returns:
        Boolean whether the candle the candle has a short upper shadow or not
    """

    return are_close(
        candle['High'],
        max(candle['Open'], candle['Close']))


def has_long_lower_shadow(candle):
    """
    Determines whether the candle has a long lower shadow

    :Parameters:
        candle: Series object containing candle data

    :Returns:
        Boolean whether the candle the candle has a long lower shadow or not
    """

    return abs(candle['Open'] - candle['Close']) < \
        min(candle['Open'], candle['Close']) - candle['Low']


def is_bullish_belt_hold(candle):
    """
    Determines whether the candle is a bullish belt hold candlestick pattern

    :Parameters:
        candle: Series object containing candle data

    :Returns:
        Boolean whether the candle is a bullish belt hold or not
    """

    return are_close(candle['Open'], candle['Low'])


def is_bearish_belt_hold(candle):
    """
    Determines whether the candle is a bearish belt hold candlestick pattern

    :Parameters:
        candle: Series object containing candle data

    :Returns:
        Boolean whether the candle is a bearish belt hold or not
    """

    return are_close(candle['Open'], candle['High'])


def is_hammer_or_hanging_man(candle):
    """
    Determines whether the candle is a hammer or a hanging man candlestick pattern

    :Parameters:
        candle: Series object containing candle data

    :Returns:
        Boolean whether the candle is a hammer or a hanging man or not
    """

    return has_short_upper_shadow(candle) and \
        has_long_lower_shadow(candle)
