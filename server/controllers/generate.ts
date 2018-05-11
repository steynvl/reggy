import BaseCtrl from './base';
import * as child_process from 'child_process';
import * as path from 'path';

export default class GenerateCtrl extends BaseCtrl {

  model = null;

  generate = (req, res) => {
    const samples = req.body.params;
    console.log('---------');
    console.log(samples);
    console.log('---------');

    const pathToRegex = path.join(__dirname, '..', '..', '..', 'server', 'regy', 'main.py');
    const py = child_process.spawn('python3', [pathToRegex].concat(samples));
    let output = '';

    py.stdout.on('data', (data) => {
      output += data.toString();
    });

    py.on('close', (code) => {
      res.setHeader('Content-Type', 'application/json');

      const deserialized = JSON.parse(output);

      const serverResponse: ServerResponse = {
        regex        : deserialized.regex,
        compiledRegex: deserialized.compiledRegex,
        code         : code
      };

      res.send(JSON.stringify(serverResponse));
    });

  }

}

export interface ServerResponse {
  regex        : string;
  compiledRegex: string;
  code         : number;
}
