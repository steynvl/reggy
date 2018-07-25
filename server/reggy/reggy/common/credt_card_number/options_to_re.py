from reggy.samples.tokens import Target

credit_card_to_re = {

    Target.JAVA: {

        'visa'           : {
            'No spaces or dashes'              : '4\\\\d{12}(?:\\\\d{3})?',
            'Spaces and dashes to group digits': '4\\\\d{3}[ -]*\\\\d{4}[ -]*\\\\d{4}[ -]*\\\\d(?:\\\\d{3})?',
            'Spaces and dashes anywhere'       : '4[ -]*(?:\\\\d[ -]*){11}(?:(?:\\\\d[ -]*){3})?\\\\d'
        },
        'dinersClub'     : {
            'No spaces or dashes'              : '3(?:0[0-5]|[68]\\\\d)\\\\d{11}',
            'Spaces and dashes to group digits': '3(?:0[0-5]|[68]\\\\d)\\\\d[ -]*\\\\d{6}[ -]*\\\\d{4}',
            'Spaces and dashes anywhere'       : '3[ -]*(?:0[ -]*[0-5]|[68][ -]*\\\\d)(?:[ -]*\\\\d){11}'
        },
        'masterCard'     : {
            'No spaces or dashes'              : '(?:5[1-5]\\\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])\\\\d{12}',
            'Spaces and dashes to group digits': '(?:5[1-5]\\\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])[ -]*\\\\d{4}[ -]*\\\\d{4}[ -]*\\\\d{4}',
            'Spaces and dashes anywhere'       : '(?:5[ -]*[1-5](?:[ -]*\\\\d){2}|(?:2[ -]*){3}[1-9]|(?:2[ -]*){2}[3-9][ -]*\\\\d|2[ -]*[3-6](?:[ -]*\\\\d){2}|2[ -]*7[ -]*[01][ -]*\\\\d|2[ -]*7[ -]*2[ -]*0)(?:[ -]*\\\\d){12}'
        },
        'discover'       : {
            'No spaces or dashes'              : '6(?:011|5\\\\d{2})\\\\d{12}',
            'Spaces and dashes to group digits': '6(?:011|5\\\\d{2})[ -]*\\\\d{4}[ -]*\\\\d{4}[ -]*\\\\d{4}',
            'Spaces and dashes anywhere'       : '6[ -]*(?:0[ -]*1[ -]*1|5[ -]*\\\\d[ -]*\\\\d)(?:[ -]*\\\\d){12}'
        },
        'americanExpress': {
            'No spaces or dashes'              : '3[47]\\\\d{13}',
            'Spaces and dashes to group digits': '3[47]\\\\d{2}[ -]*\\\\d{6}[ -]*\\\\d{5}',
            'Spaces and dashes anywhere'       : '3[ -]*[47](?:[ -]*\\\\d){13}'
        },
        'jcb'            : {
            'No spaces or dashes'              : '(?:2131|1800|35\\\\d{3})\\\\d{11}',
            'Spaces and dashes to group digits': '(?:2131|1800)[ -]*\\\\d{6}[ -]*\d{5}|35\\\\d{2}[ -]*\\\\d{4}[ -]*\\\\d{4}[ -]*\\\\d{4}',
            'Spaces and dashes anywhere'       : '(?:2[ -]*1[ -]*3[ -]*1|1[ -]*8[ -]*0[ -]*0|3[ -]*5(?:[ -]*\\\\d){3})(?:[ -]*\\\\d){11}'
        },


    },

    Target.PERL: {
        'visa'           : {
            'No spaces or dashes'              : '4\\d{12}(?:\\d{3})?',
            'Spaces and dashes to group digits': '4\\d{3}[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d(?:\\d{3})?',
            'Spaces and dashes anywhere'       : '4[ -]*(?:\\d[ -]*){11}(?:(?:\\d[ -]*){3})?\\d'
        },
        'dinersClub'     : {
            'No spaces or dashes'              : '3(?:0[0-5]|[68]\\d)\\d{11}',
            'Spaces and dashes to group digits': '3(?:0[0-5]|[68]\\d)\\d[ -]*\\d{6}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '3[ -]*(?:0[ -]*[0-5]|[68][ -]*\\d)(?:[ -]*\\d){11}'
        },
        'masterCard'     : {
            'No spaces or dashes'              : '(?:5[1-5]\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])\\d{12}',
            'Spaces and dashes to group digits': '(?:5[1-5]\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '(?:5[ -]*[1-5](?:[ -]*\\d){2}|(?:2[ -]*){3}[1-9]|(?:2[ -]*){2}[3-9][ -]*\\d|2[ -]*[3-6](?:[ -]*\\d){2}|2[ -]*7[ -]*[01][ -]*\\d|2[ -]*7[ -]*2[ -]*0)(?:[ -]*\\d){12}'
        },
        'discover'       : {
            'No spaces or dashes'              : '6(?:011|5\\d{2})\\d{12}',
            'Spaces and dashes to group digits': '6(?:011|5\\d{2})[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '6[ -]*(?:0[ -]*1[ -]*1|5[ -]*\\d[ -]*\\d)(?:[ -]*\\d){12}'
        },
        'americanExpress': {
            'No spaces or dashes'              : '3[47]\\d{13}',
            'Spaces and dashes to group digits': '3[47]\\d{2}[ -]*\\d{6}[ -]*\\d{5}',
            'Spaces and dashes anywhere'       : '3[ -]*[47](?:[ -]*\\d){13}'
        },
        'jcb'            : {
            'No spaces or dashes'              : '(?:2131|1800|35\\d{3})\\d{11}',
            'Spaces and dashes to group digits': '(?:2131|1800)[ -]*\\d{6}[ -]*\d{5}|35\\d{2}[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '(?:2[ -]*1[ -]*3[ -]*1|1[ -]*8[ -]*0[ -]*0|3[ -]*5(?:[ -]*\\d){3})(?:[ -]*\\d){11}'
        }
    },

    Target.POSIX: {
        'visa'           : {
            'No spaces or dashes'              : '4\\d{12}(?:\\d{3})?',
            'Spaces and dashes to group digits': '4\\d{3}[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d(?:\\d{3})?',
            'Spaces and dashes anywhere'       : '4[ -]*(?:\\d[ -]*){11}(?:(?:\\d[ -]*){3})?\\d'
        },
        'dinersClub'     : {
            'No spaces or dashes'              : '3(?:0[0-5]|[68]\\d)\\d{11}',
            'Spaces and dashes to group digits': '3(?:0[0-5]|[68]\\d)\\d[ -]*\\d{6}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '3[ -]*(?:0[ -]*[0-5]|[68][ -]*\\d)(?:[ -]*\\d){11}'
        },
        'masterCard'     : {
            'No spaces or dashes'              : '(?:5[1-5]\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])\\d{12}',
            'Spaces and dashes to group digits': '(?:5[1-5]\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '(?:5[ -]*[1-5](?:[ -]*\\d){2}|(?:2[ -]*){3}[1-9]|(?:2[ -]*){2}[3-9][ -]*\\d|2[ -]*[3-6](?:[ -]*\\d){2}|2[ -]*7[ -]*[01][ -]*\\d|2[ -]*7[ -]*2[ -]*0)(?:[ -]*\\d){12}'
        },
        'discover'       : {
            'No spaces or dashes'              : '6(?:011|5\\d{2})\\d{12}',
            'Spaces and dashes to group digits': '6(?:011|5\\d{2})[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '6[ -]*(?:0[ -]*1[ -]*1|5[ -]*\\d[ -]*\\d)(?:[ -]*\\d){12}'
        },
        'americanExpress': {
            'No spaces or dashes'              : '3[47]\\d{13}',
            'Spaces and dashes to group digits': '3[47]\\d{2}[ -]*\\d{6}[ -]*\\d{5}',
            'Spaces and dashes anywhere'       : '3[ -]*[47](?:[ -]*\\d){13}'
        },
        'jcb'            : {
            'No spaces or dashes'              : '(?:2131|1800|35\\d{3})\\d{11}',
            'Spaces and dashes to group digits': '(?:2131|1800)[ -]*\\d{6}[ -]*\d{5}|35\\d{2}[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '(?:2[ -]*1[ -]*3[ -]*1|1[ -]*8[ -]*0[ -]*0|3[ -]*5(?:[ -]*\\d){3})(?:[ -]*\\d){11}'
        }
    },

    Target.PYTHON: {
        'visa'           : {
            'No spaces or dashes'              : '4\\d{12}(?:\\d{3})?',
            'Spaces and dashes to group digits': '4\\d{3}[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d(?:\\d{3})?',
            'Spaces and dashes anywhere'       : '4[ -]*(?:\\d[ -]*){11}(?:(?:\\d[ -]*){3})?\\d'
        },
        'dinersClub'     : {
            'No spaces or dashes'              : '3(?:0[0-5]|[68]\\d)\\d{11}',
            'Spaces and dashes to group digits': '3(?:0[0-5]|[68]\\d)\\d[ -]*\\d{6}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '3[ -]*(?:0[ -]*[0-5]|[68][ -]*\\d)(?:[ -]*\\d){11}'
        },
        'masterCard'     : {
            'No spaces or dashes'              : '(?:5[1-5]\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])\\d{12}',
            'Spaces and dashes to group digits': '(?:5[1-5]\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '(?:5[ -]*[1-5](?:[ -]*\\d){2}|(?:2[ -]*){3}[1-9]|(?:2[ -]*){2}[3-9][ -]*\\d|2[ -]*[3-6](?:[ -]*\\d){2}|2[ -]*7[ -]*[01][ -]*\\d|2[ -]*7[ -]*2[ -]*0)(?:[ -]*\\d){12}'
        },
        'discover'       : {
            'No spaces or dashes'              : '6(?:011|5\\d{2})\\d{12}',
            'Spaces and dashes to group digits': '6(?:011|5\\d{2})[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '6[ -]*(?:0[ -]*1[ -]*1|5[ -]*\\d[ -]*\\d)(?:[ -]*\\d){12}'
        },
        'americanExpress': {
            'No spaces or dashes'              : '3[47]\\d{13}',
            'Spaces and dashes to group digits': '3[47]\\d{2}[ -]*\\d{6}[ -]*\\d{5}',
            'Spaces and dashes anywhere'       : '3[ -]*[47](?:[ -]*\\d){13}'
        },
        'jcb'            : {
            'No spaces or dashes'              : '(?:2131|1800|35\\d{3})\\d{11}',
            'Spaces and dashes to group digits': '(?:2131|1800)[ -]*\\d{6}[ -]*\d{5}|35\\d{2}[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere'       : '(?:2[ -]*1[ -]*3[ -]*1|1[ -]*8[ -]*0[ -]*0|3[ -]*5(?:[ -]*\\d){3})(?:[ -]*\\d){11}'
        }
    },

    Target.JAVASCRIPT: {
        'visa': {
            'No spaces or dashes': '4\\d{12}(?:\\d{3})?',
            'Spaces and dashes to group digits': '4\\d{3}[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d(?:\\d{3})?',
            'Spaces and dashes anywhere': '4[ -]*(?:\\d[ -]*){11}(?:(?:\\d[ -]*){3})?\\d'
        },
        'dinersClub': {
            'No spaces or dashes': '3(?:0[0-5]|[68]\\d)\\d{11}',
            'Spaces and dashes to group digits': '3(?:0[0-5]|[68]\\d)\\d[ -]*\\d{6}[ -]*\\d{4}',
            'Spaces and dashes anywhere': '3[ -]*(?:0[ -]*[0-5]|[68][ -]*\\d)(?:[ -]*\\d){11}'
        },
        'masterCard': {
            'No spaces or dashes': '(?:5[1-5]\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])\\d{12}',
            'Spaces and dashes to group digits': '(?:5[1-5]\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere': '(?:5[ -]*[1-5](?:[ -]*\\d){2}|(?:2[ -]*){3}[1-9]|(?:2[ -]*){2}[3-9][ -]*\\d|2[ -]*[3-6](?:[ -]*\\d){2}|2[ -]*7[ -]*[01][ -]*\\d|2[ -]*7[ -]*2[ -]*0)(?:[ -]*\\d){12}'
        },
        'discover': {
            'No spaces or dashes': '6(?:011|5\\d{2})\\d{12}',
            'Spaces and dashes to group digits': '6(?:011|5\\d{2})[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere': '6[ -]*(?:0[ -]*1[ -]*1|5[ -]*\\d[ -]*\\d)(?:[ -]*\\d){12}'
        },
        'americanExpress': {
            'No spaces or dashes': '3[47]\\d{13}',
            'Spaces and dashes to group digits': '3[47]\\d{2}[ -]*\\d{6}[ -]*\\d{5}',
            'Spaces and dashes anywhere': '3[ -]*[47](?:[ -]*\\d){13}'
        },
        'jcb': {
            'No spaces or dashes': '(?:2131|1800|35\\d{3})\\d{11}',
            'Spaces and dashes to group digits': '(?:2131|1800)[ -]*\\d{6}[ -]*\d{5}|35\\d{2}[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
            'Spaces and dashes anywhere': '(?:2[ -]*1[ -]*3[ -]*1|1[ -]*8[ -]*0[ -]*0|3[ -]*5(?:[ -]*\\d){3})(?:[ -]*\\d){11}'
        }
    },

    Target.PHP: {
      'visa': {
        'No spaces or dashes': '4\\d{12}(?:\\d{3})?',
        'Spaces and dashes to group digits': '4\\d{3}[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d(?:\\d{3})?',
        'Spaces and dashes anywhere': '4[ -]*(?:\\d[ -]*){11}(?:(?:\\d[ -]*){3})?\\d'
      },
      'dinersClub': {
        'No spaces or dashes': '3(?:0[0-5]|[68]\\d)\\d{11}',
        'Spaces and dashes to group digits': '3(?:0[0-5]|[68]\\d)\\d[ -]*\\d{6}[ -]*\\d{4}',
        'Spaces and dashes anywhere': '3[ -]*(?:0[ -]*[0-5]|[68][ -]*\\d)(?:[ -]*\\d){11}'
      },
      'masterCard': {
        'No spaces or dashes': '(?:5[1-5]\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])\\d{12}',
        'Spaces and dashes to group digits': '(?:5[1-5]\\d{2}|2720|27[01][0-9]|2[3-6][0-9]{2}|22[3-9][0-9]|222[1-9])[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
        'Spaces and dashes anywhere': '(?:5[ -]*[1-5](?:[ -]*\\d){2}|(?:2[ -]*){3}[1-9]|(?:2[ -]*){2}[3-9][ -]*\\d|2[ -]*[3-6](?:[ -]*\\d){2}|2[ -]*7[ -]*[01][ -]*\\d|2[ -]*7[ -]*2[ -]*0)(?:[ -]*\\d){12}'
      },
      'discover': {
        'No spaces or dashes': '6(?:011|5\\d{2})\\d{12}',
        'Spaces and dashes to group digits': '6(?:011|5\\d{2})[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
        'Spaces and dashes anywhere': '6[ -]*(?:0[ -]*1[ -]*1|5[ -]*\\d[ -]*\\d)(?:[ -]*\\d){12}'
      },
      'americanExpress': {
        'No spaces or dashes': '3[47]\\d{13}',
        'Spaces and dashes to group digits': '3[47]\\d{2}[ -]*\\d{6}[ -]*\\d{5}',
        'Spaces and dashes anywhere': '3[ -]*[47](?:[ -]*\\d){13}'
      },
      'jcb': {
        'No spaces or dashes': '(?:2131|1800|35\\d{3})\\d{11}',
        'Spaces and dashes to group digits': '(?:2131|1800)[ -]*\\d{6}[ -]*\d{5}|35\\d{2}[ -]*\\d{4}[ -]*\\d{4}[ -]*\\d{4}',
        'Spaces and dashes anywhere': '(?:2[ -]*1[ -]*3[ -]*1|1[ -]*8[ -]*0[ -]*0|3[ -]*5(?:[ -]*\\d){3})(?:[ -]*\\d){11}'
      }
    }

}
