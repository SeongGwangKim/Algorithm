'''

textwrap.wrap()
함수는 텍스트(문자열)의 단일 단락을 래핑하여 모든 행이 최대 너비 문자 길이가 되도록 합니다.
출력 라인 목록을 반환합니다.

textwrap.fill()
함수 는텍스트에서 단일 단락을 래핑하고 래핑된 단락을 포함하는 단일 문자열을 반환합니다.

'''
import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)