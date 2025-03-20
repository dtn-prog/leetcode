<?php
function isAlphanumeric(string $char):bool {
  $charAsciNum = ord( $char);
  return (
    ($charAsciNum >= ord('a') && $charAsciNum <= ord('z'))||
    ($charAsciNum >= ord('A') && $charAsciNum <= ord('Z'))||
    ($charAsciNum >= ord('0') && $charAsciNum <= ord('9'))
  );
}

function isPalindrome(string $char):bool {
  // $i = 0;
  // $j =  
  return true;
}