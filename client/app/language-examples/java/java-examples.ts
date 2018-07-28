
const examples = {

  'Import regex library':
  'import java.util.regex.*;\n',

  'Test if the regex matches a string':
  'boolean matches = subjectString.matches("__regex__");\n',

  'if/else to check whether the regex matches a string':
  'if (subjectString.matches("__regex__")) {\n' +
  '    /* string matched */\n' +
  '} else {\n' +
  '    /* string did not match */\n' +
  '} \n',

  'Compile regex object to use multiple times':
  '__compile__\n',

  'Apply regex object to a given string':
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n',

  'Apply regex object to more than one string':
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString1);\n' +
  '\n' +
  'matcher.reset(subjectString2);\n',

  'Use regex object to test if part of a string can be matched':
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'boolean foundMatch = matcher.find();\n',

  'Use regex object to test if a string can be matched entirely':
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'boolean foundMatch = matcher.matches();\n',

  'Use regex object in if/else branch to check if part of a string can be matched':
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'if (matcher.find()) {\n' +
  '    /* string matched */\n' +
  '} else {\n' +
  '    /* string did not match */\n' +
  '} \n',

  'Use regex object for if/else branch whether a string can be matched entirely':
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'if (matcher.matches()) {\n' +
  '    /* string matched entirely */\n' +
  '} else {\n' +
  '    /* string did not match entirely */\n' +
  '} \n',

  'Use regex object to get the part of a string matched by the regex':
  'String result = null;\n' +
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'if (matcher.find()) {\n' +
  '    result = matcher.group();\n' +
  '} \n',

  'Use regex object to get the part of a string matched by a numbered group':
  'String result = null;\n' +
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'if (matcher.find()) {\n' +
  '    result = matcher.group(1);\n' +
  '} \n',

  'Use regex object to get the part of a string matched by a named group':
  'String result = null;\n' +
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'if (matcher.find()) {\n' +
  '    result = matcher.group("group");\n' +
  '} \n',

  'Use regex object to get a list of all regex matches in a string':
  'List<String> matches = new ArrayList<>();\n' +
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'while (matcher.find()) {\n' +
  '    matches.add(matcher.group());\n' +
  '} \n',

  'Use regex match to get a list of all text matched by a numbered group':
  'List<String> matches = new ArrayList<>();\n' +
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'while (matcher.find()) {\n' +
  '    matches.add(matcher.group(1));\n' +
  '} \n',

  'Use regex object to get a list of all text matched by a named group':
  'List<String> matches = new ArrayList<>();\n' +
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'while (matcher.find()) {\n' +
  '    matches.add(matcher.group("group"));\n' +
  '} \n',

  'Iterate over all regex matches in a string':
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'while (matcher.find()) {\n' +
  '    /* text that was matched: matcher.group() */\n' +
  '    /* start of match: matcher.start() */\n' +
  '    /* end of match: matcher.end() */\n' +
  '} \n',

  'Iterate over all matches and capturing groups in a string':
  '__compile__\n' +
  'Matcher matcher = regex.matcher(subjectString);\n' +
  'while (matcher.find()) {\n' +
  '    for (int i = 1; i <= matcher.groupCount(); i++) {\n' +
  '        /* text that was matched: regexMatcher.group(i) */\n' +
  '        /* start of match: regexMatcher.start(i) */\n' +
  '        /* end of match: regexMatcher.end(i) */\n' +
  '    }\n' +
  '} \n',

};

export { examples };
