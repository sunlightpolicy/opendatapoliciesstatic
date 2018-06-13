Add extra newline after likely line endings
((\.|:|;).? ?(and)? ?)\n
\1\n\n


Also separate adjacent lines that start with numbers
(.)\n([\d\w]{1,2})\.
\1\n\n\2.

Combine adjacent lines from the above outputs
(?<!\n)\n(?!\n)
<space>


Remove newlines before numbered sections
\n(\d{1,2}\. )
\1


Remove newlines before lowercase-lettered sections
\n([a-z]{1,2}\. )
\1


Put newline only before capital-lettered sections (not numbered)
\n([A-Z]\.)
\n\n\1


Make HTML lists (still need to add <ol> or <ul> tags afterward)
\n((\d\d?|\w)\. .+)
<li>\1</li>


Put new <p> tags on new lines
<\/p> <p>
<\/p>\n<p>
