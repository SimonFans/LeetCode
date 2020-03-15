def dayOfWeek(S, K):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[(days.index(S) + K) % 7]

S, K = 'Saturday', 23
print(dayOfWeek(S, K))
