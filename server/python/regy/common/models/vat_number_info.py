class VatNumberInfo:

    def __init__(self, info):
        self._info                = info
        self.austria             = info['austria']
        self.belgium             = info['belgium']
        self.bulgaria            = info['bulgaria']
        self.hungary             = info['hungary']
        self.netherlands         = info['netherlands']
        self.cyprus              = info['cyprus']
        self.czech_republic      = info['czechRepublic']
        self.germany             = info['germany']
        self.denmark             = info['denmark']
        self.slovakia            = info['slovakia']
        self.estonia             = info['estonia']
        self.greece              = info['greece']
        self.ireland             = info['ireland']
        self.poland              = info['poland']
        self.spain               = info['spain']
        self.italy               = info['italy']
        self.portugal            = info['portugal']
        self.finland             = info['finland']
        self.lithuania           = info['lithuania']
        self.romania             = info['romania']
        self.france              = info['france']
        self.luxembourg          = info['luxembourg']
        self.united_kingdom      = info['unitedKingdom']
        self.latvia              = info['latvia']
        self.sweden              = info['sweden']
        self.croatia             = info['croatia']
        self.malta               = info['malta']
        self.slovenia            = info['slovenia']
        self.country_code        = info['countryCode']
        self.grouping_characters = info['groupingCharacters']

    def get_checked_countries(self):
        return [
            k for k in self._info.keys() if k != 'countryCode' and k != 'groupingCharacters' and self._info[k]
        ]
