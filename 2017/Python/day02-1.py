def checksum(spreadsheet):
    total = 0
    for row in spreadsheet:
        row = row.split()
        row = map(int, row)
        total += max(row) - min(row)

    return total

