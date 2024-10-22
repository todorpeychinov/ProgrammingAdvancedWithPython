def drawing_figures(n):
    if n <= 0:
        return 0
    print("*" * n)
    drawing_figures(n-1)
    print("#" * n)


n = int(input())
drawing_figures(n)