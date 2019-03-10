def print_triangle(n):
    if n > 0:
        print_triangle(n - 1)
        print("*" * n)

#print_triangle(4)

def print_opposite_triangles(n):
    if n > 0:
        print("*" * n)
        print_opposite_triangles(n - 1)
        print("*" * n)

#print_opposite_triangles(4)

def print_ruler(n):
    if n == 1:
        print("-")
    else:
        print_ruler(n - 1)
        print("-" * n)
        print_ruler(n - 1)

#print_ruler(4)