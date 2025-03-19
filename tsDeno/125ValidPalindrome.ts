const isAlphanumeric = (char: string):boolean => {
    if(char.length !== 1) {
        throw new Error('phai la a character')
    }
    const charAsciNum = char.charCodeAt(0);
    return (
    (charAsciNum >= 'a'.charCodeAt(0) && charAsciNum <= 'z'.charCodeAt(0))||
    (charAsciNum >= 'A'.charCodeAt(0) && charAsciNum <= 'Z'.charCodeAt(0))||
    (charAsciNum >= '0'.charCodeAt(0) && charAsciNum <= '9'.charCodeAt(0))
    );
}