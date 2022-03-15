def evaluate_html(file):
    file = open(file, "r")
    tags = []
    lineCount = 1
    errorsFound = False

    for line in file.readlines():
        for c in line:
            if c == '<':
                tags.append((c, lineCount))
            elif c == ">":
                try:
                    tags.pop()
                except IndexError:
                    print("Unpaired \">\" at line", lineCount)
                    errorsFound = True
        lineCount += 1
    if len(tags) > 0:
        errorsFound = True
        for c in tags:
            print("Unpaired \"<\" at line", c[1])
    if not errorsFound:
        print("No errors found")
    file.close()
