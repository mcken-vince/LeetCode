# Roman to Integer (easy)

Given a roman numeral, convert it to an integer.

Javascript solution. First iteration. Kind of went about solving this backwards for some reason.
Quadratic-time algorithm: T(n) = O($n$).
```js
function romanToInt(s) {
    const legend = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    let total = 0;
    const length = s.length;
    
 Array.from(s).map((char, i)=> {
        const prevChar = s[i - 1];
        const nextChar = s[i + 1]
        if (prevChar && legend[prevChar] < legend[char] ) {
            total += (legend[char] - legend[prevChar]);
        } else if (!nextChar || legend[nextChar] <= legend[char]) {
            total += legend[char];
        }       
    })


    return total;
};
```