
r = filter(lambda x : x > 2 ,range(1,8))
print(list(r))

def ft_filter(func,iterable):
    for it in iterable:
        if(func(it)):
            yield it

def man():
      print(list(ft_filter(lambda x: x % 2 == 0, range(10))))