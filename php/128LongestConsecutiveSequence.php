<?php
class Solution {
  function longestConsecutive($nums): int {
    // creae a set
    $numsSet = [];
    for ($i=0; $i < count($nums); $i++) {
      $n = $nums[$i];
      if(!array_key_exists($n, $numsSet)) {
        $numsSet[$n] = 0;
      }
    }

    // get the start of the sequence
    $seqStart = [];
    foreach ($numsSet as $n => $value) {
      $leftVal = $n - 1;
      if(!array_key_exists($leftVal, $numsSet)) {
        $seqStart[] = $n;
      }
    }

    $result = 0;

    foreach ($seqStart as $n) {
      $i = 1; 
      while (true) {
        $next = $n + 1;
        if(array_key_exists($next, $numsSet)) {
          $n+=1;
          $i+=1;
        } else 
          break;
      }
      if($result < $i)
        $result = $i;  
    }

    return $result;
  }
}

$solution = new Solution();
// $solution->longestConsecutive([100,4,200,1,3,2]);
$result = $solution->longestConsecutive([100,4,200,1,3,2]);
var_dump($result);