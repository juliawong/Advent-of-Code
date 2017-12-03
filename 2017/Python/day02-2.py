def checksum(spreadsheet):
    total = 0
    for row in spreadsheet:
        row = row.split()
        row = map(int, row)
        row = sorted(row)

        # Check each number in the row
        for i in range(len(row)):
            found = False
            curr = row[i]
            # Check if it divides larger numbers
            for j in range(i + 1, len(row)):
                if row[j] % curr == 0:
                    total += row[j] / curr
                    found = True
                    break
            if found:
                break

    return total

