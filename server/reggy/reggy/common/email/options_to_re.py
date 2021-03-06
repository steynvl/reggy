from reggy.samples.tokens import Target

username_to_re = {

    Target.JAVA: {
        'Allow any user name': "[\\\\d!#$%&'*+/=?_`a-z{|}~^-]++(?:\\\\.[\\\\d!#$%&'*+/=?_`a-z{|}~^-]+)*",
        'Basic characters only [a-z0-9._-]': "[\\\\d_a-z-]++(?:\\\\.[\\\\d_a-z-]+)*"
    },

    Target.PERL: {
        'Allow any user name': "[\\d!#$%&'*+\/=?_`a-z{|}~^-]++(?:\\.[\\d!#$%&'*+\/=?_`a-z{|}~^-]+)*",
        'Basic characters only [a-z0-9._-]': "[\\d_a-z-]++(?:\\.[\\d_a-z-]+)*"
    },

    Target.POSIX: {
        'Allow any user name': "[\\d!#$%&'*+/=?_`a-z{|}~^-]++(?:\\.[\\d!#$%&'*+/=?_`a-z{|}~^-]+)*",
        'Basic characters only [a-z0-9._-]': "[\\d_a-z-]++(?:\\.[\\d_a-z-]+)*"
    },

    Target.PYTHON: {
        'Allow any user name': "[\\d!#$%&\\'*+/=?_`a-z{|}~^-]+(?:\\.[\\d!#$%&\\'*+/=?_`a-z{|}~^-]+)*",
        'Basic characters only [a-z0-9._-]': "[\\d_a-z-]+(?:\\.[\\d_a-z-]+)*"
    },

    Target.JAVASCRIPT: {
        'Allow any user name': "[\\d!#$%&'*+\/=?_`a-z{|}~^-]+(?:\\.[\\d!#$%&'*+\/=?_`a-z{|}~^-]+)*",
        'Basic characters only [a-z0-9._-]': "[\\d_a-z-]+(?:\\.[\\d_a-z-]+)*"
    },

    Target.PHP: {
      'Allow any user name': "[\\d!#$%&'*+\/=?_`a-z{|}~^-]++(?:\\.[\\d!#$%&'*+\/=?_`a-z{|}~^-]+)*",
      'Basic characters only [a-z0-9._-]': "[\\d_a-z-]++(?:\\.[\\d_a-z-]+)*"
    },

    Target.GOLANG: {
        'Allow any user name': "[\\\\d!#$%&'*+/=?_`a-z{|}~^-]+(?:\\\\.[\\\\d!#$%&'*+/=?_`a-z{|}~^-]+)*",
        'Basic characters only [a-z0-9._-]': "[\\\\d_a-z-]+(?:\\\\.[\\\\d_a-z-]+)*"
    },

    Target.RUST: {
        'Allow any user name': "[\\d!#$%&\'*+/=?_`a-z{|}~^-]+(?:\\.[\\d!#$%&\'*+/=?_`a-z{|}~^-]+)*",
        'Basic characters only [a-z0-9._-]': "[\\d_a-z-]+(?:\\.[\\d_a-z-]+)*"
    },

    Target.CSHARP: {
        'Allow any user name': "[\\d!#$%&\'*+/=?_`a-z{|}~^-]+(?:\\.[\\d!#$%&\'*+/=?_`a-z{|}~^-]+)*",
        'Basic characters only [a-z0-9._-]': "[\\d_a-z-]+(?:\\.[\\d_a-z-]+)*"
    },

    Target.SCALA: {
        'Allow any user name': "[\\\\d!#$%&'*+/=?_`a-z{|}~^-]++(?:\\\\.[\\\\d!#$%&'*+/=?_`a-z{|}~^-]+)*",
        'Basic characters only [a-z0-9._-]': "[\\\\d_a-z-]++(?:\\\\.[\\\\d_a-z-]+)*"
    },

    Target.KOTLIN: {
        'Allow any user name': "[\\\\d!#$%&'*+/=?_`a-z{|}~^-]++(?:\\\\.[\\\\d!#$%&'*+/=?_`a-z{|}~^-]+)*",
        'Basic characters only [a-z0-9._-]': "[\\\\d_a-z-]++(?:\\\\.[\\\\d_a-z-]+)*"
    }

}

domain_name_to_re = {

    Target.JAVA: {
        'Allow any domain name': "(?:[\\\\da-z-]++\\\\.)+[a-z]{2,63}+",
        'Allow any domain on specific TLD(s)': "(?:[\\\\da-z-]++\\\\.)+{}",
        'Allow any subdomain on specific domain(s)': "(?:[\\\\da-z-]++\\\\.)*{}"
    },

    Target.PERL: {
        'Allow any domain name': "(?:[\\da-z-]++\\.)+[a-z]{2,63}+",
        'Allow any domain on specific TLD(s)': "(?:[\\da-z-]++\\.)+{}",
        'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]++\\.)*{}"
    },

    Target.POSIX: {
        'Allow any domain name': "(?:[\\da-z-]++\\.)+[a-z]{2,63}+",
        'Allow any domain on specific TLD(s)': "(?:[\\da-z-]++\\.)+{}",
        'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]++\\.)*{}"
    },

    Target.PYTHON: {
        'Allow any domain name': "(?:[\\da-z-]+\\.)+[a-z]{2,63}",
        'Allow any domain on specific TLD(s)': "(?:[\\da-z-]+\\.)+{}",
        'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]+\\.)*{}"
    },

    Target.JAVASCRIPT: {
        'Allow any domain name': "(?:[\\da-z-]+\\.)+[a-z]{2,63}",
        'Allow any domain on specific TLD(s)': "(?:[\\da-z-]+\\.)+{}",
        'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]+\\.)*{}"
    },

    Target.PHP: {
      'Allow any domain name': "(?:[\\da-z-]++\\.)+[a-z]{2,63}+",
      'Allow any domain on specific TLD(s)': "(?:[\\da-z-]++\\.)+{}",
      'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]++\\.)*{}"
    },

    Target.GOLANG: {
        'Allow any domain name': "(?:[\\\\da-z-]+\\\\.)+[a-z]{2,63}",
        'Allow any domain on specific TLD(s)': "(?:[\\\\da-z-]++\\\\.)+{}",
        'Allow any subdomain on specific domain(s)': "(?:[\\\\da-z-]+\\\\.)*{}"
    },

    Target.RUST: {
        'Allow any domain name': "(?:[\\da-z-]+\\.)+[a-z]{2,63}",
        'Allow any domain on specific TLD(s)': "(?:[\\da-z-]+\\.)+{}",
        'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]+\\.)*{}"
    },

    Target.CSHARP: {
        'Allow any domain name': "(?:[\\da-z-]+\\.)+[a-z]{2,63}",
        'Allow any domain on specific TLD(s)': "(?:[\\da-z-]+\\.)+{}",
        'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]+\\.)*{}"
    },

    Target.SCALA: {
        'Allow any domain name': "(?:[\\\\da-z-]++\\\\.)+[a-z]{2,63}+",
        'Allow any domain on specific TLD(s)': "(?:[\\\\da-z-]++\\\\.)+{}",
        'Allow any subdomain on specific domain(s)': "(?:[\\\\da-z-]++\\\\.)*{}"
    },

    Target.KOTLIN: {
        'Allow any domain name': "(?:[\\\\da-z-]++\\\\.)+[a-z]{2,63}+",
        'Allow any domain on specific TLD(s)': "(?:[\\\\da-z-]++\\\\.)+{}",
        'Allow any subdomain on specific domain(s)': "(?:[\\\\da-z-]++\\\\.)*{}"
    }

}
