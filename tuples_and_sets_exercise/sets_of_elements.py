m, n = map(int, input().split())

n_set = set([int(input()) for _ in range(n)])
m_set = set([int(input()) for _ in range(m)])

intersection = n_set.intersection(m_set)

print(*intersection, sep='\n')
