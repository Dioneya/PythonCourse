import re
_str = r'Jgjofnfjkf456 fljgfjkl Jds45 pldg;gs; Ldfdg4 Lead435'

parser = re.findall(r'[A-Z]{1}[a-z]*[0-9]{2,4}',_str)
print(parser)