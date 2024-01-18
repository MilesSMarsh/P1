from heapq import heappush, heappop
import math



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
    dist_traveled = {}
    detail_points = {}

    start_box = None
    end_box = None

    current_dp = source_point

    def cost(next):
    # return distance from previous point to new detail point
        print(next)
        print(current_dp)
        return math.sqrt((current_dp[0] - next[0])**2 + (current_dp[1] - next[1])**2)

    #Box (x1, x2, y1, y2)

    # Find Starting box and ending box
    for box in mesh["boxes"]:
        if box[0] <= source_point[0] and box[2] <= source_point[1] and box[1] >= source_point[0] and box[3] >= source_point[1]:
            start_box = box
            heappush(frontier, (0, box))
            boxes[box] = None
            detail_points[box] = source_point
            dist_traveled[box] = 0

        if box[0] <= destination_point[0] and box[2] <= destination_point[1] and box[1] >= destination_point[0] and box[3] >= destination_point[1]:
            end_box = box


    # Breadth First Search with priority Queue (Dijkstra's Algorithm)
    while len(frontier) > 0:
        current = heappop(frontier)[1]
        print(current)

        if current == end_box:
            break

        for adj in mesh["adj"][current]:
            print(adj)
            dp = get_detail_point(current_dp, current, adj)
            detail_points[adj] = dp
            new_cost = dist_traveled[current] + cost(detail_points[adj])
            if adj not in boxes.keys() or new_cost < dist_traveled[adj]:
                dist_traveled[adj] = new_cost
                priority = new_cost
                heappush(frontier, (priority, adj))
                boxes[adj] = current


        current_dp = detail_points[current]
                





    if end_box not in boxes or start_box not in boxes:
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
    print("point1: ", point1)
    print("point2: ", point2)

    if point1[0] == point2[0]:
        if current_point[0] <= point1[0]:
            print("left of the range")
            return point1
        if current_point[0] >= point2[0]:
            print("right of the range")
            return point2
        print("verticle to the range")
        return (current_point[0], point1[1])
    
    if point1[1] == point2[1]:
        if current_point[1] <= point1[1]:
            print("above the range")
            return point1
        if current_point[1] >= point2[1]:
            print("under the range")
            return point2
        print("horizontal to the range")
        return (point1[0], current_point[1])
    
    raise Exception("No Detail Point")