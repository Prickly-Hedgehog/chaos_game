import math
import matplotlib.pyplot as plt
import random
import time

def generate_polygon(n_sides, radius=10):
    vertices_x = [radius * math.cos(2 * math.pi * i / n_sides) for i in range(n_sides)]
    vertices_y = [radius * math.sin(2 * math.pi * i / n_sides) for i in range(n_sides)]
    angle_of_rotation = math.atan2(vertices_y[1] - vertices_y[0], vertices_x[1] - vertices_x[0])
    vertices_x_rotated = []
    vertices_y_rotated = []

    for i in range(n_sides):
        x_rot = vertices_x[i] * math.cos(-angle_of_rotation) - vertices_y[i] * math.sin(-angle_of_rotation)
        y_rot = vertices_x[i] * math.sin(-angle_of_rotation) + vertices_y[i] * math.cos(-angle_of_rotation)    
        vertices_x_rotated.append(x_rot)
        vertices_y_rotated.append(y_rot)
    
    return vertices_x_rotated, vertices_y_rotated

def fractal(fractal_type, n, r):
    points_x = []
    points_y = []
    point =  [random.uniform(min(vertices_x), max(vertices_x)), random.uniform(min(vertices_y), max(vertices_y))]
    previous_vertices = [None, None]

    for _ in range(round(points_number)):
        random_vertex_index = random.randint(0, n - 1)
        if fractal_type == "star" or fractal_type == "square":
            if previous_vertices[0] == previous_vertices[1] and previous_vertices[0] is not None:
                while abs(random_vertex_index - previous_vertices[0]) == 1 or abs(random_vertex_index - previous_vertices[0]) == n - 1:
                    random_vertex_index = random.randint(0, n - 1)

        previous_vertices[1] = previous_vertices[0]
        previous_vertices[0] = random_vertex_index
        random_vertex = [vertices_x[random_vertex_index], vertices_y[random_vertex_index]]
        point = [(point[0] + random_vertex[0])*r, (point[1] + random_vertex[1])*r]
        points_x.append(point[0])
        points_y.append(point[1])

    return points_x, points_y

if __name__ == "__main__":
    
    selected = False

    while not selected :
        selected = True
        selected_fractal = input(
"""(1) Square
(2) Star
(3) Sierpinski
Enter fractal to generate: """).lower()
        
        match selected_fractal:
            
            case "1":
                n = 4 #Number of sides of the polygon
                r = 1/2 #How far a point jumps to a vertex. e.g. when r=1/2, the point will jump to the midpoint between it and the selected vertex
                selected_fractal = "square"
            case "2":
                n = 5
                r = 1/2
                selected_fractal = "star"
            case "3":
                n = 3
                r = 1/2
                selected_fractal = "sierpinski"
            case _:
                print("Invalid fractal")
                selected = False

    points_number = int(input("Enter number of points to simulate (*1,000,000): ")) * 1000000
    start = time.time()
    polygon_radius = 10
    vertices_x, vertices_y = generate_polygon(n, polygon_radius)
    all_x, all_y = fractal(selected_fractal, n, r)
    end = time.time()
    print(f"Chaos game simulation time: {round(end-start, 3)} seconds")
    plt.gcf().canvas.manager.set_window_title("Chaos game fractal")
    points_alpha = 200000/points_number
    if points_alpha > 1:
        points_alpha = 1
    plt.plot(all_x, all_y, ',k', alpha = points_alpha)
    plt.axis("equal")
    plt.show()