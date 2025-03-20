<?php
function isAlphanumeric(string $char):bool {
  $charAsciNum = ord( $char);
  return (
    ($charAsciNum >= ord('a') && $charAsciNum <= ord('z'))||
    ($charAsciNum >= ord('A') && $charAsciNum <= ord('Z'))||
    ($charAsciNum >= ord('0') && $charAsciNum <= ord('9'))
  );
}

function isPalindrome(string $str):bool {
  for($i = 0,$j = strlen($str)-1; $i < $j; $i++,$j--) {
    while(!isAlphanumeric($str[$i]) && $i < $j)
      $i++;
    while(!isAlphanumeric($str[$j]) && $i < $j)
      $j--;
    if(strtolower($str[$i]) !== strtolower($str[$j]))
      return false;
  }   
  return true;
}