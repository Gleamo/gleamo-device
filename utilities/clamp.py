'''
clamp a `value` between a `min_value` and a `max_value`

@param numeric value – the value to clamp
@param numeric min_value – the minimum the value can be
@param numeric max_value – the maximum the value can be
'''
def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)
