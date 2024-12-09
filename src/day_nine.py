class DayNine:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        disk = []
        for idx, digit in enumerate(self.input):
            value = int(digit)
            if idx % 2 == 0:
                fid = idx // 2
                disk += [fid] * value
            else:
                disk += [-1] * value

        blanks = [idx for idx, digit in enumerate(disk) if digit == -1]

        for blank in blanks:
            while disk[-1] == -1:
                disk.pop()
            if len(disk) <= blank:
                break
            disk[blank] = disk.pop()

        return sum(i * x for i, x in enumerate(disk))

    def part_two(self) -> int:
        files = {}
        blanks = []
        position = 0
        file_id = 0
        for idx, digit in enumerate(self.input):
            value = int(digit)
            if idx % 2 == 0:
                files[file_id] = (position, value)
                file_id += 1
                position += value
                continue

            if value != 0:
                blanks.append((position, value))
                position += value
                continue

        while file_id > 0:
            file_id -= 1
            position, size = files[file_id]
            for idx, (start, length) in enumerate(blanks):
                if start >= position:
                    blanks = blanks[:idx]
                    break
                if size <= length:
                    files[file_id] = (start, size)
                    if size == length:
                        blanks.pop(idx)
                        break

                    blanks[idx] = (start + size, length - size)
                    break

        total = 0
        for idx, (position, size) in files.items():
            for value in range(position, position + size):
                total += idx * value
        return total
