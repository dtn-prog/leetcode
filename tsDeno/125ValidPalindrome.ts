const isAlphanumeric = (char: string): boolean => {
  if (char.length !== 1) {
    throw new Error("char must be a single character");
  }
  const charAsciNum = char.charCodeAt(0);
  return (
    (charAsciNum >= "a".charCodeAt(0) && charAsciNum <= "z".charCodeAt(0)) ||
    (charAsciNum >= "A".charCodeAt(0) && charAsciNum <= "Z".charCodeAt(0)) ||
    (charAsciNum >= "0".charCodeAt(0) && charAsciNum <= "9".charCodeAt(0))
  );
};

function isPalindrome(s: string): boolean {
	const size = s.length
	for(let i=0,j=size-1; i < j; i++,j--) {
		while(!isAlphanumeric(s[i]) && i < j)
			i++
		while(!isAlphanumeric(s[j]) && i < j)
			j--
		if (s[i].toLowerCase() !== s[j].toLowerCase()) {
			return false
		}
	}
	return true
}

console.log(isPalindrome('was it a cat that i saw?'))
