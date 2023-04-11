<h1 align="center"> LeetCode-solutions <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWNiNjdlZjgzMGQyNTBiOWY2OGU2NWIwNjZlNWI4OTRkM2JkODNiNiZjdD1z/dAoHbGjH7k5ZTeQeBI/giphy.gif" height="34"/> </h1>
<div>Hi, this is repo for my solution of problem on LeetCode</div>

<h3>Stats</h3>

[![KnlnKS's LeetCode stats](https://leetcode-stats-six.vercel.app/api?username=morozoff_yarik)](https://github.com/KnlnKS/leetcode-stats)

<div>to fast find use CMD(Ctrl)+F + name of problem (or num)🐗</div>

<h1>🍏EASY🍏</h1>

<h2>1. Two Sum</h2>
<a href = "https://leetcode.com/problems/two-sum/"> Problem <a/>
  
<a href = "https://github.com/morozooff/leetCode-solutions/blob/master/easy/twoSum.py"> Solution <a/>
  
<p>Return sum of two elements by their index</p>
  
<h2>9. Palindrome Number</h2>
<a href = "https://leetcode.com/problems/palindrome-number/"> Problem <a/>
  
<a href = "https://github.com/morozooff/leetCode-solutions/blob/master/easy/palindromeNumber.py"> Solution <a/>
  
<p>Invert string, compare invert with original</p>
  
<h2>13. Roman to Integer</h2>
<a href = "https://leetcode.com/problems/roman-to-integer/"> Problem <a/>
  
<a href = "https://github.com/morozooff/leetCode-solutions/blob/master/easy/romanToInteger.py"> Solution <a/>
  
<p>Use Python dictionaries for coeff and counters symbol, than just sum </p>

<h2>14. Longest Common Prefix</h2>
<a href = "https://leetcode.com/problems/longest-common-prefix/"> Problem <a/>
  
<a href = "https://github.com/morozooff/leetCode-solutions/blob/master/easy/longectCommonPrefix.py"> Solution <a/>
  
<p>Use zip(), set() than compare</p>
  
<h2>20. Valid Parentheses</h2>
<a href = "https://leetcode.com/problems/valid-parentheses/"> Problem <a/>
  
<a href = "https://github.com/morozooff/leetCode-solutions/blob/master/easy/validParentheses.py"> Solution <a/>
  
<p>Create stack, add at stack bracket, if bracket already in stack just pop() it out. If string is valid, len(strng) must be 0</p>
  
<h2>118. Pascal's Triangle</h2>
<a href = "https://leetcode.com/problems/pascals-triangle/"> Problem <a/>
  
<a href = "https://github.com/morozooff/leetCode-solutions/blob/master/easy/pascalsTriangle.py"> Solution <a/>

___
<a href = "https://leetcode.com/problems/pascals-triangle/solutions/3403862/solution-with-comb-n-k-beast-85-44/"> My post with explanation <a/>

<h2>119. Pascal's Triangle II</h2>
<a href = "https://leetcode.com/problems/pascals-triangle-ii/description/"> Problem <a/>
  
<a href = "https://github.com/morozooff/leetCode-solutions/blob/master/easy/PascalsTriangle2.py"> Solution <a/>
<p>For more details check post with explanation <b>118. Pascal Triangle</b></p>
  
<h2>136. Single Number</h2>
<a href = "https://leetcode.com/problems/single-number/description/"> Problem <a/>
  
<a href = "https://github.com/morozooff/leetCode-solutions/blob/master/easy/singleNumber.py"> Solution <a/>
<p>Create additional list, if current elem already exists on list, delete from list same elem. <br>
  If doesnt exist - add current elem on list
</p>

<h1>🍋MEDIUM🍋</h1>
<h2>2390. Removing Stars From a String</h2>

<p> I see two ways to solve this problem <br> <br>
<b>First</b> - for any Py version:<br>
<ol type="1"> 
<li> Create stack </li> 
<li> Iterate elements </li> 
<li> Add to stack if elem is not *, but if elem is *, take out highter elem in stack </li> 
</ol> 
</p>

<p> <b>Second</b> - for any Py version using syntactic sugar 🤤:<br>
<b>❗️WARN❗️</b> Its solution expensive on time <br> <br>
While there is *:
<ol type="1">  
<li> In new string create <b>slice</b> =  [elem before left neighbor of *] +  [elem after *]  </li> 
<li> For definition index use index() </li> 
</ol> 
</p>
  
<a href = "https://leetcode.com/problems/removing-stars-from-a-string/description/"> Problem <a/>

<a href = "https://github.com/morozooff/leetCode-solutions/blob/master/medium/removingStarsFromAString.py"> Solution <a/>

<h1>🍅HARD🍅</h1>
