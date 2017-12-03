''' What floor do the instructions take Santa to? '''
def santaFloor(floor_data):
    up_count = floor_data.count("(")
    down_count = floor_data.count(")")
    return up_count - down_count
