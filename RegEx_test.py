import re

def keyword_check():
    with open('D:\\Python\\Moje projekty\\opensquat\\keywords.txt', 'r', encoding='utf-8') as kw:

        """skip header line"""
        first_line = kw.readline()

        for kw_line in kw:
            print('')
            print(kw_line)

            """adding zero or more characters befor and after keyword"""
            pattern = re.compile(r'.*' + kw_line.strip() + r'.*')

            """searching keyword in domain-names file"""
            with open('D:\\Python\\Moje projekty\\opensquat\\domain-names.txt', 'r', encoding='utf-8') as dn:
                for dn_line in dn:
                    compliance = pattern.search(dn_line)
                    if compliance is None:
                        continue
                    else:
                        print(compliance)


keyword_check()
