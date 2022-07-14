def alnum(s_list):
    answer = False
    for ch in s_list:
        if ch.isalnum():
            answer = True
            break
    return answer


def alpha(s_list):
    answer = False
    for ch in s_list:
        if ch.isalpha():
            answer = True
            break
    return answer


def digit(s_list):
    answer = False
    for ch in s_list:
        if ch.isdigit():
            answer = True
            break
    return answer


def lower(s_list):
    answer = False
    for ch in s_list:
        if ch.islower():
            answer = True
            break
    return answer


def upper(s_list):
    answer = False
    for ch in s_list:
        if ch.isupper():
            answer = True
            break
    return answer


if __name__ == '__main__':
    s = input()

    s_list = list(s)

    print(alnum(s_list))
    print(alpha(s_list))
    print(digit(s_list))
    print(lower(s_list))
    print(upper(s_list))
