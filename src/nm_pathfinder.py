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
    boxes = []
    frontier = []
    start_box = None
    end_box = None


    # Find Starting box and ending box
    for box in mesh["boxes"]:
        if box[0] <= source_point[0] and box[2] <= source_point[1] and box[1] >= source_point[0] and box[3] >= source_point[1]:
            start_box = box
            frontier.append(box)
            boxes.append(box)
        if box[0] <= destination_point[0] and box[2] <= destination_point[1] and box[1] >= destination_point[0] and box[3] >= destination_point[1]:
            end_box = box

    if start_box == None or end_box == None:
        print("No path!")


    while len(frontier) > 0:
        current = frontier.pop(0)
        if current == end_box:
            print("End?")
            break
        for adj in mesh["adj"][current]:
            if adj not in boxes:
                frontier.append(adj)
                boxes.append(adj)
                print("new box")
        print(frontier)





    return path, boxes
