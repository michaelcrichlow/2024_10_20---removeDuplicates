def removeDuplicates(nums: list[int]) -> int:
    nums_as_set = set(nums)
    for i, val in enumerate(nums_as_set):
        nums[i] = val
    return len(nums_as_set)


def main() -> None:
    val = [1, 1, 2]
    print(removeDuplicates(val))
    print(val)


if __name__ == '__main__':
    main()
