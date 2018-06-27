import * as path from 'path';
import * as child_process from 'child_process';

export default class InferrerCtrl {

  inferGrammar = (req, res) => {
    const samples = req.body.params;
    console.log('---------');
    console.log(samples);
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
        dot          : deserialized.dot,
        code         : code
      };

      res.send(JSON.stringify(serverResponse));
    });

  }

}

function spawnChildProcess(info) {
  const pathToRegex = path.join(__dirname, '..', '..', '..', 'server', 'reggy', 'reggy', 'inferrer',  'main.py');
  return child_process.spawn('python3', [pathToRegex].concat(info));
}

interface ServerResponse {
  code: number;
  regex: string;
  dot: string;

}
