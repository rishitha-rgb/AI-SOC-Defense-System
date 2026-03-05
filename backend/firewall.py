import re

rules = [
    r"OR 1=1",
    r"SELECT.*FROM",
    r"<script>",
    r"UNION SELECT"
]

def firewall_check(request):

    for rule in rules:
        if re.search(rule,request,re.IGNORECASE):
            return True

    return False
