import * as child_process from 'child_process';
import * as path from 'path';

export default class GenerateCtrl {

  generateRegex = (req, res) => {
    const samples = req.body.params;
    console.log('---------');
    console.log(samples);
    console.log(JSON.stringify(JSON.parse(samples), null, 2));
    console.log('---------');

    const py = spawnChildProcess(samples);
    let output = '';

    py.stdout.on('data', (data) => {
      output += data.toString();
    });

    py.on('close', (code) => {
      res.setHeader('Content-Type', 'application/json');

      let deserialized;
      if (code === 0) {
        deserialized = JSON.parse(output);
      }

      const serverResponse: ServerResponse = {
        regex        : deserialized.regex,
        compiledRegex: deserialized.compiledRegex,
        code         : code
      };

      res.send(JSON.stringify(serverResponse));
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
