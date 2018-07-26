from reggy.samples.tokens import Target

url_to_re = {

    Target.JAVA: {
        'scheme': {
            'http'                         : 'http://',
            'https'                        : 'https://',
            'http;https'                   : 'https?://',
            'http;https;www.'              : '(?:https?//|www\\\\.)',
            'ftp'                          : 'ftp://',
            'ftp;ftp.'                     : '(?:ftp://|ftp\\\\.)',
            'ftp;http'                     : '(?:ht|f)tp://',
            'ftp;http;ftp.;www.'           : '(?:(?:ht|f)tp://|(?:ftp|www)\\\\.)',
            'file'                         : 'file://',
            'file;http;https'              : '(?:file|https?)://',
            'file;http;https;www.'         : '(?:(?:file|https?)://|www\\\\.)',
            'file;ftp'                     : 'f(?:ile|tp)://',
            'file;ftp;http;https'          : '(?:file|ftp|https?)://',
            'file;ftp;http;https;ftp.;www.': '(?:(?:file|ftp|https?)://|(?:ftp|www)\\\\.)',
            'feed'                         : 'feed://',
            'feed;http;https'              : '(?:feed|https?)://',
            'feed;http;https;www.'         : '(?:(?:feed|https?)://|www\\\\.)',
            'news;nntp'                    : 'bn(?:ews|ntp)://',
            'news;nntp;news.'              : '(?:n(?:ews|ntp)://|news\\\\.)',
            'dns'                          : 'dns://',
            'ldap'                         : 'ldap://',
            'nfs'                          : 'nfs://',
            'pop'                          : 'pop://',
            'rtsp'                         : 'rtsp://',
            'snmp'                         : 'snmp://'
        },
        'username': {
            'No user names': '',
            'Allow any user name': '(?:[]\d!"#$%&\'()*+,./:;<=>?@\[\\\\_`a-z{{|}}~^-]+{}{}?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:[\d!$\'()*+,._a-z-]+{}{}?',
            'Basic characters only [A-Za-z0-9._-]': '(?:[\d._a-z-]+{}{}?',
            'Specific user names only': ''
        },
        'password': {
            'No password': '',
            'Optional password': '(?::[\\\\d!#$%&\'*+./=?_`a-z{|}~^-]+)?@)?',
            'Require password': ':[\\\\d!#$%&\'*+./=?_`a-z{|}~^-]+@)?',
            'specUserOptionalPassword': '(?::[\\\\w!#$%&\'*+./=?`{|}~^-]+)?@',
            'specUserRequirePassword': ':[\\\\w!#$%&\'*+./=?`{|}~^-]+@'
        },
        'host': {
            'Allow any domain name'                    : "(?:[\\\\da-z-]++\\\\.)+[a-z]{2,63}+",
            'Allow any domain on specific TLD(s)'      : "(?:[\\\\da-z-]++\\\\.)+{}",
            'Allow any subdomain on specific domain(s)': "(?:[\\\\da-z-]++\\\\.)*{}"
        },
        'portNumbers': {
            'No port number'               : '',
            'Optional port number'         : '(?::\\\\d{1,5}+)?',
            'Specify optional port numbers': '(:{})?',
            'Require port number'          : ':\\\\d{1,5}+',
            'Specify required port numbers': ':{}'
        },
        'folders': {
            'No folders': '',
            'Allow any path': '(?:/[]\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+)',
            'Safe URL characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\\\d!$\'()*+,._a-z-]++)',
            'Safe folder characters only [A-Za-z0-9$_+!\'(),-]': '(?:/[\\\\d!$\'()+,_a-z-]++)',
            'Basic characters only [A-Za-z0-9._-]': '(?:/[\\\\d._a-z-]++)',
            'Basic folder characters only [A-Za-z0-9_-]': '(?:/[\d_a-z-]++)',
            'Specific folders only': '(?:{})?'
        },
        'fileNames': {
            'required': {
            'Allow any file name'                         : '/[]\\\\d!"#$%&\'()*+,.:;<=>?@\[\\\\_`a-z{|}~^-]+',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/[\\\\d!$\'()*+,._a-z-]+',
            'Basic characters only [A-Za-z0-9._-]'        : '/[\\\\d._a-z-]+',
            'Specific extensions only'                    : '/[\\\\w.-]+\\\\.{}',
            'Specific file names only'                    : '/{}'
            },
            'optional': {
            'Allow any file name'                         : '(?:/[]\\\\d!"#$%&\'()*+,.:;<=>?@\[\\\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\\\d!$\'()*+,._a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]'        : '(?:/[\\\\d._a-z-]*)?',
            'Specific extensions only'                    : '(?:/[\\\\w.-]+\\\\.{}?)?',
            'Specific file names only'                    : '(?:/{}?)?'
            }
        },
        'parameters': {
            'Allow any parameters'                        : '/?(?:\?[]\d!"#$%&\'()*+,./:;<=>?@\[\\\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/?(?:\?[\d!$&\'()*+,.=_a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]'        : '/?(?:\?[A-Za-z0-9._-]*)?',
            'Specific parameters only'                    : {
                'one'     : '?\?{}(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?',
                'multiple': '\?(?:{})(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?&?){{{}}}'
            }
        }
    },

    Target.PERL: {
        'scheme': {
            'http'                         : 'http:\/\/',
            'https'                        : 'https:\/\/',
            'http;https'                   : 'https?:\/\/',
            'http;https;www.'              : '(?:https?\/\/|www\\.)',
            'ftp'                          : 'ftp:\/\/',
            'ftp;ftp.'                     : '(?:ftp:\/\/|ftp\\.)',
            'ftp;http'                     : '(?:ht|f)tp:\/\/',
            'ftp;http;ftp.;www.'           : '(?:(?:ht|f)tp:\/\/|(?:ftp|www)\\.)',
            'file'                         : 'file:\/\/',
            'file;http;https'              : '(?:file|https?):\/\/',
            'file;http;https;www.'         : '(?:(?:file|https?):\/\/|www\\.)',
            'file;ftp'                     : 'f(?:ile|tp):\/\/',
            'file;ftp;http;https'          : '(?:file|ftp|https?):\/\/',
            'file;ftp;http;https;ftp.;www.': '(?:(?:file|ftp|https?):\/\/|(?:ftp|www)\\.)',
            'feed'                         : 'feed:\/\/',
            'feed;http;https'              : '(?:feed|https?):\/\/',
            'feed;http;https;www.'         : '(?:(?:feed|https?):\/\/|www\\.)',
            'news;nntp'                    : 'bn(?:ews|ntp):\/\/',
            'news;nntp;news.'              : '(?:n(?:ews|ntp):\/\/|news\\.)',
            'dns'                          : 'dns:\/\/',
            'ldap'                         : 'ldap:\/\/',
            'nfs'                          : 'nfs:\/\/',
            'pop'                          : 'pop:\/\/',
            'rtsp'                         : 'rtsp:\/\/',
            'snmp'                         : 'snmp:\/\/'
        },
        'username': {
            'No user names': '',
            'Allow any user name': '(?:[]\d!"#$%&\'()*+,.\/:;<=>?@\[\\_`a-z{{|}}~^-]+{}{}?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:[\d!$\'()*+,._a-z-]+{}{}?',
            'Basic characters only [A-Za-z0-9._-]': '(?:[\d._a-z-]+{}{}?',
            'Specific user names only': ''
        },
        'password': {
            'No password': '',
            'Optional password': '(?::[\\d!#$%&\'*+.\/=?_`a-z{|}~^-]+)?@)?',
            'Require password': ':[\\d!#$%&\'*+.\/=?_`a-z{|}~^-]+@)?',
            'specUserOptionalPassword': '(?::[\\w!#$%&\'*+.\/=?`{|}~^-]+)?@',
            'specUserRequirePassword': ':[\\w!#$%&\'*+.\/=?`{|}~^-]+@'
        },
        'host': {
            'Allow any domain name'                    : "(?:[\\da-z-]++\\.)+[a-z]{2,63}+",
            'Allow any domain on specific TLD(s)'      : "(?:[\\da-z-]++\\.)+{}",
            'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]++\\.)*{}"
        },
        'portNumbers': {
            'No port number'               : '',
            'Optional port number'         : '(?::\\d{1,5}+)?',
            'Specify optional port numbers': '(:{})?',
            'Require port number'          : ':\\d{1,5}+',
            'Specify required port numbers': ':{}'
        },
        'folders': {
            'No folders': '',
            'Allow any path': '(?:\/[]\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+)',
            'Safe URL characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:\/[\\d!$\'()*+,._a-z-]++)',
            'Safe folder characters only [A-Za-z0-9$_+!\'(),-]': '(?:\/[\\d!$\'()+,_a-z-]++)',
            'Basic characters only [A-Za-z0-9._-]': '(?:\/[\\d._a-z-]++)',
            'Basic folder characters only [A-Za-z0-9_-]': '(?:\/[\d_a-z-]++)',
            'Specific folders only': '(?:{})?'
        },
        'fileNames': {
            'required': {
            'Allow any file name'                         : '\/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '\/[\\d!$\'()*+,._a-z-]+',
            'Basic characters only [A-Za-z0-9._-]'        : '\/[\\d._a-z-]+',
            'Specific extensions only'                    : '\/[\\w.-]+\\.{}',
            'Specific file names only'                    : '\/{}'
            },
            'optional': {
            'Allow any file name'                         : '(?:\/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:\/[\\d!$\'()*+,._a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]'        : '(?:\/[\\d._a-z-]*)?',
            'Specific extensions only'                    : '(?:\/[\\w.-]+\\.{}?)?',
            'Specific file names only'                    : '(?:\/{}?)?'
            }
        },
        'parameters': {
            'Allow any parameters'                        : '\/?(?:\?[]\d!"#$%&\'()*+,.\/:;<=>?@\[\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '\/?(?:\?[\d!$&\'()*+,.=_a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]'        : '\/?(?:\?[A-Za-z0-9._-]*)?',
            'Specific parameters only'                    : {
                'one'     : '?\?{}(?:=[]\d!"#$%\'()*+,.\/:;<=>?@\[\\_`a-z{{|}}~^-]*+)?',
                'multiple': '\?(?:{})(?:=[]\d!"#$%\'()*+,.\/:;<=>?@\[\\_`a-z{{|}}~^-]*+)?&?){{{}}}'
            }
        }
    },

    Target.POSIX: {
        'scheme': {
            'http'                         : 'http://',
            'https'                        : 'https://',
            'http;https'                   : 'https?://',
            'http;https;www.'              : '(?:https?//|www\\.)',
            'ftp'                          : 'ftp://',
            'ftp;ftp.'                     : '(?:ftp://|ftp\\.)',
            'ftp;http'                     : '(?:ht|f)tp://',
            'ftp;http;ftp.;www.'           : '(?:(?:ht|f)tp://|(?:ftp|www)\\.)',
            'file'                         : 'file://',
            'file;http;https'              : '(?:file|https?)://',
            'file;http;https;www.'         : '(?:(?:file|https?)://|www\\.)',
            'file;ftp'                     : 'f(?:ile|tp)://',
            'file;ftp;http;https'          : '(?:file|ftp|https?)://',
            'file;ftp;http;https;ftp.;www.': '(?:(?:file|ftp|https?)://|(?:ftp|www)\\.)',
            'feed'                         : 'feed://',
            'feed;http;https'              : '(?:feed|https?)://',
            'feed;http;https;www.'         : '(?:(?:feed|https?)://|www\\.)',
            'news;nntp'                    : 'bn(?:ews|ntp)://',
            'news;nntp;news.'              : '(?:n(?:ews|ntp)://|news\\.)',
            'dns'                          : 'dns://',
            'ldap'                         : 'ldap://',
            'nfs'                          : 'nfs://',
            'pop'                          : 'pop://',
            'rtsp'                         : 'rtsp://',
            'snmp'                         : 'snmp://'
        },
        'username': {
            'No user names': '',
            'Allow any user name': '(?:[]\d!"#$%&\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]+{}{}?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:[\d!$\'()*+,._a-z-]+{}{}?',
            'Basic characters only [A-Za-z0-9._-]': '(?:[\d._a-z-]+{}{}?',
            'Specific user names only': ''
        },
        'password': {
            'No password': '',
            'Optional password': '(?::[\\d!#$%&\'*+./=?_`a-z{|}~^-]+)?@)?',
            'Require password': ':[\\d!#$%&\'*+./=?_`a-z{|}~^-]+@)?',
            'specUserOptionalPassword': '(?::[\\w!#$%&\'*+./=?`{|}~^-]+)?@',
            'specUserRequirePassword': ':[\\w!#$%&\'*+./=?`{|}~^-]+@'
        },
        'host': {
            'Allow any domain name'                    : "(?:[\\da-z-]++\\.)+[a-z]{2,63}+",
            'Allow any domain on specific TLD(s)'      : "(?:[\\da-z-]++\\.)+{}",
            'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]++\\.)*{}"
        },
        'portNumbers': {
            'No port number'               : '',
            'Optional port number'         : '(?::\\d{1,5}+)?',
            'Specify optional port numbers': '(:{})?',
            'Require port number'          : ':\\d{1,5}+',
            'Specify required port numbers': ':{}'
        },
        'folders': {
            'No folders': '',
            'Allow any path': '(?:/[]\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+)',
            'Safe URL characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\d!$\'()*+,._a-z-]++)',
            'Safe folder characters only [A-Za-z0-9$_+!\'(),-]': '(?:/[\\d!$\'()+,_a-z-]++)',
            'Basic characters only [A-Za-z0-9._-]': '(?:/[\\d._a-z-]++)',
            'Basic folder characters only [A-Za-z0-9_-]': '(?:/[\d_a-z-]++)',
            'Specific folders only': '(?:{})?'
        },
        'fileNames': {
            'required': {
            'Allow any file name'                         : '/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/[\\d!$\'()*+,._a-z-]+',
            'Basic characters only [A-Za-z0-9._-]'        : '/[\\d._a-z-]+',
            'Specific extensions only'                    : '/[\\w.-]+\\.{}',
            'Specific file names only'                    : '/{}'
            },
            'optional': {
            'Allow any file name'                         : '(?:/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\d!$\'()*+,._a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]'        : '(?:/[\\d._a-z-]*)?',
            'Specific extensions only'                    : '(?:/[\\w.-]+\\.{}?)?',
            'Specific file names only'                    : '(?:/{}?)?'
            }
        },
        'parameters': {
            'Allow any parameters'                        : '/?(?:\?[]\d!"#$%&\'()*+,./:;<=>?@\[\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/?(?:\?[\d!$&\'()*+,.=_a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]'        : '/?(?:\?[A-Za-z0-9._-]*)?',
            'Specific parameters only'                    : {
                'one'     : '?\?{}(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?',
                'multiple': '\?(?:{})(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?&?){{{}}}'
            }
        }
    },

    Target.PYTHON: {
        'scheme': {
            'http'                         : 'http://',
            'https'                        : 'https://',
            'http;https'                   : 'https?://',
            'http;https;www.'              : '(?:https?//|www\\.)',
            'ftp'                          : 'ftp://',
            'ftp;ftp.'                     : '(?:ftp://|ftp\\.)',
            'ftp;http'                     : '(?:ht|f)tp://',
            'ftp;http;ftp.;www.'           : '(?:(?:ht|f)tp://|(?:ftp|www)\\.)',
            'file'                         : 'file://',
            'file;http;https'              : '(?:file|https?)://',
            'file;http;https;www.'         : '(?:(?:file|https?)://|www\\.)',
            'file;ftp'                     : 'f(?:ile|tp)://',
            'file;ftp;http;https'          : '(?:file|ftp|https?)://',
            'file;ftp;http;https;ftp.;www.': '(?:(?:file|ftp|https?)://|(?:ftp|www)\\.)',
            'feed'                         : 'feed://',
            'feed;http;https'              : '(?:feed|https?)://',
            'feed;http;https;www.'         : '(?:(?:feed|https?)://|www\\.)',
            'news;nntp'                    : 'bn(?:ews|ntp)://',
            'news;nntp;news.'              : '(?:n(?:ews|ntp)://|news\\.)',
            'dns'                          : 'dns://',
            'ldap'                         : 'ldap://',
            'nfs'                          : 'nfs://',
            'pop'                          : 'pop://',
            'rtsp'                         : 'rtsp://',
            'snmp'                         : 'snmp://'
        },
        'username': {
            'No user names': '',
            'Allow any user name': '(?:[]\d!"#$%&\\\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]+{}{}?',
            'Safe characters only [A-Za-z0-9$_.+!*\\\'(),-]': '(?:[\d!$\\\'()*+,._a-z-]+{}{}?',
            'Basic characters only [A-Za-z0-9._-]': '(?:[\d._a-z-]+{}{}?',
            'Specific user names only': ''
        },
        'password': {
            'No password': '',
            'Optional password': '(?::[\\d!#$%&\\\'*+./=?_`a-z{|}~^-]+)?@)?',
            'Require password': ':[\\d!#$%&\'*+./=?_`a-z{|}~^-]+@)?',
            'specUserOptionalPassword': '(?::[\\w!#$%&\\\'*+./=?`{|}~^-]+)?@',
            'specUserRequirePassword': ':[\\w!#$%&\'*+./=?`{|}~^-]+@'
        },
        'host': {
            'Allow any domain name'                    : "(?:[\\da-z-]+\\.)+[a-z]{2,63}",
            'Allow any domain on specific TLD(s)'      : "(?:[\\da-z-]+\\.)+{}",
            'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]+\\.)*{}"
        },
        'portNumbers': {
            'No port number'               : '',
            'Optional port number'         : '(?::\\d{1,5})?',
            'Specify optional port numbers': '(:{})?',
            'Require port number'          : ':\\d{1,5}',
            'Specify required port numbers': ':{}'
        },
        'folders': {
            'No folders': '',
            'Allow any path': '(?:/[]\d!"#$%&\\\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+)',
            'Safe URL characters only [A-Za-z0-9$_.+!*\\\'(),-]': '(?:/[\\d!$\\\'()*+,._a-z-]+)',
            'Safe folder characters only [A-Za-z0-9$_+!\\\'(),-]': '(?:/[\\d!$\\\'()+,_a-z-]+)',
            'Basic characters only [A-Za-z0-9._-]': '(?:/[\\d._a-z-]+)',
            'Basic folder characters only [A-Za-z0-9_-]': '(?:/[\d_a-z-]+)',
            'Specific folders only': '(?:{})?'
        },
        'fileNames': {
            'required': {
            'Allow any file name'                         : '/[]\\d!"#$%&\\\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/[\\d!$\\\'()*+,._a-z-]+',
            'Basic characters only [A-Za-z0-9._-]'        : '/[\\d._a-z-]+',
            'Specific extensions only'                    : '/[\\w.-]+\\.{}',
            'Specific file names only'                    : '/{}'
            },
            'optional': {
            'Allow any file name'                         : '(?:/[]\\d!"#$%&\\\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\d!$\\\'()*+,._a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]'        : '(?:/[\\d._a-z-]*)?',
            'Specific extensions only'                    : '(?:/[\\w.-]+\\.{}?)?',
            'Specific file names only'                    : '(?:/{}?)?'
            }
        },
        'parameters': {
            'Allow any parameters'                        : '/?(?:\?[]\d!"#$%&\\\'()*+,./:;<=>?@\[\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/?(?:\?[\d!$&\\\'()*+,.=_a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]'        : '/?(?:\?[A-Za-z0-9._-]*)?',
            'Specific parameters only'                    : {
                'one'     : '?\?{}(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?',
                'multiple': '\?(?:{})(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?&?){{{}}}'
            }
        }
    },

    Target.JAVASCRIPT: {
        'scheme': {
            'http': 'http:\/\/',
            'https': 'https:\/\/',
            'http;https': 'https?:\/\/',
            'http;https;www.': '(?:https?\/\/|www\\.)',
            'ftp': 'ftp:\/\/',
            'ftp;ftp.': '(?:ftp:\/\/|ftp\\.)',
            'ftp;http': '(?:ht|f)tp:\/\/',
            'ftp;http;ftp.;www.': '(?:(?:ht|f)tp:\/\/|(?:ftp|www)\\.)',
            'file': 'file:\/\/',
            'file;http;https': '(?:file|https?):\/\/',
            'file;http;https;www.': '(?:(?:file|https?):\/\/|www\\.)',
            'file;ftp': 'f(?:ile|tp):\/\/',
            'file;ftp;http;https': '(?:file|ftp|https?):\/\/',
            'file;ftp;http;https;ftp.;www.': '(?:(?:file|ftp|https?):\/\/|(?:ftp|www)\\.)',
            'feed': 'feed:\/\/',
            'feed;http;https': '(?:feed|https?):\/\/',
            'feed;http;https;www.': '(?:(?:feed|https?):\/\/|www\\.)',
            'news;nntp': 'bn(?:ews|ntp):\/\/',
            'news;nntp;news.': '(?:n(?:ews|ntp):\/\/|news\\.)',
            'dns': 'dns:\/\/',
            'ldap': 'ldap:\/\/',
            'nfs': 'nfs:\/\/',
            'pop': 'pop:\/\/',
            'rtsp': 'rtsp:\/\/',
            'snmp': 'snmp:\/\/'
        },
        'username': {
            'No user names': '',
            'Allow any user name': '(?:[]\d!"#$%&\'()*+,.\/:;<=>?@\[\\_`a-z{{|}}~^-]+{}{}?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:[\d!$\'()*+,._a-z-]+{}{}?',
            'Basic characters only [A-Za-z0-9._-]': '(?:[\d._a-z-]+{}{}?',
            'Specific user names only': ''
        },
        'password': {
            'No password': '',
            'Optional password': '(?::[\\d!#$%&\'*+.\/=?_`a-z{|}~^-]+)?@)?',
            'Require password': ':[\\d!#$%&\'*+.\/=?_`a-z{|}~^-]+@)?',
            'specUserOptionalPassword': '(?::[\\w!#$%&\'*+.\/=?`{|}~^-]+)?@',
            'specUserRequirePassword': ':[\\w!#$%&\'*+.\/=?`{|}~^-]+@'
        },
        'host': {
            'Allow any domain name': "(?:[\\da-z-]+\\.)+[a-z]{2,63}",
            'Allow any domain on specific TLD(s)': "(?:[\\da-z-]+\\.)+{}",
            'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]+\\.)*{}"
        },
        'portNumbers': {
            'No port number': '',
            'Optional port number': '(?::\\d{1,5})?',
            'Specify optional port numbers': '(:{})?',
            'Require port number': ':\\d{1,5}',
            'Specify required port numbers': ':{}'
        },
        'folders': {
            'No folders': '',
            'Allow any path': '(?:\/[]\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+)',
            'Safe URL characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:\/[\\d!$\'()*+,._a-z-]+)',
            'Safe folder characters only [A-Za-z0-9$_+!\'(),-]': '(?:\/[\\d!$\'()+,_a-z-]+)',
            'Basic characters only [A-Za-z0-9._-]': '(?:\/[\\d._a-z-]+)',
            'Basic folder characters only [A-Za-z0-9_-]': '(?:\/[\d_a-z-]+)',
            'Specific folders only': '(?:{})?'
        },
        'fileNames': {
            'required': {
                'Allow any file name': '\/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+',
                'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '\/[\\d!$\'()*+,._a-z-]+',
                'Basic characters only [A-Za-z0-9._-]': '\/[\\d._a-z-]+',
                'Specific extensions only': '\/[\\w.-]+\\.{}',
                'Specific file names only': '\/{}'
            },
            'optional': {
                'Allow any file name': '(?:\/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]*)?',
                'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:\/[\\d!$\'()*+,._a-z-]*)?',
                'Basic characters only [A-Za-z0-9._-]': '(?:\/[\\d._a-z-]*)?',
                'Specific extensions only': '(?:\/[\\w.-]+\\.{}?)?',
                'Specific file names only': '(?:\/{}?)?'
            }
        },
        'parameters': {
            'Allow any parameters': '\/?(?:\?[]\d!"#$%&\'()*+,.\/:;<=>?@\[\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '\/?(?:\?[\d!$&\'()*+,.=_a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]': '\/?(?:\?[A-Za-z0-9._-]*)?',
            'Specific parameters only': {
                'one': '?\?{}(?:=[]\d!"#$%\'()*+,.\/:;<=>?@\[\\_`a-z{{|}}~^-]*+)?',
                'multiple': '\?(?:{})(?:=[]\d!"#$%\'()*+,.\/:;<=>?@\[\\_`a-z{{|}}~^-]*+)?&?){{{}}}'
            }
        }
    },

    Target.PHP: {
      'scheme': {
        'http': 'http:\/\/',
        'https': 'https:\/\/',
        'http;https': 'https?:\/\/',
        'http;https;www.': '(?:https?\/\/|www\\.)',
        'ftp': 'ftp:\/\/',
        'ftp;ftp.': '(?:ftp:\/\/|ftp\\.)',
        'ftp;http': '(?:ht|f)tp:\/\/',
        'ftp;http;ftp.;www.': '(?:(?:ht|f)tp:\/\/|(?:ftp|www)\\.)',
        'file': 'file:\/\/',
        'file;http;https': '(?:file|https?):\/\/',
        'file;http;https;www.': '(?:(?:file|https?):\/\/|www\\.)',
        'file;ftp': 'f(?:ile|tp):\/\/',
        'file;ftp;http;https': '(?:file|ftp|https?):\/\/',
        'file;ftp;http;https;ftp.;www.': '(?:(?:file|ftp|https?):\/\/|(?:ftp|www)\\.)',
        'feed': 'feed:\/\/',
        'feed;http;https': '(?:feed|https?):\/\/',
        'feed;http;https;www.': '(?:(?:feed|https?):\/\/|www\\.)',
        'news;nntp': 'bn(?:ews|ntp):\/\/',
        'news;nntp;news.': '(?:n(?:ews|ntp):\/\/|news\\.)',
        'dns': 'dns:\/\/',
        'ldap': 'ldap:\/\/',
        'nfs': 'nfs:\/\/',
        'pop': 'pop:\/\/',
        'rtsp': 'rtsp:\/\/',
        'snmp': 'snmp:\/\/'
      },
      'username': {
        'No user names': '',
        'Allow any user name': '(?:[]\d!"#$%&\'()*+,.\/:;<=>?@\[\\_`a-z{{|}}~^-]+{}{}?',
        'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:[\d!$\'()*+,._a-z-]+{}{}?',
        'Basic characters only [A-Za-z0-9._-]': '(?:[\d._a-z-]+{}{}?',
        'Specific user names only': ''
      },
      'password': {
        'No password': '',
        'Optional password': '(?::[\\d!#$%&\'*+.\/=?_`a-z{|}~^-]+)?@)?',
        'Require password': ':[\\d!#$%&\'*+.\/=?_`a-z{|}~^-]+@)?',
        'specUserOptionalPassword': '(?::[\\w!#$%&\'*+.\/=?`{|}~^-]+)?@',
        'specUserRequirePassword': ':[\\w!#$%&\'*+.\/=?`{|}~^-]+@'
      },
      'host': {
        'Allow any domain name': "(?:[\\da-z-]++\\.)+[a-z]{2,63}+",
        'Allow any domain on specific TLD(s)': "(?:[\\da-z-]++\\.)+{}",
        'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]++\\.)*{}"
      },
      'portNumbers': {
        'No port number': '',
        'Optional port number': '(?::\\d{1,5}+)?',
        'Specify optional port numbers': '(:{})?',
        'Require port number': ':\\d{1,5}+',
        'Specify required port numbers': ':{}'
      },
      'folders': {
        'No folders': '',
        'Allow any path': '(?:\/[]\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+)',
        'Safe URL characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:\/[\\d!$\'()*+,._a-z-]++)',
        'Safe folder characters only [A-Za-z0-9$_+!\'(),-]': '(?:\/[\\d!$\'()+,_a-z-]++)',
        'Basic characters only [A-Za-z0-9._-]': '(?:\/[\\d._a-z-]++)',
        'Basic folder characters only [A-Za-z0-9_-]': '(?:\/[\d_a-z-]++)',
        'Specific folders only': '(?:{})?'
      },
      'fileNames': {
        'required': {
          'Allow any file name': '\/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+',
          'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '\/[\\d!$\'()*+,._a-z-]+',
          'Basic characters only [A-Za-z0-9._-]': '\/[\\d._a-z-]+',
          'Specific extensions only': '\/[\\w.-]+\\.{}',
          'Specific file names only': '\/{}'
        },
        'optional': {
          'Allow any file name': '(?:\/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]*)?',
          'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:\/[\\d!$\'()*+,._a-z-]*)?',
          'Basic characters only [A-Za-z0-9._-]': '(?:\/[\\d._a-z-]*)?',
          'Specific extensions only': '(?:\/[\\w.-]+\\.{}?)?',
          'Specific file names only': '(?:\/{}?)?'
        }
      },
      'parameters': {
        'Allow any parameters': '\/?(?:\?[]\d!"#$%&\'()*+,.\/:;<=>?@\[\\_`a-z{|}~^-]*)?',
        'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '\/?(?:\?[\d!$&\'()*+,.=_a-z-]*)?',
        'Basic characters only [A-Za-z0-9._-]': '\/?(?:\?[A-Za-z0-9._-]*)?',
        'Specific parameters only': {
          'one': '?\?{}(?:=[]\d!"#$%\'()*+,.\/:;<=>?@\[\\_`a-z{{|}}~^-]*+)?',
          'multiple': '\?(?:{})(?:=[]\d!"#$%\'()*+,.\/:;<=>?@\[\\_`a-z{{|}}~^-]*+)?&?){{{}}}'
        }
      }
    },

    Target.GOLANG: {
        'scheme': {
            'http'                         : 'http://',
            'https'                        : 'https://',
            'http;https'                   : 'https?://',
            'http;https;www.'              : '(?:https?//|www\\\\.)',
            'ftp'                          : 'ftp://',
            'ftp;ftp.'                     : '(?:ftp://|ftp\\\\.)',
            'ftp;http'                     : '(?:ht|f)tp://',
            'ftp;http;ftp.;www.'           : '(?:(?:ht|f)tp://|(?:ftp|www)\\\\.)',
            'file'                         : 'file://',
            'file;http;https'              : '(?:file|https?)://',
            'file;http;https;www.'         : '(?:(?:file|https?)://|www\\\\.)',
            'file;ftp'                     : 'f(?:ile|tp)://',
            'file;ftp;http;https'          : '(?:file|ftp|https?)://',
            'file;ftp;http;https;ftp.;www.': '(?:(?:file|ftp|https?)://|(?:ftp|www)\\\\.)',
            'feed'                         : 'feed://',
            'feed;http;https'              : '(?:feed|https?)://',
            'feed;http;https;www.'         : '(?:(?:feed|https?)://|www\\\\.)',
            'news;nntp'                    : 'bn(?:ews|ntp)://',
            'news;nntp;news.'              : '(?:n(?:ews|ntp)://|news\\\\.)',
            'dns'                          : 'dns://',
            'ldap'                         : 'ldap://',
            'nfs'                          : 'nfs://',
            'pop'                          : 'pop://',
            'rtsp'                         : 'rtsp://',
            'snmp'                         : 'snmp://'
        },
        'username': {
            'No user names': '',
            'Allow any user name': '(?:[]\d!"#$%&\'()*+,./:;<=>?@\[\\\\_`a-z{{|}}~^-]+{}{}?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:[\d!$\'()*+,._a-z-]+{}{}?',
            'Basic characters only [A-Za-z0-9._-]': '(?:[\d._a-z-]+{}{}?',
            'Specific user names only': ''
        },
        'password': {
            'No password': '',
            'Optional password': '(?::[\\\\d!#$%&\'*+./=?_`a-z{|}~^-]+)?@)?',
            'Require password': ':[\\\\d!#$%&\'*+./=?_`a-z{|}~^-]+@)?',
            'specUserOptionalPassword': '(?::[\\\\w!#$%&\'*+./=?`{|}~^-]+)?@',
            'specUserRequirePassword': ':[\\\\w!#$%&\'*+./=?`{|}~^-]+@'
        },
        'host': {
            'Allow any domain name'                    : "(?:[\\\\da-z-]+\\\\.)+[a-z]{2,63}",
            'Allow any domain on specific TLD(s)'      : "(?:[\\\\da-z-]+\\\\.)+{}",
            'Allow any subdomain on specific domain(s)': "(?:[\\\\da-z-]+\\\\.)*{}"
        },
        'portNumbers': {
            'No port number'               : '',
            'Optional port number'         : '(?::\\\\d{1,5})?',
            'Specify optional port numbers': '(:{})?',
            'Require port number'          : ':\\\\d{1,5}',
            'Specify required port numbers': ':{}'
        },
        'folders': {
            'No folders': '',
            'Allow any path': '(?:/[]\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+)',
            'Safe URL characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\\\d!$\'()*+,._a-z-]+)',
            'Safe folder characters only [A-Za-z0-9$_+!\'(),-]': '(?:/[\\\\d!$\'()+,_a-z-]+)',
            'Basic characters only [A-Za-z0-9._-]': '(?:/[\\\\d._a-z-]+)',
            'Basic folder characters only [A-Za-z0-9_-]': '(?:/[\d_a-z-]+)',
            'Specific folders only': '(?:{})?'
        },
        'fileNames': {
            'required': {
            'Allow any file name'                         : '/[]\\\\d!"#$%&\'()*+,.:;<=>?@\[\\\\_`a-z{|}~^-]+',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/[\\\\d!$\'()*+,._a-z-]+',
            'Basic characters only [A-Za-z0-9._-]'        : '/[\\\\d._a-z-]+',
            'Specific extensions only'                    : '/[\\\\w.-]+\\\\.{}',
            'Specific file names only'                    : '/{}'
            },
            'optional': {
            'Allow any file name'                         : '(?:/[]\\\\d!"#$%&\'()*+,.:;<=>?@\[\\\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\\\d!$\'()*+,._a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]'        : '(?:/[\\\\d._a-z-]*)?',
            'Specific extensions only'                    : '(?:/[\\\\w.-]+\\\\.{}?)?',
            'Specific file names only'                    : '(?:/{}?)?'
            }
        },
        'parameters': {
            'Allow any parameters'                        : '/?(?:\?[]\d!"#$%&\'()*+,./:;<=>?@\[\\\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/?(?:\?[\d!$&\'()*+,.=_a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]'        : '/?(?:\?[A-Za-z0-9._-]*)?',
            'Specific parameters only'                    : {
                'one'     : '?\?{}(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?',
                'multiple': '\?(?:{})(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?&?){{{}}}'
            }
        }
    },

    Target.RUST: {
        'scheme': {
            'http': 'http://',
            'https': 'https://',
            'http;https': 'https?://',
            'http;https;www.': '(?:https?//|www\\.)',
            'ftp': 'ftp://',
            'ftp;ftp.': '(?:ftp://|ftp\\.)',
            'ftp;http': '(?:ht|f)tp://',
            'ftp;http;ftp.;www.': '(?:(?:ht|f)tp://|(?:ftp|www)\\.)',
            'file': 'file://',
            'file;http;https': '(?:file|https?)://',
            'file;http;https;www.': '(?:(?:file|https?)://|www\\.)',
            'file;ftp': 'f(?:ile|tp)://',
            'file;ftp;http;https': '(?:file|ftp|https?)://',
            'file;ftp;http;https;ftp.;www.': '(?:(?:file|ftp|https?)://|(?:ftp|www)\\.)',
            'feed': 'feed://',
            'feed;http;https': '(?:feed|https?)://',
            'feed;http;https;www.': '(?:(?:feed|https?)://|www\\.)',
            'news;nntp': 'bn(?:ews|ntp)://',
            'news;nntp;news.': '(?:n(?:ews|ntp)://|news\\.)',
            'dns': 'dns://',
            'ldap': 'ldap://',
            'nfs': 'nfs://',
            'pop': 'pop://',
            'rtsp': 'rtsp://',
            'snmp': 'snmp://'
        },
        'username': {
            'No user names': '',
            'Allow any user name': '(?:[]\d!"#$%&\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]+{}{}?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:[\d!$\'()*+,._a-z-]+{}{}?',
            'Basic characters only [A-Za-z0-9._-]': '(?:[\d._a-z-]+{}{}?',
            'Specific user names only': ''
        },
        'password': {
            'No password': '',
            'Optional password': '(?::[\\d!#$%&\'*+./=?_`a-z{|}~^-]+)?@)?',
            'Require password': ':[\\d!#$%&\'*+./=?_`a-z{|}~^-]+@)?',
            'specUserOptionalPassword': '(?::[\\w!#$%&\'*+./=?`{|}~^-]+)?@',
            'specUserRequirePassword': ':[\\w!#$%&\'*+./=?`{|}~^-]+@'
        },
        'host': {
            'Allow any domain name': "(?:[\\da-z-]+\\.)+[a-z]{2,63}",
            'Allow any domain on specific TLD(s)': "(?:[\\da-z-]+\\.)+{}",
            'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]+\\.)*{}"
        },
        'portNumbers': {
            'No port number': '',
            'Optional port number': '(?::\\d{1,5})?',
            'Specify optional port numbers': '(:{})?',
            'Require port number': ':\\d{1,5}',
            'Specify required port numbers': ':{}'
        },
        'folders': {
            'No folders': '',
            'Allow any path': '(?:/[]\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+)',
            'Safe URL characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\d!$\'()*+,._a-z-]+)',
            'Safe folder characters only [A-Za-z0-9$_+!\'(),-]': '(?:/[\\d!$\'()+,_a-z-]+)',
            'Basic characters only [A-Za-z0-9._-]': '(?:/[\\d._a-z-]+)',
            'Basic folder characters only [A-Za-z0-9_-]': '(?:/[\d_a-z-]+)',
            'Specific folders only': '(?:{})?'
        },
        'fileNames': {
            'required': {
                'Allow any file name': '/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+',
                'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/[\\d!$\'()*+,._a-z-]+',
                'Basic characters only [A-Za-z0-9._-]': '/[\\d._a-z-]+',
                'Specific extensions only': '/[\\w.-]+\\.{}',
                'Specific file names only': '/{}'
            },
            'optional': {
                'Allow any file name': '(?:/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]*)?',
                'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\d!$\'()*+,._a-z-]*)?',
                'Basic characters only [A-Za-z0-9._-]': '(?:/[\\d._a-z-]*)?',
                'Specific extensions only': '(?:/[\\w.-]+\\.{}?)?',
                'Specific file names only': '(?:/{}?)?'
            }
        },
        'parameters': {
            'Allow any parameters': '/?(?:\?[]\d!"#$%&\'()*+,./:;<=>?@\[\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/?(?:\?[\d!$&\'()*+,.=_a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]': '/?(?:\?[A-Za-z0-9._-]*)?',
            'Specific parameters only': {
                'one': '?\?{}(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?',
                'multiple': '\?(?:{})(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?&?){{{}}}'
            }
        }
    },

    Target.CSHARP: {
        'scheme': {
            'http': 'http://',
            'https': 'https://',
            'http;https': 'https?://',
            'http;https;www.': '(?:https?//|www\\.)',
            'ftp': 'ftp://',
            'ftp;ftp.': '(?:ftp://|ftp\\.)',
            'ftp;http': '(?:ht|f)tp://',
            'ftp;http;ftp.;www.': '(?:(?:ht|f)tp://|(?:ftp|www)\\.)',
            'file': 'file://',
            'file;http;https': '(?:file|https?)://',
            'file;http;https;www.': '(?:(?:file|https?)://|www\\.)',
            'file;ftp': 'f(?:ile|tp)://',
            'file;ftp;http;https': '(?:file|ftp|https?)://',
            'file;ftp;http;https;ftp.;www.': '(?:(?:file|ftp|https?)://|(?:ftp|www)\\.)',
            'feed': 'feed://',
            'feed;http;https': '(?:feed|https?)://',
            'feed;http;https;www.': '(?:(?:feed|https?)://|www\\.)',
            'news;nntp': 'bn(?:ews|ntp)://',
            'news;nntp;news.': '(?:n(?:ews|ntp)://|news\\.)',
            'dns': 'dns://',
            'ldap': 'ldap://',
            'nfs': 'nfs://',
            'pop': 'pop://',
            'rtsp': 'rtsp://',
            'snmp': 'snmp://'
        },
        'username': {
            'No user names': '',
            'Allow any user name': '(?:[]\d!"#$%&\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]+{}{}?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:[\d!$\'()*+,._a-z-]+{}{}?',
            'Basic characters only [A-Za-z0-9._-]': '(?:[\d._a-z-]+{}{}?',
            'Specific user names only': ''
        },
        'password': {
            'No password': '',
            'Optional password': '(?::[\\d!#$%&\'*+./=?_`a-z{|}~^-]+)?@)?',
            'Require password': ':[\\d!#$%&\'*+./=?_`a-z{|}~^-]+@)?',
            'specUserOptionalPassword': '(?::[\\w!#$%&\'*+./=?`{|}~^-]+)?@',
            'specUserRequirePassword': ':[\\w!#$%&\'*+./=?`{|}~^-]+@'
        },
        'host': {
            'Allow any domain name': "(?:[\\da-z-]+\\.)+[a-z]{2,63}",
            'Allow any domain on specific TLD(s)': "(?:[\\da-z-]+\\.)+{}",
            'Allow any subdomain on specific domain(s)': "(?:[\\da-z-]+\\.)*{}"
        },
        'portNumbers': {
            'No port number': '',
            'Optional port number': '(?::\\d{1,5})?',
            'Specify optional port numbers': '(:{})?',
            'Require port number': ':\\d{1,5}',
            'Specify required port numbers': ':{}'
        },
        'folders': {
            'No folders': '',
            'Allow any path': '(?:/[]\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+)',
            'Safe URL characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\d!$\'()*+,._a-z-]+)',
            'Safe folder characters only [A-Za-z0-9$_+!\'(),-]': '(?:/[\\d!$\'()+,_a-z-]+)',
            'Basic characters only [A-Za-z0-9._-]': '(?:/[\\d._a-z-]+)',
            'Basic folder characters only [A-Za-z0-9_-]': '(?:/[\d_a-z-]+)',
            'Specific folders only': '(?:{})?'
        },
        'fileNames': {
            'required': {
                'Allow any file name': '/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+',
                'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/[\\d!$\'()*+,._a-z-]+',
                'Basic characters only [A-Za-z0-9._-]': '/[\\d._a-z-]+',
                'Specific extensions only': '/[\\w.-]+\\.{}',
                'Specific file names only': '/{}'
            },
            'optional': {
                'Allow any file name': '(?:/[]\\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]*)?',
                'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\d!$\'()*+,._a-z-]*)?',
                'Basic characters only [A-Za-z0-9._-]': '(?:/[\\d._a-z-]*)?',
                'Specific extensions only': '(?:/[\\w.-]+\\.{}?)?',
                'Specific file names only': '(?:/{}?)?'
            }
        },
        'parameters': {
            'Allow any parameters': '/?(?:\?[]\d!"#$%&\'()*+,./:;<=>?@\[\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/?(?:\?[\d!$&\'()*+,.=_a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]': '/?(?:\?[A-Za-z0-9._-]*)?',
            'Specific parameters only': {
                'one': '?\?{}(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?',
                'multiple': '\?(?:{})(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?&?){{{}}}'
            }
        }
    },

    Target.SCALA: {
        'scheme': {
            'http': 'http://',
            'https': 'https://',
            'http;https': 'https?://',
            'http;https;www.': '(?:https?//|www\\\\.)',
            'ftp': 'ftp://',
            'ftp;ftp.': '(?:ftp://|ftp\\\\.)',
            'ftp;http': '(?:ht|f)tp://',
            'ftp;http;ftp.;www.': '(?:(?:ht|f)tp://|(?:ftp|www)\\\\.)',
            'file': 'file://',
            'file;http;https': '(?:file|https?)://',
            'file;http;https;www.': '(?:(?:file|https?)://|www\\\\.)',
            'file;ftp': 'f(?:ile|tp)://',
            'file;ftp;http;https': '(?:file|ftp|https?)://',
            'file;ftp;http;https;ftp.;www.': '(?:(?:file|ftp|https?)://|(?:ftp|www)\\\\.)',
            'feed': 'feed://',
            'feed;http;https': '(?:feed|https?)://',
            'feed;http;https;www.': '(?:(?:feed|https?)://|www\\\\.)',
            'news;nntp': 'bn(?:ews|ntp)://',
            'news;nntp;news.': '(?:n(?:ews|ntp)://|news\\\\.)',
            'dns': 'dns://',
            'ldap': 'ldap://',
            'nfs': 'nfs://',
            'pop': 'pop://',
            'rtsp': 'rtsp://',
            'snmp': 'snmp://'
        },
        'username': {
            'No user names': '',
            'Allow any user name': '(?:[]\d!"#$%&\'()*+,./:;<=>?@\[\\\\_`a-z{{|}}~^-]+{}{}?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:[\d!$\'()*+,._a-z-]+{}{}?',
            'Basic characters only [A-Za-z0-9._-]': '(?:[\d._a-z-]+{}{}?',
            'Specific user names only': ''
        },
        'password': {
            'No password': '',
            'Optional password': '(?::[\\\\d!#$%&\'*+./=?_`a-z{|}~^-]+)?@)?',
            'Require password': ':[\\\\d!#$%&\'*+./=?_`a-z{|}~^-]+@)?',
            'specUserOptionalPassword': '(?::[\\\\w!#$%&\'*+./=?`{|}~^-]+)?@',
            'specUserRequirePassword': ':[\\\\w!#$%&\'*+./=?`{|}~^-]+@'
        },
        'host': {
            'Allow any domain name': "(?:[\\\\da-z-]++\\\\.)+[a-z]{2,63}+",
            'Allow any domain on specific TLD(s)': "(?:[\\\\da-z-]++\\\\.)+{}",
            'Allow any subdomain on specific domain(s)': "(?:[\\\\da-z-]++\\\\.)*{}"
        },
        'portNumbers': {
            'No port number': '',
            'Optional port number': '(?::\\\\d{1,5}+)?',
            'Specify optional port numbers': '(:{})?',
            'Require port number': ':\\\\d{1,5}+',
            'Specify required port numbers': ':{}'
        },
        'folders': {
            'No folders': '',
            'Allow any path': '(?:/[]\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+)',
            'Safe URL characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\\\d!$\'()*+,._a-z-]++)',
            'Safe folder characters only [A-Za-z0-9$_+!\'(),-]': '(?:/[\\\\d!$\'()+,_a-z-]++)',
            'Basic characters only [A-Za-z0-9._-]': '(?:/[\\\\d._a-z-]++)',
            'Basic folder characters only [A-Za-z0-9_-]': '(?:/[\d_a-z-]++)',
            'Specific folders only': '(?:{})?'
        },
        'fileNames': {
            'required': {
                'Allow any file name': '/[]\\\\d!"#$%&\'()*+,.:;<=>?@\[\\\\_`a-z{|}~^-]+',
                'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/[\\\\d!$\'()*+,._a-z-]+',
                'Basic characters only [A-Za-z0-9._-]': '/[\\\\d._a-z-]+',
                'Specific extensions only': '/[\\\\w.-]+\\\\.{}',
                'Specific file names only': '/{}'
            },
            'optional': {
                'Allow any file name': '(?:/[]\\\\d!"#$%&\'()*+,.:;<=>?@\[\\\\_`a-z{|}~^-]*)?',
                'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\\\d!$\'()*+,._a-z-]*)?',
                'Basic characters only [A-Za-z0-9._-]': '(?:/[\\\\d._a-z-]*)?',
                'Specific extensions only': '(?:/[\\\\w.-]+\\\\.{}?)?',
                'Specific file names only': '(?:/{}?)?'
            }
        },
        'parameters': {
            'Allow any parameters': '/?(?:\?[]\d!"#$%&\'()*+,./:;<=>?@\[\\\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/?(?:\?[\d!$&\'()*+,.=_a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]': '/?(?:\?[A-Za-z0-9._-]*)?',
            'Specific parameters only': {
                'one': '?\?{}(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?',
                'multiple': '\?(?:{})(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?&?){{{}}}'
            }
        }
    },

    Target.KOTLIN: {
        'scheme': {
            'http': 'http://',
            'https': 'https://',
            'http;https': 'https?://',
            'http;https;www.': '(?:https?//|www\\\\.)',
            'ftp': 'ftp://',
            'ftp;ftp.': '(?:ftp://|ftp\\\\.)',
            'ftp;http': '(?:ht|f)tp://',
            'ftp;http;ftp.;www.': '(?:(?:ht|f)tp://|(?:ftp|www)\\\\.)',
            'file': 'file://',
            'file;http;https': '(?:file|https?)://',
            'file;http;https;www.': '(?:(?:file|https?)://|www\\\\.)',
            'file;ftp': 'f(?:ile|tp)://',
            'file;ftp;http;https': '(?:file|ftp|https?)://',
            'file;ftp;http;https;ftp.;www.': '(?:(?:file|ftp|https?)://|(?:ftp|www)\\\\.)',
            'feed': 'feed://',
            'feed;http;https': '(?:feed|https?)://',
            'feed;http;https;www.': '(?:(?:feed|https?)://|www\\\\.)',
            'news;nntp': 'bn(?:ews|ntp)://',
            'news;nntp;news.': '(?:n(?:ews|ntp)://|news\\\\.)',
            'dns': 'dns://',
            'ldap': 'ldap://',
            'nfs': 'nfs://',
            'pop': 'pop://',
            'rtsp': 'rtsp://',
            'snmp': 'snmp://'
        },
        'username': {
            'No user names': '',
            'Allow any user name': '(?:[]\d!"#$%&\'()*+,./:;<=>?@\[\\\\_`a-z{{|}}~^-]+{}{}?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:[\d!$\'()*+,._a-z-]+{}{}?',
            'Basic characters only [A-Za-z0-9._-]': '(?:[\d._a-z-]+{}{}?',
            'Specific user names only': ''
        },
        'password': {
            'No password': '',
            'Optional password': '(?::[\\\\d!#$%&\'*+./=?_`a-z{|}~^-]+)?@)?',
            'Require password': ':[\\\\d!#$%&\'*+./=?_`a-z{|}~^-]+@)?',
            'specUserOptionalPassword': '(?::[\\\\w!#$%&\'*+./=?`{|}~^-]+)?@',
            'specUserRequirePassword': ':[\\\\w!#$%&\'*+./=?`{|}~^-]+@'
        },
        'host': {
            'Allow any domain name': "(?:[\\\\da-z-]++\\\\.)+[a-z]{2,63}+",
            'Allow any domain on specific TLD(s)': "(?:[\\\\da-z-]++\\\\.)+{}",
            'Allow any subdomain on specific domain(s)': "(?:[\\\\da-z-]++\\\\.)*{}"
        },
        'portNumbers': {
            'No port number': '',
            'Optional port number': '(?::\\\\d{1,5}+)?',
            'Specify optional port numbers': '(:{})?',
            'Require port number': ':\\\\d{1,5}+',
            'Specify required port numbers': ':{}'
        },
        'folders': {
            'No folders': '',
            'Allow any path': '(?:/[]\d!"#$%&\'()*+,.:;<=>?@\[\\_`a-z{|}~^-]+)',
            'Safe URL characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\\\d!$\'()*+,._a-z-]++)',
            'Safe folder characters only [A-Za-z0-9$_+!\'(),-]': '(?:/[\\\\d!$\'()+,_a-z-]++)',
            'Basic characters only [A-Za-z0-9._-]': '(?:/[\\\\d._a-z-]++)',
            'Basic folder characters only [A-Za-z0-9_-]': '(?:/[\d_a-z-]++)',
            'Specific folders only': '(?:{})?'
        },
        'fileNames': {
            'required': {
                'Allow any file name': '/[]\\\\d!"#$%&\'()*+,.:;<=>?@\[\\\\_`a-z{|}~^-]+',
                'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/[\\\\d!$\'()*+,._a-z-]+',
                'Basic characters only [A-Za-z0-9._-]': '/[\\\\d._a-z-]+',
                'Specific extensions only': '/[\\\\w.-]+\\\\.{}',
                'Specific file names only': '/{}'
            },
            'optional': {
                'Allow any file name': '(?:/[]\\\\d!"#$%&\'()*+,.:;<=>?@\[\\\\_`a-z{|}~^-]*)?',
                'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '(?:/[\\\\d!$\'()*+,._a-z-]*)?',
                'Basic characters only [A-Za-z0-9._-]': '(?:/[\\\\d._a-z-]*)?',
                'Specific extensions only': '(?:/[\\\\w.-]+\\\\.{}?)?',
                'Specific file names only': '(?:/{}?)?'
            }
        },
        'parameters': {
            'Allow any parameters': '/?(?:\?[]\d!"#$%&\'()*+,./:;<=>?@\[\\\\_`a-z{|}~^-]*)?',
            'Safe characters only [A-Za-z0-9$_.+!*\'(),-]': '/?(?:\?[\d!$&\'()*+,.=_a-z-]*)?',
            'Basic characters only [A-Za-z0-9._-]': '/?(?:\?[A-Za-z0-9._-]*)?',
            'Specific parameters only': {
                'one': '?\?{}(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?',
                'multiple': '\?(?:{})(?:=[]\d!"#$%\'()*+,./:;<=>?@\[\\_`a-z{{|}}~^-]*+)?&?){{{}}}'
            }
        }
    }

}

