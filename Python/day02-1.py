''' How many total square feet of wrapping paper should the elves order? '''
def wrapping_paper_order(present_data):
    total = 0
    for present in present_data.split():
        l, w, d = (int(i) for i in present.split('x'))
        side_areas = [l*w, w*d, d*l]
        total += sum(side_areas)*2 + min(side_areas)
    return total
