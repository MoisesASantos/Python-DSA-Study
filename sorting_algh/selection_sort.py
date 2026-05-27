Another sorting algorithm we never covered in-depth is called "selection sort". It's similar to bubble sort in that it works by repeatedly swapping items in a list. However, it's slightly more efficient than bubble sort because it only makes one swap per iteration.


def selection_sort(nums):
    for i in range(len(nums) - 1):
        smallest_idx = i
        j = i + 1
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums


this code below should work on C and C++

int	*selection_sort(int *nums)
{
	int size = 0;
	while (nums[size])
		size++;
	for (int i = 0; i < size - 1; i++)
	{
		int smallest_idx = i;
		for (int j = 0; j < size - 1 + i; i++)
		{
			if (nums[j] < nums[smallest_idx])
				smallest_idx = j;
		}
		temp = nums[i];
		nums[i] = nums[smallest_idx];
		nums[smallest_idx] = temp;
	}
	return nums;
}
