l = ["he", "hi", "hello", "hi"]
r = [k for k in l if 'gene' in k or 'dis' in k]
print(r)


with open('project2_test.txt', 'r') as f:
    prefix = 'gene'
    for line in f:
        r = filter(lambda x: x.startswith(prefix), list(line.split()))
        print(list(r))
