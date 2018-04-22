import BaseCtrl from './base';
import * as child_process from 'child_process';

export default class GenerateCtrl extends BaseCtrl {

  model = null;

  generate = (req, res) => {
    const samples = req.body.params;

    const pathToRegex = process.env.PATH_TO_PY;
    const py = child_process.spawn('python3', [pathToRegex].concat(samples));
    let output = '';

    py.stdout.on('data', (data) => {
      output += data.toString();
    });

    py.on('close', (code) => {
      res.setHeader('Content-Type', 'application/json');

      const serverResponse: ServerResponse = {
        regex: output,
        code : code
      };
      res.send(JSON.stringify(serverResponse));
    });

  }

}

export interface ServerResponse {
  regex: string;
  code : number;
}
