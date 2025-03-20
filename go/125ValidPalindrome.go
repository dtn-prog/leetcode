package main

import (
	"fmt"
	"strings"
	"unicode"
)

func isAlphanumeric(char rune) bool {
	return unicode.IsDigit(char) || unicode.IsLetter(char)
	// charAsciNum := int(char)
	// return ((charAsciNum >= int('a') && charAsciNum <= int('z')) ||
	// 	(charAsciNum >= int('A') && charAsciNum <= int('Z')) ||
	// 	(charAsciNum >= int('0') && charAsciNum <= int('9')))
}

func isPalindrome(s string) bool {
	lowerS := strings.ToLower(s)
	runeS := []rune(lowerS)
	fmt.Println(len(runeS))
	for i, j := 0, len(runeS)-1; i < j; i, j = i+1, j-1 {
		for i < j && !isAlphanumeric(runeS[i]) {
			fmt.Printf("%c\n", runeS[i])
			i++
		}
		for i < j && !isAlphanumeric(runeS[j]) {
			fmt.Printf("%c\n", runeS[j])
			j--
		}
		fmt.Println(runeS[i], runeS[j])
		if runeS[i] != runeS[j] {
			return false
		}
	}
	return true
}

func main() {
	// fmt.Println(isPalindrome("race a car"))
	fmt.Println(isAlphanumeric('a'))
}
