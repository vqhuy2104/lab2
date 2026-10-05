
import math


# ============================================================
# LAB 2: KHÔNG GIAN VECTOR, ÁNH XẠ TUYẾN TÍNH
# ============================================================


# ============================================================
# BÀI 1: TÍNH TỔ HỢP TUYẾN TÍNH
# ============================================================

def compute_linear_combination(B, c):
    dim = len(B[0])
    v = [0.0] * dim

    for i in range(len(B)):
        for j in range(dim):
            v[j] += c[i] * B[i][j]

    return v


# ============================================================
# BÀI 2: KIỂM TRA ĐỘC LẬP / PHỤ THUỘC TUYẾN TÍNH
# ============================================================

def is_linearly_dependent_2d(v1, v2):
    det = v1[0] * v2[1] - v1[1] * v2[0]

    if abs(det) < 1e-9:
        return True
    else:
        return False


# ============================================================
# BÀI 3: TÌM KERNEL VÀ NULLITY
# ============================================================

def rref_matrix(A):
    A = [row[:] for row in A]

    rows = len(A)
    cols = len(A[0])
    pivot_row = 0

    for col in range(cols):

        if pivot_row >= rows:
            break

        pivot = pivot_row

        while pivot < rows and abs(A[pivot][col]) < 1e-9:
            pivot += 1

        if pivot == rows:
            continue

        # Đổi dòng
        A[pivot_row], A[pivot] = A[pivot], A[pivot_row]

        # Chia dòng pivot cho phần tử pivot
        pivot_value = A[pivot_row][col]

        for j in range(cols):
            A[pivot_row][j] /= pivot_value

        # Khử các dòng còn lại
        for i in range(rows):

            if i != pivot_row:

                factor = A[i][col]

                for j in range(cols):
                    A[i][j] -= factor * A[pivot_row][j]

        pivot_row += 1

    # Làm tròn kết quả
    for i in range(rows):
        for j in range(cols):

            if abs(A[i][j]) < 1e-9:
                A[i][j] = 0.0

            A[i][j] = round(A[i][j], 6)

    return A


def find_kernel_basis_2x3(A):
    R = rref_matrix(A)

    print("Ma trận RREF:")

    for row in R:
        print(row)

    # Theo yêu cầu của đề:
    # RREF(A) = [1 0 c1]
    #           [0 1 c2]

    c1 = R[0][2]
    c2 = R[1][2]

    # Đặt x3 = 1
    basis_vector = [-c1, -c2, 1.0]

    # Có một biến tự do x3
    nullity = 1

    return [basis_vector], nullity


# ============================================================
# BÀI 4: PHÉP CO GIÃN
# ============================================================

def scale_points(points, sx, sy):
    result = []

    for point in points:

        x = point[0]
        y = point[1]

        new_x = x * sx
        new_y = y * sy

        result.append([
            round(new_x, 2),
            round(new_y, 2)
        ])

    return result


# ============================================================
# BÀI 4: PHÉP XOAY
# ============================================================

def rotate_points(points, angle_degrees):

    # Đổi độ sang radian
    rad = math.radians(angle_degrees)

    cos_value = math.cos(rad)
    sin_value = math.sin(rad)

    result = []

    for point in points:

        x = point[0]
        y = point[1]

        new_x = x * cos_value - y * sin_value
        new_y = x * sin_value + y * cos_value

        result.append([
            round(new_x, 2),
            round(new_y, 2)
        ])

    return result


# ============================================================
# BÀI 5: TẠO MA TRẬN AFFINE 3x3
# ============================================================

def create_affine_matrix(sx, sy, angle_deg, tx, ty):

    # Đổi góc sang radian
    rad = math.radians(angle_deg)

    cos_value = math.cos(rad)
    sin_value = math.sin(rad)

    # Ma trận biến đổi Affine
    matrix = [
        [
            sx * cos_value,
            -sy * sin_value,
            tx
        ],
        [
            sx * sin_value,
            sy * cos_value,
            ty
        ],
        [
            0,
            0,
            1
        ]
    ]

    # Làm tròn
    for i in range(3):
        for j in range(3):
            matrix[i][j] = round(matrix[i][j], 4)

    return matrix


# ============================================================
# BÀI 5: BIẾN ĐỔI BOUNDING BOX
# ============================================================

def transform_bounding_box(bbox, affine_matrix):

    result = []

    for point in bbox:

        x = point[0]
        y = point[1]

        # Chuyển sang tọa độ đồng nhất
        # [x, y] -> [x, y, 1]

        new_x = (
            affine_matrix[0][0] * x
            + affine_matrix[0][1] * y
            + affine_matrix[0][2]
        )

        new_y = (
            affine_matrix[1][0] * x
            + affine_matrix[1][1] * y
            + affine_matrix[1][2]
        )

        result.append([
            round(new_x, 2),
            round(new_y, 2)
        ])

    return result


# ============================================================
# CHƯƠNG TRÌNH CHÍNH
# ============================================================

def main():

    print("=" * 60)
    print("LAB 2: KHÔNG GIAN VECTOR, ÁNH XẠ TUYẾN TÍNH")
    print("=" * 60)


    # ========================================================
    # BÀI 1
    # ========================================================

    print("\n")
    print("========== BÀI 1 ==========")
    print("TÍNH TỔ HỢP TUYẾN TÍNH")

    B = [
        [1, 0],
        [1, 1]
    ]

    c = [-2, 7]

    result = compute_linear_combination(B, c)

    print("B =", B)
    print("c =", c)
    print("Vector kết quả v =", result)


    # ========================================================
    # BÀI 2
    # ========================================================

    print("\n")
    print("========== BÀI 2 ==========")
    print("KIỂM TRA ĐỘC LẬP / PHỤ THUỘC TUYẾN TÍNH")

    v1 = [2, 4]
    v2 = [4, 8]

    result = is_linearly_dependent_2d(v1, v2)

    print("v1 =", v1)
    print("v2 =", v2)

    if result:
        print("Kết luận: Hai vector phụ thuộc tuyến tính.")
    else:
        print("Kết luận: Hai vector độc lập tuyến tính.")


    # Trường hợp thứ hai
    v3 = [2, 4]
    v4 = [1, 5]

    result = is_linearly_dependent_2d(v3, v4)

    print("\nv3 =", v3)
    print("v4 =", v4)

    if result:
        print("Kết luận: Hai vector phụ thuộc tuyến tính.")
    else:
        print("Kết luận: Hai vector độc lập tuyến tính.")


    # ========================================================
    # BÀI 3
    # ========================================================

    print("\n")
    print("========== BÀI 3 ==========")
    print("TÌM KERNEL VÀ NULLITY")

    A = [
        [1, 2, 3],
        [2, 4, 6]
    ]

    print("Ma trận A:")

    for row in A:
        print(row)

    kernel_basis, nullity = find_kernel_basis_2x3(A)

    print("Cơ sở của Ker(f):", kernel_basis)
    print("Nullity:", nullity)


    # ========================================================
    # BÀI 4
    # ========================================================

    print("\n")
    print("========== BÀI 4 ==========")
    print("PHÉP CO GIÃN VÀ XOAY")

    points = [
        [1, 1],
        [2, 2],
        [3, 1]
    ]

    print("Các điểm ban đầu:")
    print(points)

    # Co giãn
    scaled_points = scale_points(
        points,
        2,
        3
    )

    print("\nSau khi co giãn:")
    print(scaled_points)

    # Xoay
    rotated_points = rotate_points(
        points,
        90
    )

    print("\nSau khi xoay 90 độ:")
    print(rotated_points)


    # ========================================================
    # BÀI 5
    # ========================================================

    print("\n")
    print("========== BÀI 5 ==========")
    print("AFFINE TRANSFORMATION")

    sx = 2
    sy = 2
    angle_deg = 45
    tx = 10
    ty = 5

    affine_matrix = create_affine_matrix(
        sx,
        sy,
        angle_deg,
        tx,
        ty
    )

    print("Ma trận Affine 3x3:")

    for row in affine_matrix:
        print(row)

    # Bounding Box
    bbox = [
        [1, 1],
        [4, 1],
        [4, 4],
        [1, 4]
    ]

    print("\nBounding Box ban đầu:")
    print(bbox)

    transformed_bbox = transform_bounding_box(
        bbox,
        affine_matrix
    )

    print("\nBounding Box sau khi biến đổi:")
    print(transformed_bbox)


    # ========================================================
    # KẾT THÚC
    # ========================================================

    print("\n")
    print("=" * 60)
    print("ĐÃ HOÀN THÀNH LAB 2")
    print("=" * 60)


# ============================================================
# CHẠY CHƯƠNG TRÌNH
# ============================================================

if __name__ == "__main__":
    main()