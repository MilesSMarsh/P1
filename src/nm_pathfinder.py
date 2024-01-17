def find_path (source_point, destination_point, mesh):

    """
    Searches for a path from source_point to destination_point through the mesh

    Args:
        source_point: starting point of the pathfinder
        destination_point: the ultimate goal the pathfinder must reach
        mesh: pathway constraints the path adheres to

    Returns:

        A path (list of points) from source_point to destination_point if exists
        A list of boxes explored by the algorithm
    """

    path = []
    boxes = {}
    frontier = []
    detail_points = {}

    start_box = None
    end_box = None

    current_dp = source_point

    #Box (x1, x2, y1, y2)

    # Find Starting box and ending box
    for box in mesh["boxes"]:
        if box[0] <= source_point[0] and box[2] <= source_point[1] and box[1] >= source_point[0] and box[3] >= source_point[1]:
            start_box = box
            frontier.append(box)
            boxes[box] = None
            detail_points[box] = source_point

        if box[0] <= destination_point[0] and box[2] <= destination_point[1] and box[1] >= destination_point[0] and box[3] >= destination_point[1]:
            end_box = box


    # breadth first search
    while len(frontier) > 0:
        current = frontier.pop(0)

        if current == end_box:
            break

        for adj in mesh["adj"][current]:
            if adj not in boxes.keys():
                frontier.append(adj)
                boxes[adj] = current

                dp = get_detail_point(current_dp, current, adj)
                detail_points[adj] = dp
        current_dp = detail_points[current]
                
    if end_box not in boxes:
        print("No path!")

    else:
        current = end_box
        path.append(destination_point)
        while current != start_box: 
            path.append(detail_points[current])
            current = boxes[current]
        path.append(source_point)




    return path, boxes.keys()



def get_detail_point(current_point, current, adj):
     # if we add an adjacent box we add the detail points to the dictionary with the key of the current point

    #Box (x1, x2, y1, y2)
    #b1 = current
    #b2 = adj

    #the range of two points for each adjacent box as alegal path to connect them
    #(Max(b1x1, b2x1), (Max(b1y1, b2y1)))
    #(Min(b1x2, b2x2), (Min(b1y2, b2y2)))

    point1 = (max(current[0], adj[0]), max(current[2], adj[2]))
    point2 = (min(current[1], adj[1]), min(current[3], adj[3]))

    if point1[0] == point2[0]:
        if current_point[0] < point1[0]:
            print("1")
            return point1
        elif current_point[0] < point2[0]:
            print("test")
            return (current_point[0], point1[1])
        else:
            print("2")
            return point2
    elif point1[1] == point2[1]:
        if current_point[1] < point1[1]:
            print("3")
            return point1
        elif current_point[1] < point2[1]:
            print("test2")
            return (point1[0], current_point[1])
        else:
            print("4")
            return point2
    else:
        print("no detail point")()