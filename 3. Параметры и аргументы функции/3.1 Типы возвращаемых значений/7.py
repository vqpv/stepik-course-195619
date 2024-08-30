def create_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return s
    else:
        return f"{s}_i_{s[::-1]}"
