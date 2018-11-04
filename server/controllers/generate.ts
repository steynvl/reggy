import * as child_process from 'child_process';
import * as path from 'path';

export default class GenerateCtrl {

  generateRegex = (req, res) => {
    const samples = req.body.params;
    // console.log('---------');
    // console.log(samples);
    // console.log(JSON.stringify(JSON.parse(samples), null, 2));
    // console.log('---------');

    const py = spawnChildProcess(samples);
    let output = '';

    py.stdout.on('data', (data) => {
      output += data.toString();
    });

    py.on('close', (code) => {
      res.setHeader('Content-Type', 'application/json');

      if (code === 0) {
        const deserialised = JSON.parse(output);

        const serverResponse: ServerResponse = {
          regex        : deserialised.regex,
          compiledRegex: deserialised.compiledRegex,
          code         : code
        };

        res.send(JSON.stringify(serverResponse));
      } else {
        res.send(JSON.stringify({code: 1}));
      }
    });

  }

}

function spawnChildProcess(samples) {
  const pathToRegex = path.join(__dirname, '..', '..', '..', 'server', 'reggy', 'main.py');
  return child_process.spawn('python3', [pathToRegex].concat(samples));
}

interface ServerResponse {
  regex        : string;
  compiledRegex: string;
  code         : number;
}
