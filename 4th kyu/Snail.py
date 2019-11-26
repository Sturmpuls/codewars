# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
def snail(arr):
    snail = []
    while arr:
        snail += arr[0]
        arr = list(reversed(list(zip(*arr[1:]))))
    return snail
