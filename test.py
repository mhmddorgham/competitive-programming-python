
# Go through num and get combinations missing a member
nums = [1,2,3,4];
for i in range(len(nums)):
  newList = nums[0:i] + nums[i+1 : len(nums)];
  print(newList);
