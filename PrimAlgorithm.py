MAX = 999999
N = 9

G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
     [4, 0, 8, 0, 0, 0, 0, 11, 0],
     [0, 8, 0, 7, 0, 4, 0, 0, 2],
     [0, 0, 7, 0, 9, 14, 0, 0, 0],
     [0, 0, 0, 9, 0, 10, 0, 0, 0],
     [0, 0, 4, 14, 10, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 1, 6],
     [8, 11, 0, 0, 0, 0, 1, 0, 7],
     [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print("\nFirst............Prim's Algorithm\n")

restart_prim = True

while restart_prim:
    st = input("Enter your starting vertex: ")
    st = ord(st)
    y = chr(st - 97)
    x = ord(y)

    selected_node = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    no_edge = 0

    selected_node[x] = True

    print("Minimum Spanning Tree: ")
    print("Edge : Weight")
    while no_edge < N - 1:

        minimum = MAX
        a = 0
        b = 0
        for m in range(N):
            if selected_node[m]:
                for n in range(N):
                    if not selected_node[n] and G[m][n]:

                        if minimum > G[m][n]:
                            minimum = G[m][n]
                            a = m
                            b = n
        print(chr(97 + a) + "-" + chr(97 + b) + "  :  " + str(G[a][b]))
        selected_node[b] = True
        no_edge += 1

    where_next = input("\nEnter 1 to restart Prim's Algorithm")
    if where_next != '1':
        restart_prim = False
