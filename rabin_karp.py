"""
In this file you will find the implementation of the Rabin-Karp string search algorithm.

Below I find all starting indices where a 'pattern' appears in the 'text' using the Rabin-Karp string search algorithm.
"""
def rabin_karp(text:str, pattern:str, base: int = 256, mod: int = 101) -> list[int]:
  '''
  param text: The text string we are going to search in
  param pattern: The pattern string to search for
  param base: The base that is used for hashing - defaulting to 256
  param mod: The modilus used to keep the hasing values small - defaulting to 101
  return: Returning a list of starting indices where a pattern is found in the test
  '''

  n = len(text)
  m = len(pattern)

  #checks the edge case where an empty pattern/longer than the text is addressed
  if m == 0 or m > n:
    return []
  # h = base^(m-1) % mod
  h = pow(base, m-1, mod)

  p_hash=0 #hash for the pattern
  t_hash=0 #has for the current text window
  results:list[int]=[]

  #Step 1:computing the initial hashes for pattern and first window
  for i in range (m):
    p_hash=(base * p_hash + ord(pattern[i])) % mod
    t_hash=(base * t_hash + ord(text[i])) % mod

  #Step 2: sliding the window over the text
  for i in range (n-m +1):
    #step 3: if hashes match, then verify substring
    if p_hash == t_hash:
      if text[i:i +m] == pattern:
        results.append(i)

    #Step 4: update rolling hash for the next window
    if i < n - m:
      #remove any leading char, and add trailing char
      t_hash = (base *(t_hash - ord(text[i]) *h) + ord(text[i + m])) % mod

      #Python can give neg modulo, so this fixes it
      if t_hash <0:
        t_hash += mod

  return results



  