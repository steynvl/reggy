
const examples = {

  'Import regex library':
  'import java.util.regex.*;\n',

  'Test if the regex matches a string entirely':
  'boolean foundMatch = subjectString.matches("__regex__");\n',

  'if/else branch whether the regex matches a string entirely':
  'if (subjectString.matches("__regex__")) {\n' +
  '    // String matched entirely\n' +
  '} else {\n' +
  '    // Match attempt failed\n' +
  '} \n',

  'Create an object to use the same regex for many operations':
  'Pattern regex = Pattern.compile("__regex__");\n',

  'Create an object to apply a regex repeatedly to a given string':
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n',

  'Apply the same regex to more than one string':
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  '\n' +
  'regexMatcher.reset(anotherSubjectString);\n',

  'Use regex object to test if (part of) a string can be matched':
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'boolean foundMatch = regexMatcher.find();\n',

  'Use regex object to test if a string can be matched entirely':
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'boolean foundMatch = regexMatcher.matches();\n',

  'Use regex object for if/else branch whether (part of) a string can be matched':
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'if (regexMatcher.find()) {\n' +
  '    // Successful match\n' +
  '} else {\n' +
  '    // Match attempt failed\n' +
  '} \n',

  'Use regex object for if/else branch whether a string can be matched entirely':
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'if (regexMatcher.matches()) {\n' +
  '    // String matched entirely\n' +
  '} else {\n' +
  '    // Match attempt failed\n' +
  '} \n',

  'Use regex object to get the part of a string matched by the regex':
  'String ResultString = null;\n' +
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'if (regexMatcher.find()) {\n' +
  '    ResultString = regexMatcher.group();\n' +
  '} \n',

  'Use regex object to get the part of a string matched by a numbered group':
  'String ResultString = null;\n' +
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'if (regexMatcher.find()) {\n' +
  '    ResultString = regexMatcher.group(1);\n' +
  '} \n',

  'Use regex object to get the part of a string matched by a named group':
  'String ResultString = null;\n' +
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'if (regexMatcher.find()) {\n' +
  '    ResultString = regexMatcher.group("group");\n' +
  '} \n',

  'Use regex object to get a list of all regex matches in a string':
  'List<String> matchList = new ArrayList<>();\n' +
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'while (regexMatcher.find()) {\n' +
  '    matchList.add(regexMatcher.group());\n' +
  '} \n',

  'Use regex match to get a list of all text matched by a numbered group':
  'List<String> matchList = new ArrayList<String>();\n' +
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'while (regexMatcher.find()) {\n' +
  '    matchList.add(regexMatcher.group(1));\n' +
  '} \n',

  'Use regex object to get a list of all text matched by a named group':
  'List<String> matchList = new ArrayList<String>();\n' +
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'while (regexMatcher.find()) {\n' +
  '    matchList.add(regexMatcher.group("group"));\n' +
  '} \n',

  'Iterate over all matched in a string':
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'while (regexMatcher.find()) {\n' +
  '    // matched text: regexMatcher.group()\n' +
  '    // match start: regexMatcher.start()\n' +
  '    // match end: regexMatcher.end()\n' +
  '} \n',

  'Iterate over all matches and capturing groups in a string':
  'Pattern regex = Pattern.compile("__regex__");\n' +
  'Matcher regexMatcher = regex.matcher(subjectString);\n' +
  'while (regexMatcher.find()) {\n' +
  '    for (int i = 1; i <= regexMatcher.groupCount(); i++) {\n' +
  '        // matched text: regexMatcher.group(i)\n' +
  '        // match start: regexMatcher.start(i)\n' +
  '        // match end: regexMatcher.end(i)\n' +
  '    }\n' +
  '} \n',

};

export { examples };
