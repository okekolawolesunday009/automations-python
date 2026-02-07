## 3. Regex Special Characters in Python

| Symbol | Meaning | Example |
|--------|---------|---------|
| . | Any character except newline | `re.findall(r'.', 'abc')` → `['a','b','c']` |
| ^ | Start of string | `re.match(r'^a', 'abc')` → matches `'a'` |
| $ | End of string | `re.search(r'b$', 'ab')` → matches `'b'` |
| * | 0 or more repetitions | `re.findall(r'ab*', 'abb ab a')` → `['abb','ab','a']` |
| + | 1 or more repetitions | `re.findall(r'ab+', 'abb ab a')` → `['abb','ab']` |
| ? | 0 or 1 repetition | `re.findall(r'ab?', 'abb ab a')` → `['ab','ab','a']` |
| {n} | Exactly n repetitions | `re.findall(r'a{2}', 'aa aaa a')` → `['aa','aa']` |
| {n,m} | Between n and m repetitions | `re.findall(r'a{1,2}', 'aa aaa a')` → `['aa','aa','a']` |
| [] | Character class | `re.findall(r'[aeiou]', 'hello')` → `['e','o']` |
| [^ ] | Negated character class | `re.findall(r'[^aeiou]', 'hello')` → `['h','l','l']` |
| \| | OR | - |
| () | Grouping | `m = re.search(r'(\d+)-(\w+)', '123-abc')` → `('123','abc')` |
| \ | Escape special character | `re.findall(r'\.', 'a.b.c')` → `['.','.']` |


## 4. Regex Shorthand Character Classes

| Shorthand | Meaning | Example |
|-----------|---------|---------|
| \d | Any digit [0-9] | `re.findall(r'\d', 'a1b2')` → `['1','2']` |
| \D | Non-digit | `re.findall(r'\D', 'a1b2')` → `['a','b']` |
| \w | Word character [a-zA-Z0-9_] | `re.findall(r'\w', 'hi!_123')` → `['h','i','_','1','2','3']` |
| \W | Non-word character | `re.findall(r'\W', 'hi!_123')` → `['!']` |
| \s | Whitespace [ \t\n\r\f\v] | `re.findall(r'\s', 'a b\nc')` → `[' ','\n']` |
| \S | Non-whitespace | `re.findall(r'\S', 'a b\nc')` → `['a','b','c']` |
| \b | Word boundary | `re.findall(r'\bcat\b', 'cat scatter')` → `['cat']` |
| \B | Not word boundary | `re.findall(r'\Bcat\B', 'scattering')` → `['cat']` |

r'pool="([^"]*)" release="([^"]*)" upstream_status="([^"]*)" ' #[^"]* - value of pool, release upstream

result.group(1) #pool
