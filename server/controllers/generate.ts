import BaseCtrl from './base';
import * as child_process from 'child_process';

export default class GenerateCtrl extends BaseCtrl {

  model = null;

  generate = (req, res) => {
    const samples = Object.values(req.query);
    const pathToRegex = process.env.PATH_TO_REGEX;

    console.log([pathToRegex].concat(samples));
    const py = child_process.spawn('python3', [pathToRegex].concat(samples));
    let regex = '';

    py.stdout.on('data', (data) => {
      regex += data.toString();
    });

    py.stdout.on('end', () => {
      console.log(`Regex = ${regex.trim()}`);
      res.setHeader('Content-Type', 'application/json');
      res.send(regex);
    });

    py.on('close', (code) => {
      console.log(`Exit code = ${code}`);
      if (code !== 0) {
        // TODO something went wrong
      }
    });

  };

}

