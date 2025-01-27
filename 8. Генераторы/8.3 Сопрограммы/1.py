def grep(pattern):
    while True:
        text = yield
        if not text:
            break
        for t in text.lower().split():
            if pattern.lower() in t:
                print(text)
                break
