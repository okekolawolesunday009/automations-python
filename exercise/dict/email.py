def email_list(domains):
	emails = []
	for domain_i, users in domains.items():
	  for user in users:
	    emails.append(str(user) + "@" + domain_i )
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))