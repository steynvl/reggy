class DateAndTimeInfo:

    def __init__(self, info):
        self.date_separator  = info['dateSeparator']
        self.time_separator  = info['timeSeparator']
        self.am_pm_indicator = info['amPmIndicator']
        self.leading_zeros   = info['leadingZeros']
        self.date_formats    = info['dateFormats']
