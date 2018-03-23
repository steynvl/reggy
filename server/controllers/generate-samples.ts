import BaseCtrl from './base';
import * as child_process from 'child_process';

export default class GenerateSamplesCtrl extends BaseCtrl {

  model = null;

  generate = (req, res) => {
    const samples = req.body.params;

    const pathToRegex = process.env.PATH_TO_REGEX;
    const py = child_process.spawn('python3', [pathToRegex].concat(samples));
    let regex = '';

    py.stdout.on('data', (data) => {
      regex += data.toString();
    });

    py.stdout.on('end', () => {
      console.log('-----');
      console.log(`Regex = ${regex.trim()}`);
      console.log('-----');
      res.setHeader('Content-Type', 'application/json');
      res.send(JSON.stringify(regex));
    });

    py.on('close', (code) => {
      console.log(`Exit code = ${code}`);
      if (code !== 0) {
        // TODO something went wrong
      }
    });

  };

}

