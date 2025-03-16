function longestConsecutive(nums) {
  // conver to a hash set
  const hashSet = new Set(nums);

  // get the start of the sequence
  const sequenceStarts = [];
  for (const n of hashSet) {
    if (!hashSet.has(n - 1)) {
      sequenceStarts.push(n);
    }
  }
  //loop through the sequence start to check the len
  let result = 0;
  for (let n of sequenceStarts) {
    let i = 1;
    while (true) {
      if (hashSet.has(n + 1)) {
        i++;
        n++;
      } else break;
    }

    if (result < i) {
      result = i;
    }
  }

  return result;
}

console.log(longestConsecutive([1, 0, 1, 2]));
