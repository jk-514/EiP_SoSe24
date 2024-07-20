import random

punctuation = ['.', ',', ':', ';', '?', '!', '(', ')', '[', ']', '{', '}', '"', "'", '-']

def train():
    successors = {}
    with open('faust.txt', 'r') as file:
        text = file.read()
        text = text.replace('\n', ' ')
        for p in punctuation:
            text = text.replace(p, '')
        text = text.lower()
        words = text.split()
        for i in range(len(words) - 1):
            w = words[i].strip()
            if w not in successors:
                successors[w] = []
            successors[w].append(words[i + 1].strip())
    return successors

def generate(successors, start, n):
    result = [start]
    for i in range(n-1):
        if start in successors:
            start = random.choice(successors[start])
            result.append(start)
        else:
            break
    return ' '.join(result)

successors = train()
print(generate(successors, 'faust', 10))
