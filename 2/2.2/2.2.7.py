word = list(input())
gl = [ i for i in range(len(word)) if word[i] in 'ауоыиэяюёе']

n = int(input())
for _ in range(n):
    word_new = list(input())
    if [ i for i in range(len(word_new)) if word_new[i] in 'ауоыиэяюёе'] == gl:
        print(''.join(word_new))
