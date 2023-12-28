# Это файл с проверкой твоего решения
# Постарайся ничего здесь не менять! =)

if __name__ == '__main__':
    import hashlib
    N = 1
    answers = None
    with open('materials/task2/answers.txt', 'r') as f:
        answers = f.read().splitlines()

    while True:
        try:
            ans = str(N) + input().lower()
            hashed_string = hashlib.sha256(ans.encode('utf-8')).hexdigest()
            
            if hashed_string == answers[N-1]:
                print(f"#{N} is OK!")
            else:
                print(f"#{N} is WRONG!")
                print(f"{N} out of {len(answers)}...")
                print(f"Try again!")
                exit(1)
            N += 1
        except EOFError:
            break
