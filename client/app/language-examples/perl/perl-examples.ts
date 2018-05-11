
const examples = {

  'Create an object to use the same regex for many operations':
  '__compile__\n',

  'if/else branch whether the regex matches (part of) a string':
  'if ($subject =~ m/__regex__/) {\n' +
  '    # Successful match\n' +
  '} else {\n' +
  '    # Match attempt failed\n' +
  '}\n',
  'if/else branch whether the regex matches a string entirely':
  'if ($subject =~ m/\\A__regex__\\z/) {\n' +
  '    # Successful match\n' +
  '} else {\n' +
  '    # Match attempt failed\n' +
  '}\n',
  'Get the part of a string matched by the regex':
  'if ($subject =~ m/__regex__/) {\n' +
  '    $result = $&;\n' +
  '} else {\n' +
  '    $result = "";\n' +
  '}\n',
  'Get the part of a string matched by a numbered group':
  'if ($subject =~ m/__regex__/) {\n' +
  '    $result = $1;\n' +
  '} else {\n' +
  '    $result = "";\n' +
  '}\n',

  'Get an array of all regex matches in a string':
  '@result = $subject =~ m/__regex__/g;',
  'Iterate over all matches in a string': 'while ($subject =~ m/__regex__/g) {\n' +
  '    # matched text = $&\n' +
  '}\n'

};

export { examples };
