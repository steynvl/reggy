class EmailInfo:

    def __init__(self, info):
        self.username                      = info['username']
        self.domain_name                   = info['domainName']
        self.mailto_prefix                 = info['mailtoPrefix']
        self.specific_usernames_only       = info['specificUserNamesOnly']
        self.domain_on_spec_tld            = info['domainOnSpecificTld']
        self.any_sub_domain_on_spec_domain = info['anySubDomainOnSpecificDomain']
        self.specific_domains_only         = info['specificDomainsOnly']
