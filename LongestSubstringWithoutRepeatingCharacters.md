# Longest Substring Without Repeating Characters (medium)

Given a string s, find the length of the longest substring without repeating characters.

Javascript solution. It works on reasonably sized strings, but times out when given every character in order many times in a row.
Quadratic-time algorithm: T(n) = O($n^2$).
```js
const lengthOfLongestSubstring = (s) => {
    if (s.length === 1) {
        return 1;
    }
    let longestSubstring = 0;
    let uniqueChars;
    
    for (let x = 0; x < s.length; x++) {
        uniqueChars = [s[x]];
        
        for (let y = x + 1; y < s.length; y++) {            
            if (!uniqueChars.includes(s[y])) {
                uniqueChars.push(s[y]);
            } else {
                break;
            }                
        }
        
        if (uniqueChars.length > longestSubstring) {
                longestSubstring = uniqueChars.length;
        }
    }
    return longestSubstring;
};
```
// I think a better solution would have to check and compare indices of each unique character. Would have a better Big-O rank 