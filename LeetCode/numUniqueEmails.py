def numUniqueEmails(emails):
    s = set()
    for email in emails:
        local, domain = email.split('@')
        # print(local, domain)
        removePlus = local.split('+')[0]
        # print(removePlus)
        removeDot = ''
        for r in removePlus:
            if r != '.':
                removeDot += r

        # print(removeDot)
        s.add(removeDot + '@' + domain)

    print(len(s))
    return len(s)

emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
numUniqueEmails(emails)