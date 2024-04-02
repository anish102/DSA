/* Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. */
var strStr = function (haystack, needle) {
  let temp;
  let flag;
  for (let i = 0; i < haystack.length; i++) {
    if (needle.length === 1) {
      if (haystack[i] === needle) return i;
    } else {
      if (haystack[i] !== needle[0]) {
        continue;
      } else {
        temp = i;
        let k = i;
        for (let j = 1; j < needle.length; j++) {
          k++;
          if (haystack[k] === needle[j]) {
            flag = 1;
          } else {
            flag = 0;
            break;
          }
        }
        if (flag === 1) {
          return temp;
        }
      }
    }
  }
  return -1;
};

console.log(strStr("sadbutsad", "but"));
