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
    frontier = []
    box_path = {}
    current_cost = {}
    detail_points = {}

    start_box = None
    end_box = None

    

    # return distance from previous point to new detail point
    def cost(current, next):
        return math.sqrt((current[0] - next[0])**2 + (current[1] - next[1])**2)
    


    # Find Starting box and ending box
    for box in mesh["boxes"]:
        if box[0] <= source_point[0] and box[2] <= source_point[1] and box[1] >= source_point[0] and box[3] >= source_point[1]:
            start_box = box
            heappush(frontier, (0, box))
            box_path[box] = None
            detail_points[box] = source_point
            current_cost[box] = 0

        if box[0] <= destination_point[0] and box[2] <= destination_point[1] and box[1] >= destination_point[0] and box[3] >= destination_point[1]:
            end_box = box
            detail_points[box] = destination_point



    # Breadth First Search with priority Queue (Dijkstra's Algorithm)
    while len(frontier) > 0:
        priority, current_box = heappop(frontier)

        if current_box == end_box:
            break
        
        for next in mesh["adj"][current_box]:
            current_dp = detail_points[current_box]
            next_dp = get_detail_point(current_dp, current_box, next)
            new_cost = current_cost[current_box] + cost(current_dp, next_dp)
            if (next not in box_path.keys()) or (new_cost < current_cost[next]):
                detail_points[next] = next_dp
                current_cost[next] = new_cost
                priority = cost(detail_points[end_box], next)
                heappush(frontier, (priority, next))
                box_path[next] = current_box


                





    if end_box not in box_path or start_box not in box_path:
        print("No path!")
    else:
        current = end_box
        path.append(destination_point)
        while current != start_box: 
            path.append(detail_points[current])
            current = box_path[current]
        path.append(source_point)




    return path, box_path.keys()











def get_detail_point(current_point, current, adj):
     # if we add an adjacent box we add the detail points to the dictionary with the key of the current point

    #Box (x1, x2, y1, y2)
    #b1 = current
    #b2 = adj

    #the range of two points for each adjacent box as a legal path to connect them
    #(Max(b1x1, b2x1), (Max(b1y1, b2y1)))
    #(Min(b1x2, b2x2), (Min(b1y2, b2y2)))

    x1, y1 = (max(current[0], adj[0]), max(current[2], adj[2]))
    x2, y2 = (min(current[1], adj[1]), min(current[3], adj[3]))
    rx, ry = (0,0)

    if current_point[0] < x1:
        rx = x1
    elif current_point[0] > x2:
        rx = x2
    else:
        rx = current_point[0]

    if current_point[1] < y1:
        ry = y1
    elif current_point[1] > y2:
        ry = y2
    else:
        ry = current_point[1]

    return (rx, ry)