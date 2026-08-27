#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int lastIndex[128]; // ASCII characters
    for (int i = 0; i < 128; i++) {
        lastIndex[i] = -1; // -1 means char not seen yet
    }

    int maxLen = 0;
    int start = 0; // start of current window

    for (int end = 0; s[end]!= '\0'; end++) {
        // If char was seen and is inside current window
        if (lastIndex[(int)s[end]] >= start) {
            start = lastIndex[(int)s[end]] + 1; // move start past the duplicate
        }

        lastIndex[(int)s[end]] = end; // update last seen index
        int currLen = end - start + 1;
        if (currLen > maxLen) {
            maxLen = currLen;
        }
    }

    return maxLen;
}