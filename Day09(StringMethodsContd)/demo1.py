# isdigit() - Return True if the string is a digit string, False otherwise.
# isnumeric() - Return True if the string is a numeric string, False otherwise.

s1 = "d123"

print(s1.isnumeric())
print(s1.isdigit())

s2 = "12345"
print(s2.isnumeric())
print(s2.isdigit())

print('½'.isnumeric()) # Fraction is numeric
print('½'.isdigit()) # Fraction is not a digit

print('²'.isdigit()) # superscript or power is both digit and numeric
print('²'.isnumeric()) #superscript or power is both digit and numeric

# When to use which?
# If you only want to accept normal numbers or things that could represent integer digits → use isdigit().
#
# If you want to accept any numeric symbol (like fractions, subscripts, superscripts) → use isnumeric().

#  Summary of differences between digit and numeric
#
# Method	    Accepts...	                                        Example
# isdigit()	    Only digits & Unicode digit characters	            '123', '²'
# isnumeric()	All numeric characters (digits, fractions, etc.)	'123', '²', '½'
