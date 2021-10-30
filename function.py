def convert_seconds(x):
    hour = x // 3600
    minute = x // 60 - hour * 60
    second = x - (hour * 3600 + minute * 60)
    return '{:.0f} hours, {:.0f} minutes, {:.1f} secondes'.format(hour, minute, second)