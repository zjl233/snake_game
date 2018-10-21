# for debug in linux terminal
def log(*args, **kwargs):
    from datetime import datetime
    dt = datetime.now()
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def cycle(n, mn, mx):
    if n < mn:
        return mx
    elif n > mx:
        # render at board can cause error
        return mn
    else:
        return n
